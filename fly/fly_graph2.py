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

   def get_path(self, start, end, path=[]):
      path = path + [start]
      if start == end:
         return [path]#[path] return to new_path=
      if start not in self.adj:
         print("Not avialable")
      paths = []
      for node in self.adj[start]:
         if node not in path:
            new_path = self.get_path(node, end, path)#path->where node come from
            for p in new_path:
               paths.append(p)
      return paths
def main():
   G = Graph()
   with open(sys.argv[1]) as f:
      for line in f:
         edge = line.strip().split()
         G.add_edge(edge)
   # print(G.get_path("Mumbai", "NewYork"))
   print(G.adj)
if __name__ == "__main__":
   main()