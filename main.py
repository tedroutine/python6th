import os

current_directory = os.getcwd()
print(current_directory)

# os.mkdir('new_directory')
# os.makedirs('parent_directory/child_directory/grandchild_directory')

# os.rmdir('new_directory')

# os.removedirs('parent_directory/child_directory/grandchild_directory')

for dirpath, dirnames, filenames in os.walk('.'):
    print(f"directory paths : {dirpath}")
    print(f"directory dir_name : {dirnames}")
    print(f"directory file_name : {filenames}")