# Accommodate spaces and punctuation
def dblDutch(theName):
  thePile = ""
  for aLetter in theName:
    if aLetter.lower() in "aeiou":
      thePile = thePile + aLetter
    if not (aLetter.lower() in "aeiou"):
      thePile = thePile + aLetter + "_" + aLetter
  print thePile