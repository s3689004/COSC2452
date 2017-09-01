# prob 4.8
# Set Red,Green,Blue color values to 255
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,0,0)
print pixelA
redVal = getRed(pixelA)
greenVal = getGreen(pixelA)
blueVal = getBlue(pixelA)
print''
setRed(pixelA,255)
setGreen(pixelA,255)
setBlue(pixelA,255)
pixelB = getPixel(picture,0,0)
print 'New values:'
print pixelB
explore(picture)