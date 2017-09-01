pict = makePicture(pickAFile())

def decreaseRed(pict):
  for pixl in getPixels(pict):
    value = getRed(pixl)
    setRed(pixl, value * 3.5)
    repaint(pict)
    show(pict)

# or from CLI
'''
>>> for pixel in getPixels(pict):
...   setRed(pixel, getRed(pixel) * 0.5)
'''