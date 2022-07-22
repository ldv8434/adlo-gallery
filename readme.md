# Adlo Gallery

Dead-simple web gallery creator. Turn a folder (or folder structure) of images into a simple gallery.

Generates a single web page with an HTML table or flexbox grid of thumbnail images. Clicking on an image will open the full version of the image.

Adlo Gallery aims to generate pages that load fast by converting images to thumbnails for use in the primary grid.

The gallery HTML file will be added to the target folder. Additionally, a `_thumbnails` folder will be created to contain all thumbmails.

## Features
- Adjustable table width size (in items)
- Adjustable CSS styling
- Thumbnail conversion for faster main-page loading times.
- No JS/PHP/etc. Only HTML.

## Usage
```
python adlo-gallery.py [flags] [input directory]
	-v : verbose/debug mode
	-f : use flexbox instead of HTML table
	-c <path> : css file to use. default: <adlo-gallery.py directory>/style.css
	-t <path> : jinja template file to use. <adlo-gallery.py directory>/template.html
	-o <directory> : output directory path.

	Sorting Options
	--sort-name : sort by name (default)
	--sort-mtime : sort by date created/modified

	Thumbnail Options
	--no-thumbnail : don't generate thumbnails and use the original images instead (not recommended)
	--thumbnail-size <size>: maximum height/width in px of a thumbnail image. default: 100
	--thumbnail-index-color : use indexed colours for thumbnails for possibly better loading speeds
	--thumbnail-grey : use greyscale colour mode for thumbnails for extremely large galleries
	--thumbnail-regenerate : re-generate thumbnails for all images.
```


## Features (dev map edition?)
- [ ] Generate from folder
- [ ] Thumbnail generation
- [ ] Symlinks images into new folder
- [ ] Generate from folder structure
- [ ] RSS/Atom feed generation
- [ ] Clearer settings from ini file
