## Chapter 3 - Problem 3.13
def dupTimes1(something):
  dup = ''
  for index in range(0, len(something)):
    dup = dup + (2*something[index])
  return dup
  
########
def dupTimes2(something):
  dup = ''
  for index in range(0, len(something)):
    dup = dup + (index*something[index])
  return dup

########
def dupTimes3(something):
  dup = '_'
  for index in range(0, len(something)):
    dup = dup + something[index]
  return dup
  
########
#def dupTimes4(something):
#  for index in range(0, len(something)):
#    dup = dup + something[index]  # <--'dup' is referenced before assignment
#  dup = '' 
#  return dup