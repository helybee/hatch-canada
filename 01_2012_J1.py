# CCC Junior 2012 Problem 1

# Check types
def check_input(value):
  # Value must be of type int
  try:
    value = int(value)
  except ValueError:
    print "Apparently %s is not a number" % value
  
  # Car speed and limit must be positive ints
  try:
    assert value >= 0
  except(AttributeError):
    raise AssertionError('input should be positive')
    
  return value

# Define function
def check_fine(limit, speed):

  # Fine amounts
  lowFine = 100
  midFine = 270
  highFine = 500

  # Check speeding amounts
  difference = speed - limit
  if (difference <= 0):
    print "Congratulations, you are within the speed limit!"
  elif (difference > 30):
    print "You are speeding, and your fine is $%i" % (highFine)
  elif (difference > 20):
    print "You are speeding, and your fine is $%i" % (midFine)
  elif (difference > 0):
    print "You are speeding, and your fine is $%i" % (lowFine)
  else:
    print "problem"
  
def main():
  # Prompt user for speed limit and recorded speed of car
  speed_limit = raw_input("Enter the speed limit: ")
  car_speed = raw_input("Enter the recorded speed of the car: ")

  speed_limit = check_input(speed_limit)
  car_speed = check_input(car_speed)

  if type(speed_limit) ==  int and type (car_speed) == int:
    check_fine(speed_limit, car_speed)
  else:
    print "Please retry with integers as the limit and car speed"
    
main()
