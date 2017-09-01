def buildCipher(key):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  rest = ''
  for letter in alpha:
    if not(letter in key):
      rest = rest + letter
    print key+rest