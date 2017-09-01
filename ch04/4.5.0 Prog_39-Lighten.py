def lighten(picture):
  for px in getPixels(picture):
    color = getColor(px)
    color = makeLighter(color)
    setColor(px, color)