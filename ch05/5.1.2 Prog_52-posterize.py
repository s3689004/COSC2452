# prog 52
'''
student = makePicture('low-res.jpg')
explore(student)
posterize(student)
explore(student)
'''
def posterize(picture):

  # loop through the pixels
  for p in getPixels(picture):
    # get RGB values
    red   = getRed(p)
    blue  = getBlue(p)
    green = getGreen(p)
    
  # check and set RED values
  if(red < 64):
    setRed(p, 31)
  if(red > 63 and red < 128):
    setRed(p, 95)
  if(red > 127 and red < 192):
    setRed(p, 159)
  if(red > 191 and red < 256):
    setRed(p, 223)
    
  # check and set GREEN values
  if(green < 64):
    setGreen(p, 31)
  if(green > 63 and green < 128):
    setGreen(p, 95)
  if(green > 127 and green < 192):
    setGreen(p, 159)
  if(green > 191 and green < 256):
    setGreen(p, 223)
    
  # check and set BLUE values
  if(blue < 64):
    setBlue(p, 31)
  if(blue > 63 and blue < 128):
    setBlue(p, 95)
  if(blue > 127 and blue < 192):
    setBlue(p, 159)
  if(blue > 191 and blue < 256):
    setBlue(p, 223)