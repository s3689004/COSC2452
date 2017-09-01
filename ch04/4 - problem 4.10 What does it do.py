# 4.10 what does it do?
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
pixelA = getPixel(picture,10,10)
print pixelA

def test2 (picture):
  for p in getPixels(picture):
    setBlue(p,getBlue(p) * 1)
    
newBlue = getBlue(pixelA)
print('new Blue: ', newBlue)
explore(picture)