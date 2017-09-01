# Prob 4.3
file=makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
explore(file)

def moreBlue(file):
  for pix in getPixels(file):
    value=getBlue(pix)
    setRed(pix, value * 1.2)

def lessGreen(file):
  for pix in getPixels(file):
    value=getGreen(pix)
    setGreen(pix, value * 0.3)

moreBlue(file)
explore(file)
lessGreen(file)
explore(file)