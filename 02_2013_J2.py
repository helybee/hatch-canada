# CCC Junior 2013 Problem 2013
# Rotating Letters
# An artist wants to construct a sign whose letters will rotate freely in the breeze. 
# In order to do this, she must only use letters that are not changed by rotation of 180 degrees: I, O, S, H, Z, X, and N.
# Write a program that reads a word and determines whether the word can be used on the sign.

def can_rotate(w):
  ok_letters = "IOSHZXN"
  is_ok = True
  
  for k in w:
    if ok_letters.find(k) >= 0:
      continue
    else:
      print "NO"
      is_ok = False
      break
  if is_ok:
    print "YES"

word = raw_input('Enter potential sign word: ')
can_rotate(word)

