def count_frowns(t):
  num = t.split(":-(")
  return len(num) - 1
  
def count_smiles(t):
  num = t.split(":-)")
  return len(num) - 1

def main():
  text = raw_input()
  frowns = count_frowns(text)
  smiles = count_smiles(text)
  
  if smiles > frowns:
    print "happy"
  elif smiles < frowns:
    print "sad"
  elif smiles == frowns:
    print "unsure"
  else:
    print "none"
main()