import os

target_dir="/Users/pvilas/Desktop/armbar from mount"

# name of the actual directory
dir_name=str.split(target_dir, '/')[-1]
print(dir_name)


# take the files
files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(target_dir):
    for file_name in f:
        print(file_name)
        if ('.jgp', '.png', '.gif') in file_name:
            files.append(os.path.join(r, file_name))

print("File names:")
for f in files:
    print(f)