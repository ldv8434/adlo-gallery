
def create_table_gallery(path)
	begin table string

	get list of files from "images" subfolder
	sort list of files

	for image in list of files
		if at start of line
			if NOT in first line
				end previous tr tag
			create new tr tag
		
		get path to image
		if not no_thumbs
			create thumbnail
		else 
			thumbnail_path = path
		
		start td + a tags line
		add img tag line w/ thumbnail 
		end a + td tags line
		
	if extra space in tr
		add extra empty td
	
	end tr and table tags

	return gallery string

def create_flexbox_gallery(path)
	begin flex container

	get list of files from "images" subfolder
	sort list of files

	for image in list of files
		
		get path to image
		if not no_thumbs
			create thumbnail
		else 
			thumbnail_path = path
		
		start td + a tags line
		add img tag line w/ thumbnail 
		end a + td tags line
		
	
	end flex container

	return gallery string

def create_thumbnail(path)
	extract filename from path
	create thumbnail path using "_thumbnails" + filename
		
	if (not regen_thumbnails and thumb exists):
		log "already exists, skipping"
		return

	if thumb exists
		print "already exists, removing"
		remove thumbnail file

	try:
		with open image
			switch thumbnail quality
				low
				med
				high
			convert to RGB
			save to thumb path as jpg
	except 
		log "error creating thumbnail"

def create_artist_page
	check if artist image exists
	read in artist bio/index.md
	read in template file
	convert template markdown to html
	add bio to template
	write template file

def create_sub_page
	find all subdirectories
	remove "images" and thumbnail folder from list
	create subpage list	
	for subpage
		create_subpage
		add subpage to subpage list

	read in template file
	convert template markdown to html
	
	if flexbox mode
		create flexbox gallery
	else
		create table gallery

	add items to template
	create template
		

def create_main_page
	make artist page
	
	find all subdirectories
	remove "images" and thumbnail folder from list
	create subpage list	
	for subpage
		create_subpage
		add subpage to subpage list

	read in template file
	convert template markdown to html
	
	if flexbox mode
		create flexbox gallery
	else
		create table gallery

	add items to template
	create template


def create_sample_folder_structure
	create tree of format
	├── artist
	│   ├── artist.jpg
	│   └── readme.md
	├── images
	│   └── sample.jpg
	├── readme.md
	├── subfolder1
	│   ├── images
	│   │   └── sample.jpg
	│   └── readme.md
	└── subfolder2
	    ├── images
	    │   └── sample.jpg
	    └── readme.md

def argparser_stuff
	setup argparse stuff
	argparse

def logging stuff
	create global logger
	set logger options
	if verbose
		logger setlevel debug
	else 
		logger setlevel error


def main()
	create global logger
	









