def grayScale(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
# USAGE #
'''
file = "C:\\somepicture.jpg"
pict = makePicture(file)
decreaseRedHalf(pict)
explore(pict)
'''