# 4.2 Manipulating pictures
def pixelSet():
  file = pickAFile()
  myPict = makePicture(file)
  show(myPict)
  pixel = getPixel(myPict, 400, 200)
  print pixel
  print getRed(pixel)
  setRed(pixel, 128)
  print getRed(pixel)