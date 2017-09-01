# prob 4.6
# Swap the values of two colors of one pixel
picture = makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources/low-res.jpg')
pixelA = getPixel(picture,10,10,)
print pixelA
print''

redSwap = getRed(pixelA)
print('Orig RED: ', redSwap)

greenSwap = getGreen(pixelA)

print ('Orig GREEN: ', greenSwap)
print''
print('Swapping...')

newGreen = redSwap
newRed   = greenSwap

print''
print('New RED: ', newRed)
print('New GREEN: ', newGreen)

swapIt = makeColor(newRed,newGreen,getBlue(pixelA))

print''
print swapIt