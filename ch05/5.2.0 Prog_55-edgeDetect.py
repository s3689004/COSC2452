# prog 55 - Create line drawing using Clearer Edge Detection
def luminance(pixel):
  r = getRed(pixel)
  g = getGreen(pixel)
  b = getBlue(pixel)
  return (r+g+b)/3
  
def edgeDetect(source):
  for px in getPixels(source):
    x = getX(px)
    y = getY(px)
    if y < getHeight(source)-1 and x < getWidth(source)-1:
      botrt = getPixel(source, x+1, y+1)
      thislum = luminance(px)
      brlum = luminance(botrt)
      if abs(brlum-thislum) > 10:
        setColor(px, black)
      if abs(brlum-thislum) <= 10:
        setColor(px, white)