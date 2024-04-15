import os

# Directory
directory = "test_dir"

# Parent directory
parent_directory = "C:/Users/temia/Desktop/Tech_258/github"

# Path
path = os.path.join(parent_directory, directory)

# Remove any previous tests
os.rmdir(path)

# Create dir
os.mkdir(path)
