# 4.12 What does it do - Adds 10 to each RGB
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,20,20)
print pixelA

def test4 (picture):
  for p in getPixels(picture):
    red = getRed(p) + 10
    green = getGreen(p) + 10
    blue = getBlue(p) + 10
    color = makeColor(red, green, blue)
    setColor(p, color)

test4(picture)
pixelB = getPixel(picture,20,20)
print pixelB