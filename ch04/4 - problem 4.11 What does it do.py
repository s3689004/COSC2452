# 4.11 What does it do?
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
print 'Original values:'
pixelA = getPixel(picture,10,10)
print pixelA

for pixelA in getPixels(picture):
  oldBlue=getBlue(pixelA)
  setBlue(pixelA, oldBlue * 1.6)
  
newBlue = getBlue(pixelA)
print newBlue
print pixelA