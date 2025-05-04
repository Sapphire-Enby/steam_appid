#!/usr/bin/env python3
from pathlib import Path
import re
soredPairings= {}
# Directores that have the acf files
# acfDirectories=["/home/saph/.steam/debian-installation/steamapps/" , 
#                "/media/saph/Storage/SteamLibrary/steamapps/"]

def line_handler(line=test_line):  # provides app id or name from a line
    """
    expects to be fed a line that has either "appid" or "name"
    will check that two strings within quotes exist in line
    and then will return the second quoted value
    otherwise will raise an exception
    """ 
    matches = re.findall(r'"(.*?)"', line) # match " then group ( any symbol . of 1 or more amount * 
    if len(matches) >= 2:  # check proper number oof matches
        second_value = matches[1]  # value is second match
        if DEBUG: print(second_value)
        return second_value  # return it 

    else: raise Exception(f"incorrect number of matches {matches} 2 expected")



def acf_parser(acfPath="/home/saph/WORKING/example.acf"):  # checks if file has desired lines
    """
    checks if a file has a line with "name" and also a line with "appid"
    upon being found, will pass line into line_handler, to parse and return relevant value
    if both matching lines are not found it will return -1, 
    ortherwise the desired values
    """
    with acfPath.open('r') as file:
        cond1 = False # app id found
        cond2 = False # name found
        appid: int    # placeholder
        name: str     # placeholder
        
        for line in file: 
            
            if '"appid"' in line:  
                cond1 = True
                appid = line_handler(line)# send to handler and store to register
            
            if '"name"' in line:
                cond2 = True
                name = line_handler(line)
        
        if DEBUG: print(f"test results {cond1} and {cond2}")

        if not (cond1 and cond2):  # FAIL condition 
            return -1
        
        else: return (appid,name)  # PASS condition

def store_pairing(inTuple):
    if inTuple == -1:
        raise Exception("invalid argument passed for storing")
    else: store_pairing[inTuple[0]] = inTuple[1]

def main():
    if DEBUG:
        output = acf_parser()
        print(output)

if __name__ == "__main__":
    main()

