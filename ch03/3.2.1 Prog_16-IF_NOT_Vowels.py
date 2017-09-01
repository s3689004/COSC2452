def notvowels(myString):
  for myLetter in myString:
    if not (myLetter in 'aeiouAEIOU'):
      print("This is NOT a vowel: ")
      print myLetter.lower()