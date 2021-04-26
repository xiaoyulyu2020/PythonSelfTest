#!/usr/bin/env python3

import sys

def getchar(s):
   char = ""
   for c in s.lower():
      if c in "abcdefghijklmnopqistuvwxyz":
         char += c
   return char

def palin(s):
   if len(s) <= 1:
      return True
   return s[0] == s[-1] and palin(s[1 : -1])

def main():
   for line in sys.stdin:
      s = line.strip()
      print(palin(getchar(s)))

if __name__ == "__main__":
   main()