def reverseString(theString):
  thePile = ""
  for i in range(len(theString)-1,-1,-1):
    thePile = thePile + theString[i]
  print thePile