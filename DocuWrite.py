import json
with open('settings.json') as json_file:
    data=json.load(json_file)
    print(data)
    print(data.get("ImageNum"))

ImageName=input("Image name without file extension ex: 117339_")
print(ImageName)
print(OutputDirFinal)
print(DocPrimary)
print(DocSecondary)

# append file2 data to file1 data
fin = open(DocPrimary, "r")
data2 = fin.read()
fin.close()
fout = open(OutputDirFinal, "a")
fout.write(data2)
fout.close()
fin = open(DocSecondary, "r")
data2 = fin.read()
fin.close()
fout = open(OutputDirFinal, "a")
fout.write(data2)
fout.close()

# Read in the file
with open(data.get('OutputDirFinal'), 'r') as file :
  filedata = file.read()

global QRB1
QRB1 =str(data.get('ImageDir')) + "/" + str(ImageName) + "_.jpg"
print(QRB1)

global QRB2
QRB2 =str(data.get('ImageDir')) + "/" + str(ImageName) + "_1.jpg"
print(QRB2)

global QRB3
QRB3 =str(data.get('ImageDir')) + "/" + str(ImageName) + "_2.jpg"
print(QRB3)

# Replace the target string
filedata = filedata.replace('ReplaceMe1', QRB1)
# Replace the target string
filedata = filedata.replace('ReplaceMe2', QRB2)
# Replace the target string
filedata = filedata.replace('ReplaceMe3', QRB3)

# Write the file out again
with open(data.get('OutputDirFinal'), 'w') as file:
    file.write(filedata)
global LoopFor
LoopFor=3
print(ImageNum)
LoopIter=int(ImageNum/3)
LoopIter=LoopIter-1
print(LoopIter)

  for x in range(LoopIter):
      fin = open(DocSecondary, "r")
      data2 = fin.read()
      fin.close()
      fout = open(OutputDirFinal, "a")
      fout.write(data2)
      fout.close()
      # Read in the file
      with open(data.get('OutputDirFinal'), 'r') as file :
        filedata = file.read()
      global QRB1
      QRB1 =str(data.get('ImageDir')) + "/" + str(ImageName) +"_" + str(LoopFor) + ".jpg"
      print(QRB1)
      LoopFor= LoopFor +1
      print(LoopFor)
      global QRB2
      QRB2 =str(data.get('ImageDir')) + "/" + str(ImageName) +"_" + str(LoopFor) + ".jpg"
      print(QRB2)
      LoopFor= LoopFor +1
      print(LoopFor)
      global QRB3
      QRB3 =str(data.get('ImageDir')) + "/" + str(ImageName) +"_" + str(LoopFor) + ".jpg"
      LoopFor= LoopFor +1
      print(QRB3)

      # Replace the target string
      filedata = filedata.replace('ReplaceMe1', QRB1)
      # Replace the target string
      filedata = filedata.replace('ReplaceMe2', QRB2)
      # Replace the target string
      filedata = filedata.replace('ReplaceMe3', QRB3)

      # Write the file out again
      with open(data.get('OutputDirFinal'), 'w') as file:
          file.write(filedata)
