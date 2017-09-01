# 4.16 What will it do? Will it be darker or lighter thatn 4.15 - test7?
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA

def test8(picture):
  for p in getPixels(picture):
    red   = getRed(p)/3
    green = getGreen(p)/3
    blue  = getBlue(p)/3
    color = makeColor(red,green,blue)
    setColor(p,color)