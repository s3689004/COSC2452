def separate(String1):
  odds = ""
  even = ""
  for i in range(len(String1)):
    if i % 2 == 0:
      even = even + String1[i]
    if not (i % 2 == 0):
      odds = odds + String1[i]
  print "Odds: " , odds
  print "Even: " , even