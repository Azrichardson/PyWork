    #import dependent modules
import os, time, random, fileinput, tkinter
    #intialize variable set 0.\
from tkinter import filedialog as fd
from tkinter import Tk
#set filedialog from tk library to fd
global ImageNum, ExitCond
    #image number ex:117339, 117339_1.\
global DocPrimary, DocSecondary, DocTertiary
    #the 3 different documents generated and used. DocPrimary is everything inserted, DocSecondary is base html.\
    # DocTertiary is html inserted and modifed by python into DocSecondary.\
global DocTimeStamp
    #timestamp taken at time of document generation in miliseconds
global DocName, ImageDir, OutputDir, DocNameFinal
    #NamePrompt (prompt for custom document name on output)\
    #ImageDir (prompt for directory to all the images to be used)\
    #OutputDir (Directory that the final document will be output to)\
DocName=input("Document name")
print (DocName)
#get user input for filename
DocNameFinal =DocName + "_" + str(time.time())+".html"
print(DocNameFinal)
#create final document name with timestamp
open(DocNameFinal,"w+")
#creates and opens the created final document (DocPrimary) for read/Write
DocNameFinal.close()
#close DocNameFinal so the script doesnt freak
ExitCond="n"
while(ExitCond !="y"):
    ImageDir = 0
    root = Tk()
    root.withdraw()
    root.update()
    ImageDir = fd.askopenfilename()
    root.destroy()
    print(ImageDir)
    ExitCond = input("is the image directory " + ImageDir + " correct (y/n)");
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
print (ImageDir)
ExitCond="n"
while(ExitCond !="y"):
    OutputDir = 0
    root = Tk()
    root.withdraw()
    root.update()
    OutputDir = fd.askopenfilename()
    root.destroy()
    print(ImageDir)
    ExitCond = input("is the output directory " + OutputDir + " correct (y/n)");
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
print (OutputDir)
