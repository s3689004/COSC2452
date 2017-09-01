def koan2(sentence):
  parts = sentence.lower().split()
  verbIndex = 1
  objIndex = 2
  subject = parts[0]
  if subject in ['the','an','a']:
    subject = parts[1]
    verbIndex = 2
    objIndex = 3
  verb = parts[verbIndex]
  object = parts[objIndex]
  if object in ['a','an','the']:
    object = parts[4]
  print("")
  print("Expected position:")
  print(" 0. SUBJECT")
  print(" 1. VERB")
  print(" 2. OBJECT")
  print("")
  print("Whole SENTENCE = '" +sentence+"'")
  print("")
  print("But sometimes: " +object+ " " +verb+ " " +subject)
  print("Sometimes there is no " +subject)
  print("Sometimes there is no " +verb)
  print("")
  print("OBJECT:  " +object)
  print("VERB:  " +verb)
  print("SUBJECT:  " +subject)
  print("")