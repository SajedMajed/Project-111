import os
import shutil

from_dir="c:/Users/Downloads"
to_dir="c:/Users/Documents/Document_Files"

list_of_files=os.listdir(from_dir)
print(list_of_files)

for file_name in list_of_files:
    name,extension=os.path.splitext(file_name)