# prog 51 create 'grayScaleNew' function:

def grayScaleNew(picture):
  for p in getPixels(picture):
    newRed= getRed(p)*.299
    newGreen= getGreen(p)*.587
    newBlue= getBlue(p)*.114
    luminance= newRed+newGreen+newBlue
    setColor(p, makeColor(luminance, luminance, luminance)) 