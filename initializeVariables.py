    #import dependent modules
import os, time, random, fileinput, tkinter, os.path
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
import base.py
