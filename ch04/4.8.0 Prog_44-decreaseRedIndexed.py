def decreaseRedIndexed(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)):
    pixel = pixels[index]
    value = getRed(pixel)
    setRed(pixel,value * 0.5)
# USAGE #
'''
file = 'path/to/image/file'
pict = makePicture(file)
decreaseRedIndexed(file)
explore(pict)
'''