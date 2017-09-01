print('')
print('--- To test whether RED has changed ---')
print('( For this script to work, you need to run "4.3.2  Prog_34-lessRed.py" first )')
print('')
pixel = getPixel(picture,0,0)
print pixel
lessRed(picture)
newPixel = getPixel(picture,0,0)
print newPixel
print('')
print('Check if the Red value has changed')
print('')

### From CLI ###
''' --- TO TEST ---
>>> pixel = getPixel(picture,0,0)
>>> print pixel
Pixel red=128 green=255 blue=255
>>> lessRed(picture)
[The program was stopped by the stop button.]
>>> 
>>> newPixel = getPixel(picture,0,0)
>>> print newPixel
Pixel red=64 green=255 blue=255
### --> Compare the two red values
'''