def changeRed(picture, amount):
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p, value * amount)
    
## Usage ##
'''
Apicture = makePicture(pickAFile())
amount = 0.7
changeRed(thePicture, amount)
show(thePicture)
'''