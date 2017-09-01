# 4.2 Manipulating pictures
def drawALine():
  theFile='/home/jo/Documents/RMIT/code/mediasources/caterpillar.jpg'
  pict=makePicture(theFile)
  show(pict)
  print black
  thePixels = getPixels(pict)
  setColor(thePixels[0],black)
  setColor(thePixels[1],black)
  setColor(thePixels[2],black)
  setColor(thePixels[3],black)
  setColor(thePixels[4],black)
  setColor(thePixels[5],black)
  setColor(thePixels[6],black)
  setColor(thePixels[7],black)
  setColor(thePixels[8],black)
  setColor(thePixels[9],black)
  repaint(pict)
  writePictureTo(pict, '/home/jo/Documents/RMIT/code/mediasources/caterpillar_line.jpg')