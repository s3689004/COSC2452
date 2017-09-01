# 4.14 What does it do - sets RED = 0
#picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
#print 'Original values:'
pixelA = getPixel(picture,10,10)
print pixelA

def reduceRed():
  picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
  show(picture)
  for p in getPixels(picture):
    val = getRed(p)
    setRed(p,0)
  repaint(picture)

reduceRed()
pixelB = getPixel(picture,10,10)
print pixelB
