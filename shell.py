# grater shell collection


SHELLS = {}
SHELLNAMES = [n for n in SHELLS]

def rndshell(ver=""):
 """
  returns a rng filled shell
  uses the most recent shell format by defalt
 """
 global SHELLS, SHELLNAMES
 
 if not ver in SHELLNAMES:
  s = SHELLS[SHELLNAMES[0]]
 else:
  s = SHELLS[ver]
 
 pass