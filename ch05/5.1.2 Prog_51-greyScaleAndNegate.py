def greyScaleAndNegate(pic):  
  for px in getPixels(pic):
    level = 255 - int(0.21*getRed(px) + 0.71*getGreen(px) +0.07*getBlue(px))
    color = makeColor(level, level, level)
    setColor(px, color)

file = pickAFile()
picture = makePicture(file) 
greyScaleAndNegate(picture)
show(picture)