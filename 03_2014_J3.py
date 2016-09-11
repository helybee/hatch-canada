# CCC Junior 2014 Problem 3
# Double Dice

def reduce_total(a_total, d_total, r):
  a, d = r.split()
  
  try:
    a = int(a)
    d = int(d)
  except:
    TypeError("not valid rolls")
    
  if a < d:
    a_total = a_total - d
    return a_total, d_total
  
  elif a > d:
    d_total = d_total - a
    return a_total, d_total
  
  else:
    return a_total, d_total

def main():
  a_total = 100
  d_total = 100
  
  num_games = raw_input()
  try:
    num_games = int(num_games)
  except:
    TypeError("please enter an integer.")
  
  rolls = ""
  if num_games > 0:
    for i in range(num_games):
      rolls = raw_input()
      a_total, d_total = reduce_total(a_total, d_total, rolls)
      
  print a_total
  print d_total
      
main()