# prog 53
def grayPosterize(pic):
  for p in getPixels(pic):
    r = getRed(p)
    g = getGreen(p)
    b = getBlue(p)
    luminance = (r+g+b)/3
    if luminance < 64:
      setColor(p, black)
    if luminance >= 64:
      setColor(p,white)