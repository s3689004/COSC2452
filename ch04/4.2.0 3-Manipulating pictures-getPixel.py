# 4.2 Manipulating pictures
def pixelGet():
  file = pickAFile()
  myPict = makePicture(file)
  show(myPict)
  pixel = getPixel(myPict, 100, 50)
  print pixel
  pixels = getPixels(myPict)
#  print pixels[0] # <-- will crash
  print("X is at: ", getX(pixel))
  print("Y is at: ", getY(pixel))
