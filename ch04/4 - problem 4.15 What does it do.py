# 4.15 What does it do - reduces RGB values by 50%
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA

def test7 (picture):
  for p in getPixels(picture):
    red   = getRed(p)/2
    green = getGreen(p)/2
    blue  = getBlue(p)/2
    color = makeColor(red,green,blue)
    setColor(p,color)
    
test7(picture)
pixelB = getPixel(picture,0,0)
print pixelB