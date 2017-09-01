## prog 61 Gray Posterize to Two Levels with else
def grayPosterize(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p, black)
    else:
      setColor(p, white)
# USAGE #
'''
pic = makePicture(pickAFile())
grayPosterize(pic)
explore(pic)
'''