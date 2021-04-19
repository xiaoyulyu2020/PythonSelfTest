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

   def maxone(self):
      return max(self.adj.values(), key=len)


def main():
   with open(sys.argv[1]) as f:
      G = Graph()
      for line in f:
         lines = line.strip().split()
         start, end = lines[0], lines[-1]
         G.add_edge(start, end)
   print(G.adj)
   for c in G.adj:
      if len(G.adj[c]) != 0:
         print(f"{c} have {len(G.adj[c])} number of destinations")
         destinations = ",".join(G.adj[c])
         print(f"{c} can fly to {destinations}")

   for c in G.adj:
      if G.adj[c] == G.maxone():
         print(f"The most flexiable country is {c}, routs {len(G.maxone())}")

if __name__ == "__main__":
   main()