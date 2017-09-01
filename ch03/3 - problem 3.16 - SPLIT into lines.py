# will split a string on text at each comma ','
def split_line(text):
  words = text.split(',')
  for word in words:
    print(word)