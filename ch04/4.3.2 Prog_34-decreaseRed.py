def decreaseRed(picture):
  for p in getPixels(picture):
    value = getRed(p)
    setRed(p, value * 0.5)
## Usage ##
# file='/path/to/picture.jpg'
# picture=makePicture(file)
# show(picture)
# decreaseRed(picture)
# repaint(picture)