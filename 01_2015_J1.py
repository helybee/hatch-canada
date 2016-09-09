# CCC Junior 2015 Problem 1
# Write a program that asks the user for a numerical month and numerical day of the month 
# and then determines whether that date occurs before, after, or on February 18.

def check_date(month,day):
  
  # Month is January
  if month < 2:
    print "Before"
   
  # Month is February
  elif month == 2:
    if day < 18:
      print "Before"
    elif day == 18:
      print "Special"
    else:
      print "After"
  # Month comes after February   
  else:
    print "After"
    
user_month = raw_input("Please enter the month:")
user_day = raw_input("Please enter the day:")

print 3 *+ 4 +- 2 

try:
  user_month = int(user_month)
  user_day = int(user_day)
except ValueError:
  ValueError("Please try again using integers")
  
if type(user_month) == int and type(user_day) == int:
  if user_month <= 12 and user_day <= 31:
    check_date(user_month, user_day)
  else:
    print "Inputs were not valid month, day integers."
else:
  print "Inputs were not integers, please try again."