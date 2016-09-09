# CCC Junior 2012 Problem 2
def check_readings(d1, d2, d3, d4):
  
  if d1 < d2 and d2 < d3 and d3 < d4:
    print "Fish Rising"
  elif d1 > d2 and d2 > d3 and d3 > d4:
    print "Fish Diving"
  elif d1 == d2 and d2 == d3 and d3 == d4:
    print "Constant Depth"
  else:
    print "No Fish"
    
depth1 = raw_input()
depth2 = raw_input()
depth3 = raw_input()
depth4 = raw_input() 

try:
  depth1 = int(depth1)
  depth2 = int(depth2)
  depth3 = int(depth3)
  depth4 = int(depth4)
except TypeError:
  raise TypeError('Input was not of type int')

if type(depth1) == int and type(depth2) == int and type(depth3) == int and type(depth4) == int:
  check_readings(depth1, depth2, depth3, depth4)
else:
  print "inputs were not integers, please try again."