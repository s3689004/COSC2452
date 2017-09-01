def encode(myString, keyLetters):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  secret = ''
  for letter in myString:
    index = alpha.find(letter)
    secret = secret + keyLetters[index]
  print secret