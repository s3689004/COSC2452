# prog 50 - Remove Redeye
def removeRedEye(pic, startX, startY, endX, endY, endColor):
  for px in getPixels(pic):
    x = getX(px)
    y = getY(px)
    if (startX <= x <= endX) and (startY <= y <= endY):
      if (distance(red, getColor(px)) < 165):
        setColor(px, endColor)

'''
## USAGE ##
(1) Set the media path:
setMediaPath()
-or-
setMediaPath('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources')
(2) make the picture:
jenny=makePicture("jenny-red.jpg")
(3) Same as:
jenny = makePicture(getMediaPath("jenny-red.jpg"))
(4) Run it:
removeRedEye(jenny, 247, 76, 277, 96, black)
(5) view the results:
explore(jenny)

--or--

>>> makePicture(pickAFile())
Picture, filename C:\CRASHPLAN\TRAINING\RMIT\code\mediasources\jenny-red.jpg height 622 width 532
>>> jenny=makePicture(pickAFile())
>>> removeRedEye(jenny,20, 15, 50, 25, black)
>>> explore(jenny)
'''