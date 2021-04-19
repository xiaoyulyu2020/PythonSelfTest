#!/usr/bin/env python3

import sys

class Graph(object):
   def __init__(self):
      self.adj = {}

   def add_edge(self, edge):
      start, end = edge[0], edge[1]
      if start not in self.adj:
         self.adj[start] = [end]
      else:
         self.adj[start].append(end)



def main():
   G = Graph()
   with open(sys.argv[1]) as f:
      for line in f:
         edge = line.strip().split()
         G.add_edge(edge)

   print(G.adj)
if __name__ == "__main__":
   main()