# Program that lists all values in the fibonnacci sequence up to and including a given number
import sys

def input_ok(m):
  try:
    m = int(m)
    if m > 1:
      return True
    else:
      return False
  except:
    return False


def gen_fibonnaci(n):
  seq = [1,1]
  
  while seq[-2] + seq[-1] <= n:
    seq.append(seq[-2] + seq[-1])
    
  print seq
  
  
def main():
  num = raw_input("n = ")
  if input_ok(num):
    gen_fibonnaci(int(num))
  else:
    print "There was a problem generating the sequence with the given input"
    
main()
  
  