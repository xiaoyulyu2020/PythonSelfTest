#!/usr/bin/env python3

def main():
   s = input()
   stack = []
   for c in s:
      if c not in stack:
         stack.append(c)
      else:
         print(c)
         return
if __name__ == "__main__":
   main()
