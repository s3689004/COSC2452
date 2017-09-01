# prob 4.7
# Set Red,Green,Blue color values of a pixel in picture
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA
redVal = getRed(pixelA)
greenVal = getGreen(pixelA)
blueVal = getBlue(pixelA)
print''
setRed(pixelA,10)
setGreen(pixelA,20)
setBlue(pixelA,30)
pixelB = getPixel(picture,0,0)
print 'New values:'
print pixelB
explore(picture)