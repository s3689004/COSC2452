def decode(secret, keyLetters):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  clear = ''
  for letter in secret:
    index = keyLetters.find(letter)
    clear = clear+alpha[index]
  print clear