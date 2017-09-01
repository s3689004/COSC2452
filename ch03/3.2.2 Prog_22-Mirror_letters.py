def Mirror(theSource):
  aPile = ""
  for theLetter in theSource:
    aPile = theLetter + aPile + theLetter
  print aPile