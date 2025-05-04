#!/usr/bin/env python3
import ast
import sys
import difflib

translation= {}  # dict to store translations after being read
gamenames = []
args = sys.argv[1:]

def is_integer(s): 
    try:
        int(s)
        return True
    except ValueError:
        return False 

def populate_gamenames():
    with open("gametranslate", "r") as f: #  read translations into dict variable
        global translation
        contents = f.read()
        translation = ast.literal_eval(contents)
    gamenames.extend(list(translation.values()))

def find_closest_match(game_title): #returns closest value in dict 
    matches = difflib.get_close_matches(game_title, gamenames, n=1, cutoff=0.0)
    return matches[0] if matches else None 

def return_appid(game_name): 
    key = next((k for k, v in translation.items() if v == game_name), None)
    return key

def main():
    populate_gamenames()
    #print(translation)
    args=sys.argv[1:]
    if len(sys.argv)-1 == 1 and is_integer(args[0]):
        inarg=args[0]
        appid= translation.get(inarg)
        if appid is not None:
            print(appid)
        else:
            print(f"{inarg} is not in the record")
    else:
        checkstr= ''.join(args)
        print(return_appid(find_closest_match(checkstr)))
if __name__ == "__main__":
    main()
