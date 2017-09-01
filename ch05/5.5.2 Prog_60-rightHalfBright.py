# prog 60 lighten the right half of the picture
def rightHalfBright(pic):
  halfway = getWidth(pic) / 2
  for px in getPixels(pic):
    x = getX(px)
    if x > halfway:
      color = getColor(px)
      setColor(px, makeLighter(color))
# USAGE #
'''
>>> pic = makePicture(pickAFile())
>>> rightHalfBright(pic)
>>> explore(pic)
-or-
>>> setMediaPath('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources')
>>> getMediaPath()
'C:\\CRASHPLAN\\TRAINING\\RMIT\\code\\mediasources\\'
'''