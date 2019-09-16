import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
import argparse
from datetime import date


# example 
# python i2m.py -d "/Users/pvilas/Desktop/armbar from mount/" -u "/images/jujutsu/2019-09-15-armbar/" -o git -g
# "jujutsu, armbar" -s "[Draculino: Arm Bar from Mount Position](https://www.youtube.com/watch?v=5uuU0LfsZOY)"

# initialize template env
env = Environment(
    loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
    autoescape=select_autoescape(['html', 'xml'])
)

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser(description="Creates a document from a list of images")

ap.add_argument("-d", "--directory", required=False, default='./',
                help="Directory where the images are stored")

ap.add_argument("-t", "--template", required=False, default='markdown.md',
                help="Name of the template used to create the page (default markdown.md)")

ap.add_argument("-o", "--output", required=False, 
                help="File name of the output page. Use file name git to use github pages style.")

ap.add_argument("-u", "--image_base_url", required=False, default='images',
                help="Base url for the image files. Default images")

ap.add_argument("-g", "--tags", required=False, default='',
                help="Comma separated list of tags")

ap.add_argument("-s", "--source", required=False, default='',
                help="Source of the video")



args = ap.parse_args()

if not args.directory:
            print('Need an image directory')
            ap.print_help()
            exit(1)


target_dir=args.directory #"/Users/pvilas/Desktop/armbar from mount"

def prepare_image_title(tit):
    # return the description of the image based on the file name
    # remove extension
    base=os.path.splitext(tit)[0]
    return base

title=''
try:
    # make the page title
    title=target_dir.rstrip('/').split('/')[-1].capitalize()
    print(f"Title: {title}")
except Exception as ex:
    print(f"Error making title: {ex}")
    exit(-1)

# default file output is the format of github pages ISO_DATE+title-with-dash+'.md'
git_file_name=''
if args.output=='git':
    try:
        git_file_name=f"{date.today().isoformat()}-{title.replace(' ', '-')}.{args.template.split('.')[-1]}"
    except Exception as ex:
        print(f"Error creating default output file name: {ex}")
        exit(-1)


# take the files
files = []
image_prefix=f"{date.today().isoformat()}-{title.replace(' ', '-')}"
try:
    # r=root, d=directories, f = files
    for r, d, f in os.walk(target_dir):        
        for old_file_name in f:            
            # take name without underscores
            name_wout, exten = os.path.splitext(old_file_name)
            if exten in ('.jpg', '.png', '.gif'):                        
                # replace spaces by underscores
                new_file_name=name_wout.replace(' ', '_')
                # if file name doesnt start with image_prefix, add it
                #if not new_file_name.startswith(image_prefix):
                #    new_file_name=image_prefix+new_file_name

                # rename file            
                os.rename(  os.path.join(target_dir, old_file_name),
                            os.path.join(target_dir, new_file_name+exten))

                # full_name=os.path.join(target_dir, new_file_name)                
                # imgtitle, file_extension = os.path.splitext(full_name)                
                files.append( 
                    (
                        args.image_base_url.rstrip('/')+'/'+new_file_name.lstrip('/')+exten,  # file
                        new_file_name.replace('_', ' ') # file desc
                    )
                )

except Exception as ex:
    print(f"Error reading directory {target_dir}: {ex}")
    exit(-2)

files.sort()
print(f"Total number of files: {len(files)}")

try:
    template = env.get_template(args.template)
except Exception as ex:
    print(f"Error getting the template: {ex}")
    exit(-1)

try:
    # process the template with data
    result=template.render(
        files=files,
        title=title,
        source=args.source,
        tags=args.tags
    )
except Exception as ex:
    print(f"Error processing the template: {ex}")
    exit(-1)

# handle output
if not args.output:
    print(result)
else:
    if args.output=='git':
        out_fn=git_file_name
    else:
        out_fn=args.output
    try:
        f = open(out_fn, "w")
        f.write(result)
        f.close()    
    except Exception as ex:
        print(f"Error creating output file: {ex}")
        exit(-1)
