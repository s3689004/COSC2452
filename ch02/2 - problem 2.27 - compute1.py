def compute():
  distanceInMiles = 3279.8
  metersPerMile = 1609.34
  distanceInMeters = distanceInMiles * metersPerMile
  turtleSpeed = 0.5
  turtleSecondsM2S = distanceInMeters / turtleSpeed
  print("Time in seconds")
  print("For turtle from Miami to Seattle:")
  print(turtleSecondsM2S)
  turtleMinutes = turtleSecondsM2S / 60
  print("In minutes:")
  print(turtleMinutes)
  turtleHours = turtleMinutes / 60
  turtleDays = turtleHours / 24
  turtleWeeks = turtleDays / 7
  print("In weeks:")
  print(turtleWeeks)