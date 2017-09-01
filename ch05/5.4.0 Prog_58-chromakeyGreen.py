# prog 58 - chromakeyGreen - replace all GREEN with a new background
# USAGE #
'''
>>> alice = makePicture("Alice.jpg")
>>> jungle = makePicture("Jungle.jpg")
>>> chromakeyGreen(alice, jungle)
>>> explore(alice)
>>> alice = makePicture("Alice.png")
>>> chromakeyGreen(alice, jungle)
>>> explore(alice)
'''
def chromakeyGreen(source, bg):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if(getRed(px) + getBlue(px) < getGreen(px)):
      bgpx  = getPixel(bg, x, y)
      bgcol = getColor(bgpx)
      setColor(px, bgcol)