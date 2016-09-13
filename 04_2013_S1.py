# CCC Senior 2013 Problem 1
# Given a year, find next year with distinct digits

def is_unique(year):
  chars = []
  for k in year:
    if k not in chars:
      chars.append(k)
    else:
      return False
  if len(chars) == len(year):
    return True
  

def increment_year(year):
  
  # Create a marking array to indicate which of 10 digits are taken
  nums = [False] * 10
  done = False
  
  # Iterate through the year's digits and mark them in nums
  for i in range(0,len(year)):
    print "year[%i] = " %i, year[i], "year = ", year 
    if nums[int(year[i])] == False:
      nums[int(year[i])] = True
    
    # Digit was taken, take the next available digit, and reset all succeeding digits
    else:
      k = int(year[i])
      
      # If k = 9, set digit to zero, update preceding digit, and rerun function
      if k == 9:
        k = 0
        preceding = year[0:i]
        
        if preceding == "":
          preceding = "1"
          year = preceding + year # adds extra unit length of 1 when increasing digit length (i.e. 999 to 1000)
          return year, done
        
        else:
          preceding = str(int(preceding) + 1)
        print "check 1"
        year = preceding + str(k) + str(0) * (len(year) - (i + 1)) # reset
        increment_year(year)
        
      while nums[k] == True:
        k = k + 1
      if k < len(year):
        print "check 2"
        year = year[0:i] + str(k) + str(0) * (len(year) - (i + 1)) # reset
      else:
        print "check 3"
        year = year[0:i] + str(k)
      nums[k] = True
   
  done = is_unique(year)
  return year, done
  
def main():
  
  current_year = raw_input()
  try:
    int(current_year)
  except:
    TypeError("Please enter an integer value")
  
  year = current_year
  if int(current_year) >= 0 and int(current_year) <= 10000:
    year, done = increment_year(year)
    while done != True:
      year, done = increment_year(year)
    
  else:
    print "Please enter a year greater than 0 and less than 10000 inclusively."
  print year

  
main()