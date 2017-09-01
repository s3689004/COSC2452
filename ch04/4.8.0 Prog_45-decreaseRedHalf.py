def decreaseRedHalf(picture):
  pixels = getPixels(picture)
  for index in range(0,len(pixels)/2):
    pixel = pixels[index]
    value = getRed(pixel)
    setRed(pixel,value * 0.5)
# USAGE #
'''
file = "C:\\somepicture.jpg"
pict = makePicture(file)
decreaseRedHalf(pict)
explore(pict)
'''