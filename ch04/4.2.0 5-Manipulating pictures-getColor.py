# 4.2 Manipulating pictures
def colorGet():
  file = pickAFile()
  myPict = makePicture(file)
  show(myPict)
  pixel = getPixel(myPict, 400, 200)
  color = getColor(pixel)
  print color