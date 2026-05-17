import os

# Path of the directory
path = "/"

# Get the contents of the directory
contents = os.listdir(path)

# Print each file/folder name
for item in contents:
    print(item)