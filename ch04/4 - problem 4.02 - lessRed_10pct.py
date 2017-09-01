# Problem 4.2 - 10 %
def lessRed(picture):
  for pix in getPixels(picture):
    value=getRed(pix)
    setRed(pix,value * 0.1)

''' ---USAGE---
file='C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg'  # note the \ and /
picture=makePicture(file)
explore(picture)
lessRed(picture)
explore(picture)
'''