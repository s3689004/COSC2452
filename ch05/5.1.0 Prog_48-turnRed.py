# prog 48
def turnRed():
  file='C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg'
  picture=makePicture(file)
  for px in getPixels(picture):
    brown = makeColor(42,25,15)
    color = getColor(px)
    if distance(color, brown)<50.0:
      r=getRed(px)*2
      g=getGreen(px)
      b=getBlue(px)
      setColor(px,makeColor(r,g,b))
    show(picture)
    return picture
#explore(picture)