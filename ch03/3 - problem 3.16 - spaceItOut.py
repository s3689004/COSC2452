# Chapter 3 - Problem 3.16
# Function that takes a string and a number of spaces to insert between each letter
# then print the resultant string
# EG:
# spaceutout('It was a dark and stormy night', 3)
#def spaceitout(text, spaces):
 # print('Original text: ' + text)
#  print('Number of spaces: ' + spaces)
 # print(text.split('-',2))
def split_line(text):
  words = text.split(',')
  for word in words:
    print(word)