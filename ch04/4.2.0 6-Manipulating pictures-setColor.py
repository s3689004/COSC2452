# 4.2 Manipulating pictures
def colorSet():
  file = pickAFile()
  myPict = makePicture(file)
  show(myPict)
  pixel = getPixel(myPict, 400, 200)
  color = getColor(pixel)
  print color
  newColor = makeColor(0, 100, 0)
  print newColor
  setColor(pixel, newColor)
#  print getColor(pixel)
  print getPixel(myPict, 400, 200)
  repaint(myPict)
  writePictureTo(myPict, '/home/jo/Documents/RMIT/code/mediasources/rgb.png')