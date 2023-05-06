# adlo-gallery.py
# Author: Lukas Vacula <ldv8434@rit.edu>

import argparse
import logging
import os
import sys

from PIL import Image
from jinja2 import Environment, FileSystemLoader, select_autoescape

# create the main gallery HTML as table and return string
#	input_path: string of location relative to args.input
def create_table_gallery(args, input_path):
	gallery_string = '<table>\n'

	# get list of files in directory
	path_list = [path for path in os.listdir(input_path) if os.path.isfile(os.path.join(input_path,path))]
	path_list.sort()

	num = 0
	while (num < len(path_list)):
		if (num % args.columns) == 0:
			if num == 0:
				gallery_string += '</tr>'
			gallery_string += '<tr>\n'
		path = path_list[num]
		if not args.no_thumbnails:
			create_thumbnail(os.path.join(args.input,path))

		gallery_string += '<td><a href="./img/' + os.path.basename(path) + '">\n'
		if not args.no_thumbnails:
			gallery_string += '<img src="./_thumbnails/' + os.path.basename(path) + '">\n'
		if not args.no_thumbnails:
			gallery_string += '<img src="./img/' + os.path.basename(path) + '">\n'
		gallery_string += '</a></td>\n'

		num += 1

	while ((num % args.columns) == 0):
		gallery_string += "<td></td>"

	gallery_string += "</tr></table>"

	return gallery_string

# create the main gallery HTML as table and return string
#	input_path: string of location relative to args.input
def create_flexbox_gallery(args, input_path):
	gallery_string = '<div class="flex-container">'

	# get list of files in directory
	path_list = [path for path in os.listdir(input_path) if os.path.isfile(os.path.join(input_path,path))]
	path_list.sort()
	for path in path_list:
		if not args.no_thumbnails:
			create_thumbnail(os.path.join(args.input,path))


		gallery_string += '<div><a href="./img/' + os.path.basename(path) + '">\n'
		if not args.no_thumbnails:
			gallery_string += '<img src="./_thumbnails/' + os.path.basename(path) + '">\n'
		if not args.no_thumbnails:
			gallery_string += '<img src="./img/' + os.path.basename(path) + '">\n'
		gallery_string += '</a></div>\n'

	# close flex container
	gallery_string += '</div>'

	return gallery_string

# create thumbnail in the _thumbnails folder
# path: string of path to current image
def create_thumbnail(path):
	filename = os.path.basename(path)
	thumb_path = os.path.join(args.output,'_thumbnails',filename)
	# get path for result

	# check for existing thumbnail; optimizization
	if (not args.regen_thumbnails and os.path.exists(thumb_path)):
		logging.warning("Thumbnail already exists for " + filename)
		return


	if os.path.exists(thumb_path):
			print('Removing existing thumbnail ' + thumb_path)
			os.remove(thumb_path)


	try:
		with Image.open(path) as im:
			if args.thumbnail_quality == 'low':
				im.thumbnail((128,128))
			if args.thumbnail_quality == 'med':
				im.thumbnail((256,256))
			if args.thumbnail_quality == 'low':
				im.thumbnail((512,512))
			im = im.convert('RGB')
			im.save(thumb_path, "JPEG")
	except AssertionError:#OSError:
		logging.error("Error creating thumbnail for " + filename)

	# Debugging option

def create_artist_page(path):
	pass

def main():
	# Create argument parser
	parser = argparse.ArgumentParser(description='Create an HTML gallery')
	parser.add_argument('-v', action='store_true', help='Verbose/debug mode')
	parser.add_argument('-f', action='store_true', help='Use flexbox instead of HTML table')
	css_default_path = os.path.normpath(os.path.dirname(__file__)+os.path.sep+'style.css')
	parser.add_argument('-c','--css', default=css_default_path, help='CSS file to use')
	template_default_path = os.path.normpath(os.path.dirname(__file__)+os.path.sep+'template.html')
	parser.add_argument('-t', default=template_default_path, help='Jinja2 HTML template file to use')
	parser.add_argument('-o', '--output', required=True, help='Output directory to use')
	parser.add_argument('-i', '--input', required=True, help='Input directory to use')
	parser.add_argument('--no-symlink', action='store_true', help='Copy files instead of symlinking them')

	#parser.add_argument('--sorting', default='name-asc', choices=['mtime-asc','mtime-desc','name-asc','name-desc'], help='Sorting setting.')

	group = parser.add_argument_group('thumbnail options')
	group.add_argument('--no-thumbnails', action='store_true', help='Disable thumbnail generation and use full-size images.')
	group.add_argument('--regen-thumbnails', action='store_true', help='Regenerate all thumbnails.')
	group.add_argument('--thumbnail-quality', default='low', choices=['low','med','high'], help='Thumbnail quality.')

	table_group = parser.add_argument_group('table options')
	table_group.add_argument('--columns', default=8, help='Columns to use for tables')



	global args
	args = parser.parse_args()

	# Create logger
	global logger
	logger = logging.getLogger('adlo-gallery')
	handler_out = logging.StreamHandler(sys.stdout)
	handler_out.addFilter(lambda record: record.levelno <= logging.WARNING)
	# Handle verbose mode
	if args.v:
		handler_out.setLevel(logging.DEBUG)
	else:
		handler_out.setLevel(logging.ERROR)
	handler_err = logging.StreamHandler(sys.stderr)
	handler_err.setLevel(logging.ERROR)
	logger.setLevel(logging.DEBUG)
	logger.addHandler(handler_out)
	logger.addHandler(handler_err)

	# Crate Jinja environment
	env = Environment(
		loader=FileSystemLoader(os.path.dirname(args.t)),
		autoescape=False
	)

	# Load template
	template = env.get_template(os.path.basename(args.t))

	# Create output directory if it doesn't exist
	if not os.path.exists(args.output):
		os.mkdir(args.output)

	# Create image source directory if it doesn't exist
	if not os.path.exists(os.path.join(args.output,'img')):
		os.mkdir(os.path.join(args.output,'img'))

	# Create thumbnail directory
	if not args.no_thumbnails and not os.path.exists(os.path.join(args.output,'_thumbnails')):
		os.mkdir(os.path.join(args.output,'_thumbnails'))

	# Generate flexbox/table
	if args.f:
		gallery_string = create_flexbox_gallery()
	else:
		gallery_string = create_table_gallery()


	with open(args.css, 'r') as css_file:
		css_string = css_file.read()

	# Print HTML
	#logger.debug(template.render(CSS=css_string, GALLERY=gallery_string))

	# Write file
	with open(os.path.join(args.output,'index.html'), 'w') as outfile:
		outfile.write(template.render(CSS=css_string, GALLERY=gallery_string))

if __name__ == "__main__":
   main()
