import os
import fileinput
global XB
XB=1

r"C:\Users\6871347\Desktop\TEST\TEST.html"

DIR=r'C:\Users\6871347\Desktop\BATCH'
onlyfiles = next(os.walk(DIR))[2] #dir is your directory path as string
XN=(len(onlyfiles))
print (XN)

for x in range (0,XN):
    print (XB)
    XB+=1

# insert contents of "/test1.txt" into "/test2.txt" at line 20
with open(r"C:\Users\6871347\Desktop\TEST\TEST.html", "r+") as f2:
    for x in range(31):
        f2.readline()   # skip past early lines
    pos = f2.tell() # remember insertion position
    f2_remainder = f2.read()    # cache the rest of f2
    f2.seek(pos)
    with open(r"C:\Users\6871347\Desktop\TEST\L1.html", "r+") as f1:
        f2.write(f1.read())
    f2.write(f2_remainder)

with open(r"C:\Users\6871347\Desktop\TEST\TEST.html") as myfile:
     if r"C:\Users\6871347\Desktop\117339RO\117339_" in myfile.read():
         print('Blahblah')
