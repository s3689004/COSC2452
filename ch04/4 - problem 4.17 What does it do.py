# 4.17 - What does it do?
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,20,20)
print pixelA

def test9 (picture):
  for p in getPixels(picture):
    red   = getRed(p)*2
    green = getGreen(p)*2
    blue  = getBlue(p)*2
    color = makeColor(red,green,blue)
    setColor(p,color)
    
test9(picture)
pixelB = getPixel(picture,20,20)
print pixelB
