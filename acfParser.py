#!/usr/bin/env python3
from pathlib import Path
from gameids import * 

acf_dirs=["/home/saph/.steam/debian-installation/steamapps/" , 
                "/media/saph/Storage/SteamLibrary/steamapps/"]

acf_file_list = []
translation_directory = {}


"""
1. make a list of only the files ending in .acf in these two Directories
"""
for folder in acf_dirs:     # Operate on strings of of acf_dirs
    d_path = Path(folder)   # make path object of current directory
    files = [f for f in d_path.iterdir() if f.is_file() and f.name.endswith('.acf')] # make Path object list of acf files
    acf_file_list.extend(files) #place files in list in global collection

"""
2. make sure that the entries in the list are full filepaths)
"""
for file in acf_file_list:                          # get appid and name from file in list
    result = acf_parser(file)                       # returns (appid,name) if ran sucessfully, ortherwise returns -1
    if result == -1: 
        continue                                    # continues parent loop, ceases current iteration
    translation_directory[result[0]] = result[1]    # place appid and name in directory

"""
3. pass each file path into a acf_handler function:
"""
#for key, value in translation_directory.items():    #print contents of collection
with open('gametranslate', 'w') as out:
    out.write(str(translation_directory))
