def koan(sentence):
  parts = sentence.lower().split()
  subject = parts[0]
  verb = parts[1]
  object = parts[2]
  print "Sometimes "+ sentence
  print "But somtimes "+object+" "+verb+" "+subject
  print "Sometimes there is no " +subject
  print "Sometimes there is no " +verb
  print "Watch out for the " +verb