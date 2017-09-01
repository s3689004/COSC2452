# 4.2 Manipulating pictures
def howCoords():
  file = pickAFile()
  print file
  myPict = makePicture(file)
  show(myPict)
  print(myPict)
  print("Pic width:", getWidth(myPict))
  print("Pic height: ", getHeight(myPict)
