def decreaseRed2(picture):
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p, value * 0.5)
    
## Usage ##
'''
thePicture = makePicture(pickAFile())
decreaseRed2(thePicture)
show(thePicture)
'''