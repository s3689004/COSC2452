def makeSunset2NotReusable():
  picture=makePicture(pickAFile())
  getPixel(picture,1,1)
  reduceBlue(picture)
  reduceGreen(picture)
  repaint(picture)