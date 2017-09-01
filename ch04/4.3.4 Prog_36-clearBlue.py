picture = makePicture(pickAFile())
def clearBlue(picture):
  for p in getPixels(picture):
    setBlue(p,0)
repaint(picture)
show(picture)