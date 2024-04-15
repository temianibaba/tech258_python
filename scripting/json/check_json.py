import sys, os, json


if len(sys.argv) > 1: # If there's more than 1 argument
    if os.path.exists(sys.argv[1]): # is the filename real?
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is Valid!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("Usage: python check_kson.py <file>")