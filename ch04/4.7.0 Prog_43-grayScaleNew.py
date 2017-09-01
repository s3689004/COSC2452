def grayScaleNew(picture):
  for px in getPixels(picture):
    newRed = getRed(px) * 0.299
    newGreen = getGreen(px) * 0.587
    newBlue = getBlue(px) * 0.114
    # 0.299 + 0.587 + 0.114 = 1
    luminance = newRed+newGreen+newBlue
    setColor(px,makeColor(luminance,luminance,luminance))
# USAGE #
'''
file = "C:\\somepicture.jpg"
pict = makePicture(file)
decreaseRedHalf(pict)
explore(pict)
'''