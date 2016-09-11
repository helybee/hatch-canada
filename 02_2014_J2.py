# CCC Junior 2014 Problem 2

# The input will be two lines. The first line will contain V (1 <= V <= 15), the total number of
# votes. The second line of input will be a sequence of V characters, each of which will be A or B,
# representing the votes for a particular singer.

# The output will be one of three possibilities:
#   A, if there are more A votes than B votes;
#   B, if there are more B votes than A votes;
#   Tie, if there are an equal number of A votes and B votes.

def find_winner(num, votes):
  a_count = 0
  b_count = 0
  invalid_count = 0
  
  for i in votes:
    if i == 'A':
      a_count = a_count + 1
    elif i == 'B':
      b_count = b_count + 1
    else:
      invalid_count = invalid_count + 1
      
  if a_count > b_count:
    print "A"
  if a_count < b_count:
    print "B"
  if a_count == b_count:
    print "Tie"

def main():
  v = raw_input()
  seq = raw_input()
  
  # Ensure inputs are of correct type
  try:
    v = int(v)
    seq = str(seq)
    except TypeError: 
      print "First input must be an integer value and second input must be a sequence of A's and B's"

  if v >= 1 and v <= 15:
    if v == len(seq):
      find_winner(v, seq)
      else: 
        print "Number of votes does not match the number of ballots"
      else:
        print "number of votes must be between 1 and 15"
        
main()