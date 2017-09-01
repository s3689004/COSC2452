# prog 51 Convert image to Sepia Tones

## USAGE ##
'''
>>> setMediaPath('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources')
>>> picture = makePicture(getMediaPath("low-res.jpg"))
>>> explore(picture)
>>> grayScaleNew(picture)
>>> sepiaTint(picture)
>>> explore(picture)
'''

def grayScaleNew(picture):
  for p in getPixels(picture):
    newRed= getRed(p)*.299
    newGreen= getGreen(p)*.587
    newBlue= getBlue(p)*.114
    luminance= newRed+newGreen+newBlue
    setColor(p, makeColor(luminance, luminance, luminance)) 
    
def sepiaTint(picture):
  # Convert img to GreyScale
  grayScaleNew(picture)  #  Had to add this function first ^^
  
  # loop through the img to tint pixels
  for p in getPixels(picture):
    red  = getRed(p)
    blue = getBlue(p)
  
  # tint shadows
  if (red < 63):
    red  = red * 1.1
    blue = blue * 0.9
    
  # tint midtones
  if (red > 62 and red < 192):
    red  = red * 1.15
    blue = blue * 0.85
  
  # tint highlights
  if (red > 191):
    red = red * 1.08
    if (red > 255):
      red = 255
    blue = blue * 0.93
  
  # set the new color values
  setBlue(p, blue)
  setRed(p, red)
