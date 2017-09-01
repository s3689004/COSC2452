def mirrorHalfString1(aString):
  aPile = ''
  for i in range(0,len(aString)/2):
    aPile = aPile + aString[i]
  for i in range(len(aString)/2-1,-1,-1):
    aPile = aPile + aString[i]
  print("Original string =" + aString)
  print aPile