# prog 59 Adding a border
def greekBorder(pic):
  bottom = getHeight(pic)-10    # Have to define the bottom of the pic, since we don't know the total height of the pic beforehand
  for px in getPixels(pic):
    y = getY(px)
    if y < 10:      # all pixels from row 10 and up
      setColor(px, blue)
    if y > bottom:  # all pixels in the bottom 10 rows
      setColor(px,white)
# USAGE #
'''
>>> pic = makePicture(pickAFile())
>>> greekBorder(pic)
>>> explore(pic)
'''