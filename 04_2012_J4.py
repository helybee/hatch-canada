# Big Bang Secrets

k = input()
encoded = raw_input().upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

if len(encoded) > 20 or k >= 10:
  print("Encoded string must be less than 20 characters long, and parameter k must be less than 10.")
  
else:
  p = 1
  answ = ""
  for letter in encoded:
    new_idx = alphabet.find(letter)
    orig_idx = (new_idx - k) - (3 * p)
    p += 1
    answ += alphabet[orig_idx]
    
print answ