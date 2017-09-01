def notvowels(myString):
  for myLetter in myString:
    if not (myLetter.lower()) in 'aeiou':
      print("This is NOT a vowel: ")
      print myLetter.lower()
#    elif not (myLetter.upper() in 'AEIOU'):
#      print("This is NOT a vowel: ")
#      print myLetter.lower()
    else:
      print("This is IS A VOWEL:: ")
      print myLetter.lower()