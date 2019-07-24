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
ExitCond="n"
while(ExitCond !="y"):
    ImageDir = 0
    #purge ImageDir
    root = Tk()
    root.withdraw()
    root.update()
    ImageDir = fd.askopenfilename()
    root.destroy()
    #create and destroy ImageDir root selection file dialog
    print(ImageDir)
    ExitCond = input("is the image directory " + ImageDir + " correct (y/n)");
    #directory confirmation
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
        #exit catch incase someone cant see that it means the letters y/n
print (ImageDir)
#prints the image directory
#adds the Image directory to the ImageDir variable for later use
ExitCond="n"
while(ExitCond !="y"):
    OutputDir = 0
    #purge OutputDir
    root = Tk()
    root.withdraw()
    root.update()
    OutputDir = fd.askdirectory()
    root.destroy()
    #create and destroy OutputDir root selection file dialog
    print(ImageDir)
    ExitCond = input("is the output directory " + OutputDir + " correct (y/n)");
    #directory confirmation
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
        #exit catch just incase again
print (OutputDir)

DocName=input("Document name")
print (DocName)
#get user input for filename
DocNameFinal =DocName + "_" + str(time.time())+".html"
print(DocNameFinal)
#create final document name with timestamp
open(OutputDir+"/" + DocNameFinal,"w+")
#creates and opens the created final document (DocPrimary) for read/Write

ExitCond="n"
while(ExitCond !="y"):
    DocPrimary = 0
    #purge DocPrimary
    root = Tk()
    root.withdraw()
    root.update()
    DocPrimary = fd.askopenfilename()
    root.destroy()
    #create and destroy DocPrimary root selection file dialog
    print(DocPrimary)
    ExitCond = input("is the Primary directory " + DocPrimary + " correct (y/n)");
    #directory confirmation
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
        #exit catch just incase again
print (DocPrimary)

ExitCond="n"
while(ExitCond !="y"):
    DocSecondary = 0
    #purge DocSecondary
    root = Tk()
    root.withdraw()
    root.update()
    DocSecondary = fd.askopenfilename()
    root.destroy()
    #create and destroy DocSecondary root selection file dialog
    print(DocSecondary)
    ExitCond = input("is the Secondary directory " + DocSecondary + " correct (y/n)");
    #directory confirmation
    if ExitCond == "no":
        ExitCond = "n"
    if ExitCond == "yes":
        ExitCond = "y"
        #exit catch just incase again
print (DocSecondary)

F = open("DirVar.xml", "w+")
F.write(str(ImageDir))
F.close()
