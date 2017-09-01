# prog 49
def turnRedInRange():
  brown = makeColor(42,25,15)
  file='C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg'
  picture=makePicture(file)
  for px in getPixels(picture):
    x = getX(px)
    y = getY(px)
    if 63 <= x <=125:
      if 6 <= y <= 76:
        color=getColor(px)
        if distance(color,brown)>50.0:
          r=getRed(px)*2
          g=getGreen(px)
          b=getBlue(px)
          setColor(px,makeColor(r,g,b))
    show(picture)
    return picture