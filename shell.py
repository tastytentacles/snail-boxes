# grater shell collection
from random import choice, randrange


IFLST = [
 "{}if {} < {}:\n",
 "{}if {} > {}:\n",
 "{}if {} == {}:\n",
 "{}if {} != {}:\n"
]

CMDLST = [
 "{}{} = {}\n"
]

SHELLS = {
 # 'v0.01':{
 #  'name': quickname(),
 #  'cach': {
 #   'type': "v0.01",
 #   'filedir': ""
 #  },
 #  'macro': [],
 #  'mem': [randrange(512) for _ in range(16)]
 # }
}

SHELLNAMES = [n for n in SHELLS]

def getsnaillist():
 global BOX

 def f(q):
  if "_snail.json" in q:
   return q.replace("_snail.json", "")

 raw = os.listdir(BOX)
 return [f(n) for n in raw]

def quickname():
 return "".join([choice(l) for _ in range(8)])

def rngmacro():
 global IFLST, CMDLST

 def addrule(depth=0):
  lines = [n for n in macro if macro[depth] != " "]

  t = choice(lines)
  macro.insert(macro.index(t) + 1, choice(CMDLST).format("".join([" " for _ in range(depth + 1)]), "mem[{}]".format(randrange(16)), "mem[{}]".format(randrange(16))))

 macro = []
 for _ in range(32):
  macro.append(choice(IFLST).format("", "mem[{}]".format(randrange(16)), "mem[{}]".format(randrange(16))))

 _ = [addrule() for _ in range(4)]



 f = open("macro.py", "w")
 f.writelines(macro)
 f.close()

 return macro

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
