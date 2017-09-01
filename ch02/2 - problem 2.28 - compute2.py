def compute2():
  gravity = 6.67384E-11
  earthMass = 5.9736E24
  earthRadius = 6371000
  velocity = (2 * gravity * earthMass) / earthRadius
  result = sqrt(velocity)
  print "Escape velocity:"
  print result