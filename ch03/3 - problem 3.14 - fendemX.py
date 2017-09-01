# Chapter 3 - Problem 3.14
# Required:
# >>> findem4(4)
# 'abcdabcdabcdabcdabcdabcdab'
def findem1(n):
  letters1 = 'abcdefghijklmnopqrstuvwxyz'
  pile1 = ''
  for index in range(0,n):
    pile1 = pile1 + letters1[index]
  return pile1

#####
def findem2(n):
  letters2 = 'abcdefghijklmnopqrstuvwxyz'
  pile2 = ''
  for index in range(0,n % len(letters2)):
    pile2 = pile2 + letters2[index]
  return pile2

#####
def findem3(n):
  letters3 = 'abcdefghijklmnopqrstuvwxyz'
  pile3 = ''
  for index in range(1, len(letters3)):
    pile3 = pile3 + letters3[n % index]
  return pile3

##### WINNER #####
def findem4(n):
  letters4 = 'abcdefghijklmnopqrstuvwxyz'
  pile4 = ''
  for index in range(0, len(letters4)):
    pile4 = pile4 + letters4[index % n]
  return pile4