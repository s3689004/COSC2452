# prog 54 - create line drawing using edge detection
def edge(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      sum      = getRed(px)+getGreen(px)+getBlue(px)
      botrt    = getPixel(source, x+1, y+1)
      sum2     = getRed(botrt)+getGreen(botrt)+getBlue(botrt)
      diff     = abs(sum2-sum)
      newcolor = makeColor(diff, diff, diff)
      setColor(px, newcolor)