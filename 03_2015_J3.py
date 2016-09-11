# CCC Junior 2015 Problem 3
import math

# Every consonant is replaced by 3 letters: the consonant itself, the closest alphabetical vowel, the next alphabetical consonant
VOWELS = "aeiou"
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def find_closest_vow(i):
  
  i_ind = ALPHABET.find(i)
  closest_dist = 26
  closest_ind = 26
  
  for vow in VOWELS:
    
    vow_ind = ALPHABET.find(vow)
    distance = abs(vow_ind - i_ind)
    
    # If distance of vowel is equal, earliest vowel in alphabet wins, therefore, don't update anything on equality
    if distance < closest_dist:
      closest_ind = vow_ind
      closest_dist = distance
    print closest_ind
      
  return ALPHABET[closest_ind]
  
  
def find_next_cons(j):
  
  cons_ind = ALPHABET.find(j)
  
  if j == "z":
    return "z"
  
  if ALPHABET[cons_ind + 1] not in VOWELS:
    return ALPHABET[cons_ind + 1]
  else:
    return ALPHABET[cons_ind + 2]
  
  
def insert_triplet(k):
  return k + find_closest_vow(k) + find_next_cons(k)

def rovarspraket(eng):
  
  i = 0
  while i < len(eng):
    if eng[i] not in VOWELS:
      replacement = eng.replace(eng[i], insert_triplet(eng[i]))
      eng = replacement
      i = i + 3
    else:
      i = i + 1
  
  return eng
  

def main():
  
  original = raw_input()
  result = rovarspraket(str(original))
  print result
  
main()