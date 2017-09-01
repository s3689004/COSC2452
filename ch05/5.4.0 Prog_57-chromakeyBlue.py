# prog 57 - ChromakeyBlue - replace all BLUE with a new background
def chromakeyBlue(source, bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if(getRed(px) + getGreen(px) < getBlue(px)):
      bgpx  = getPixel(bg, x, y)
      bgcol = getColor(bgpx)
      setColor(px, bgcol)
# USAGE #
'''
source = makePicture(pickAFile())
bg = makePicture(pickAFile())
explore(source)
explore(bg)
chromakeyBlue(source, bg)
explore(source)
'''