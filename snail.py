#!/usr/bin/python3

import os
import curses as c
from random import choice
from curses import wrapper
from string import ascii_lowercase


f = {
 'width': 64,
 'height': 32
}

board = {
 'tile': [[0 for n in range(16)] for _ in range(16)],
 'dat': {
  'tiles': 16,
  'twidth': 4,
  'theight': 2
 }
}

snailbox = []


def addSnail():
 snail = {
  'atp': 100,
  'name': str.__str__([choice(ascii_letters) for _ in range(8)])
 }

 return snail

def main(stdscr):
 global f, board

 stdscr.clear()
 stdscr.addstr(0, 8, "snail.py      v0.01")
 stdscr.addstr(f['height'] + 2, 8, "tile size: {}".format(board['dat']['tiles']))
 stdscr.refresh()

 hello = c.newwin(f['height'], f['width'], 2, 4)
 hello.clear()
 for y in range(f['height'] - 1):
  for x in range(f['width'] - 1):
   hello.addch(y, x, '#')
 hello.refresh()

 hello.getkey()

wrapper(main)
