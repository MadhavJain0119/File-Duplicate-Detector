from tkinter import Tk
from tkinter.filedialog import askdirectory

import os

import hashlib

#get the dialog box
Tk().withdraw()
path = askdirectory(title="Select the folder")
#print(path)

#to get the list of all the files in the folders

#gives generator object
walker = os.walk(path)
print(walker)

#iterate through the generator object
# for walk in walker:
#     print(walk)

uniquefiles = dict()
for folder, sub_folder, files in walker:
    for file in files:
        filepath = os.path.join(folder, file)
        #print(filepath)

        #to open each file and convert to hash string
        filehash = hashlib.md5(open(filepath, "rb").read()).hexdigest()
        #print(filehash)

        #to detect duplicate files
        if filehash in uniquefiles:
            print(f" {file} is a duplicate file")

        else:
            uniquefiles[filehash] = file
