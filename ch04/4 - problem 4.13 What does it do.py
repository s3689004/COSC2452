# 4.13 What does it do - Reduces RGB by 20
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA

def test5 (picture):
  for p in getPixels(picture):
    red   = getRed(p) - 20
    green = getGreen(p) - 20
    blue  = getBlue(p) - 20
    color = makeColor(red,green,blue)
    setColor(p,color)
    
test5(picture)
pixelB = getPixel(picture,0,0)
print pixelB