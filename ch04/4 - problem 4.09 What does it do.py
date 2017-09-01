# 4.8 Lower red value to 30%
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA

def test1 (picture):
  for p in getPixels(picture):
    setRed(p,getRed(p) * 0.3)