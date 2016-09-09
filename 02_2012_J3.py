# CCC Junior 2012 Problem 3

# Write a program that accepts a positive integer scaling factor and outputs the scaled icon. 
# A scaling factor of k means that each character is replaced by a k x k grid consisting only of that character.
from __future__ import print_function

def create_scaled_icon(f):
  icon = [
    "*x*",
    " xx",
    "* *"
  ]
  
  for line in icon:
    for i in range(f):
      for k in line:
        print(f * k, end = "")
      print()
    print()


k = raw_input()

try:
  k = int(k)
except TypeError:
  TypeError("scaling factor must be of type int")
  
if type(k) == int:
  if k > 0 and k < 25:
    create_scaled_icon(k)
  else:
    print("scaling factor must be greater than 0 and smaller than 25")
else:
  print("scaling factor is not an integer")