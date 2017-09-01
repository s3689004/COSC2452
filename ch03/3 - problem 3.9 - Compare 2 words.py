# Chapter 3 Problem 3.9
# Compare 2 words and print the letters which appear in both
def in_both(wordA, wordB):
  print('Word A is: ' + wordA)
  print('Word B is: ' + wordB)
  for letterA in wordA:
    if letterA in wordB:
      print(letterA)