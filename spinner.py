#!/usr/bin/python3
import os, json
from sys import argv
from string import ascii_uppercase as l
from random import choice, randrange

import shell


BOX = "box/"
if len(argv) < 2:
 SNAILCOUNT = 8
else:
 SNAILCOUNT = int(argv[1])


# def shell():
#  shell = {
#   'name': quickname(),
#   'cach': {
#    'type': "v0.01",
#    'filedir': ""
#   },
#   'macro': {},
#   'mem': [randrange(512) for _ in range(16)]
#  }
#
#  return shell

def boxsnail(snail):
 global BOX

 f = open("{}{}_snail.json".format(BOX, snail['name']), "w")
 f.write(json.dumps(snail))
 f.close()

def finalspin():
 global SNAILCOUNT

 tshell = {}
 for n in range(SNAILCOUNT):
  tshell = shell.rndshell()

  takennames = shell.getsnaillist()
  while tshell['name'] in takennames:
   tshell['name'] = shell.quickname()

  boxsnail(tshell)

# finalspin()
print(shell.rngmacro())
