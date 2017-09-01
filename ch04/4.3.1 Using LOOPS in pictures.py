print('--- Change the RGB of a picture ---')
r = input('Enter a value for Red: ')
g = input('Enter a value for Green: ')
b = input('Enter a value for Blue: ')

picture=makePicture('C:\CRASHPLAN\TRAINING\RMIT\code\mediasources\caterpillar.jpg')
show(picture)

for pixel in getPixels(picture):
  newRvalue = getRed(pixel)
  newGvalue = getGreen(pixel)
  newBvalue = getBlue(pixel)
  setRed(pixel, newRvalue * r)
  setGreen(pixel, newGvalue * g)
  setBlue(pixel, newBvalue * b)
repaint(picture)
print(picture)