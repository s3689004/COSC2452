# prob 4.4 (from p118)
picture=makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
explore(picture)

def increaseRed2(picture):
  for p in getPixels(picture):
    setRed(p, getRed(p)*1.2)
    
def increaseRed3(picture):
  for p in getPixels(picture):
    redC     = getRed(p)
    greenC   = getGreen(p)
    blueC    = getBlue(p)
    newRed   = int(redC*1.2)
    newColor = makeColor(newRed,greenC,BlueC)
    setColor(p,newColor)
    
explore(picture)