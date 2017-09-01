# prog 56 - Subtract the background and replace with a new one
# USAGE #
'''
>>> setMediaPath('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources')
>>> person = makePicture(getMediaPath("person.jpg"))
>>> bg = makePicture("bgFrame.jpg")
>>> moon = makePicture("moon-surface.jpg")
>>> swapBack(person, bg, moon)
>>> explore(person)
'''

def swapBack(pict, bg, newBg):
  for px in getPixels(pict):
    x = getX(px)
    y = getY(px)
    bgPx = getPixel(bg, x, y)
    pxcol = getColor(px)
    bgcol = getColor(bgPx)
    if (distance(pxcol, bgcol) < 15.0):
      newcol = getColor(getPixel(newBg, x, y))
      setColor(px, newcol)