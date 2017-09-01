def darken(picture):
  for px in getPixels(picture):
    color = getColor(px)
    color = makeDarker(color)
    setColor(px, color)
    