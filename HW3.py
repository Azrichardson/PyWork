import os
import random
import time
import fileinput
global XB
global HtMl
global html
global FO
global B9
XB=1
B9=9
FO= "myfile" + str(time.time())+".html"
f = open(FO, "x")

with open(r"C:\Users\6871347\Desktop\TEST\TEST.html", "r+") as f2:
    for x in range(0):
        f2.readline()   # skip past early lines
    pos = f2.tell() # remember insertion position
    f2_remainder = f2.read()    # cache the rest of f2
    f2.seek(pos)
    with open(r"C:\Users\6871347\Desktop\TEST\firstLine.html", "r+") as f1:
        f2.write(f1.read())
    f2.write(f2_remainder)
    
DIR=r'C:\Users\6871347\Desktop\BATCH'
onlyfiles = next(os.walk(DIR))[2] #dir is your directory path as string
XN=(len(onlyfiles))
print (XN)

for x in range (0,XN):
    print (XB)


# insert contents of "/test1.txt" into "/test2.txt" at line 20
    with open(r"C:\Users\6871347\Desktop\TEST\L1.html", "r+") as f2:
        for x in range(B9):
            f2.readline()   # skip past early lines
        pos = f2.tell() # remember insertion position
        f2_remainder = f2.read()    # cache the rest of f2
        f2.seek(pos)
        with open(r"C:\Users\6871347\Desktop\TEST\HTMLinsert.html", "r+") as f1:
            f2.write(f1.read())
        f2.write(f2_remainder)

    
    
    # Read in the file
    with open(r'C:\Users\6871347\Desktop\TEST\L1.html', 'r') as file :
      filedata = file.read()

    # Replace the target string
    filedata = filedata.replace(r'src="C:\Users\6871347\Desktop\117339RO\117339.jpg"', r'src="C:\Users\6871347\Desktop\117339RO\117339' + "_" + str(XB) + ".jpg" + '"')
    print ("writing file")
    XB+=1
    # Write the file out again
    with open(r'C:\Users\6871347\Desktop\TEST\L1.html', 'w') as file:
      file.write(filedata)

    B9 +=9



with open(r"C:\Users\6871347\Desktop\TEST\TEST.html", "r+") as f2:
    for x in range(35):
        f2.readline()   # skip past early lines
    pos = f2.tell() # remember insertion position
    f2_remainder = f2.read()    # cache the rest of f2
    f2.seek(pos)
    with open(r"C:\Users\6871347\Desktop\TEST\L1.html", "r+") as f1:
        f2.write(f1.read())
    f2.write(f2_remainder)

with open(r"C:\Users\6871347\Desktop\PYSCRIPTS" + '/' + str(FO), "r+") as f2:
    for x in range(35):
        f2.readline()   # skip past early lines
    pos = f2.tell() # remember insertion position
    f2_remainder = f2.read()    # cache the rest of f2
    f2.seek(pos)
    with open(r"C:\Users\6871347\Desktop\TEST\TEST.html", "r+") as f1:
        f2.write(f1.read())
    f2.write(f2_remainder)
