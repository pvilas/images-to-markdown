# images-to-markdown

This tool takes a list of images and create a markdown or html page with the file names.

I like watching martial arts, pilates or other educational videos. I document the techiques by taking snapshots from the videos and saving them with a description of what is happening in the action.

This little program takes the images of a directiory and creates a markdown or html file with the contents.

The idea would be something like this:

![images-to-markdown idea](https://docs.google.com/drawings/d/e/2PACX-1vSA00vs0JeDQn01tRRne0Z9ROCkGHZS1gwIGr-mbsU8Z28gPqaZb6oWd1V520aw1nYXnY4L7qQMcd5I/pub?w=960&amp;h=720)

The `i2m.py` options are:
```
usage: i2m.py [-h] [-d DIRECTORY] [-t TEMPLATE] [-o OUTPUT]
              [-u IMAGE_BASE_URL] [-g TAGS] [-s SOURCE]

Creates a document from a list of images

optional arguments:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Directory where the images are stored
  -t TEMPLATE, --template TEMPLATE
                        Name of the template used to create the page (default
                        markdown.md)
  -o OUTPUT, --output OUTPUT
                        File name of the output page. Use file name git to use
                        github pages style.
  -u IMAGE_BASE_URL, --image_base_url IMAGE_BASE_URL
                        Base url for the image files. Default images
  -g TAGS, --tags TAGS  Comma separated list of tags
  -s SOURCE, --source SOURCE
                        Source of the video
```

and an example

```
python i2m.py -d "/Users/pvilas/Desktop/armbar from mount/" -u "/images/jujutsu/2019-09-15-armbar/" -o git -g
 "jujutsu, armbar" -s "[Draculino: Arm Bar from Mount Position](https://www.youtube.com/watch?v=5uuU0LfsZOY)"
```

Generates [this](http://pvilas.com/2019/09/Armbar-from-mount.html) page.