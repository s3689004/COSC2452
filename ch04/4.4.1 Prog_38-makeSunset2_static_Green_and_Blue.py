def reduceBlueNotReusable():
  picture = makePicture(pickAFile())
  show(picture)
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value * 0.5)
  repaint(picture)
  
def reduceGreenNotReusable():
  picture = False
  picture = makePicture(pickAFile())
  show(picture)
  for p in getPixels(picture):
    value=getGreen(p)
    setGreen(p,value * 0.7)
  repaint(picture)
  show(Picture)