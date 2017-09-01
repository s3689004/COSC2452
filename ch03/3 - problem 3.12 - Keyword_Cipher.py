# 1. Keyword at end of alphabet, not front (Chang line 11 to:  print rest+key)
# 2. Reverese alphabet, before concatenating it to the keyword (Change line 10 to:  rest = letter + rest)
# 3. Separate the vowels & consonants in the rest of the alphabet so that the cipher alphabet is keyword
## then the rest of the vowels, then the rest of the consonants
def buildCipher(key):
  alpha = 'abcdefghijklmnopqrstuvwxyz'
  rest = ''
  for letter in alpha:
    if not(letter in key):
      rest = letter + rest
    print rest + key