#!/usr/bin/env python3

import sys

class Graph(object):
   def __init__(self):
      self.adj = {}

   def add_edge(self, start, end):
      if start not in self.adj:
         self.adj[start] = [end]
      else:
         self.adj[start].append(end)
      if end not in self.adj:
         self.adj[end] = [start]
      else:
         self.adj[end].append(start)


def main():
   with open(sys.argv[1]) as f:
      G = Graph()
      for line in f:
         lines = line.strip().split()
         start, end = lines[0], lines[-1]
         G.add_edge(start, end)
   print(G.adj)

if __name__ == "__main__":
   main()