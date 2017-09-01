# Chapter 3 - Problem 3.15
# Required:
# >>> mixem_("we hold these truths")
# 'w.e. .h.o.l.d. .t.h.ese truths'

def mixem1(aString):
  mix = ''
  for index in range(0, len(aString), 2):
    mix = mix + aString[index]
  mix = mix + '-'
  for index in range(len(aString)/2, len(aString)):
    mix = mix + aString[index]
  return mix
  
##### WINNER #####
def mixem2(aString):
  mix = ''
  for index in range(0, len(aString)/2):
    mix = mix + aString[index]+'.'
  for index in range(len(aString)/2, len(aString)):
    mix = mix + aString[index]
  return mix

#####
def mixem3(aString):
  mix = ''
  for index in range(0, len(aString)/2, 2):
    mix = mix + aString[index]
  mix = mix + '-'
  for index in range(1, len(aString), 2):
    mix = mix + aString[index]
  return mix

#####
def mixem4(aString):
  mix = ''
  for index in range(len(aString)/2,0,-1):
    mix = aString[index]+mix + aString[index]  
  return mix