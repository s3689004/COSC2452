def makeSunset2(picture):
  reduceBlue(picture)
  reduceGreen(picture)
  value=0
  
def reduceBlue(picture):
  for p in getPixels(picture):
    value=getBlue(p)
    setBlue(p,value * 0.7)
    
def reduceGreen(picture):
  for p in getPixels(picture):
    value=getGreen(p)
    setGreen(p,value * 0.7)