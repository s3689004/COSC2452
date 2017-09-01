def koan(sentence):
  parts = sentence.lower().split()
  subject = parts[0]
  verb = parts[1]
  object = parts[2]
  more = parts[3]
  print("Sentence = "+ sentence)
  print("Subject = " +subject)
  print("Verb = " +verb)
  print("Object = " +object)
  print("More = " +more)
