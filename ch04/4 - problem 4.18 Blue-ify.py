# 4.18 - Blue-ify a picture
# If any BLUE pixel has a value < 150, then make it 255
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
pixelA = getPixel(picture,40,40)
print pixelA

def measureBlue(picture):
  for p in getPixels(picture):
    getPixels(picture)
    blue = getRed(p)
  if blue < 150:
    setRed(p,0)

measureBlue(picture)
repaint(picture)
explore(picture)
pixelB = getPixel(picture,40,40)
print pixelB