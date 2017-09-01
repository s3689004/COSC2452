# prog 62 - Grey Posterize to Three leveld with elif
def posterizeBWR(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p, black)
    elif luminance > 120:
      setColor(p, white)
    else:
      setColor(p, red)
# USAGE #
'''
pic = makePicture(pickAFile())
posterizeBWR(pic)
explore(pic)
'''