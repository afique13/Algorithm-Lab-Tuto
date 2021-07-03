
from collections import defaultdict

class Vertex:
    
    def __init__(self):
        
        self.graph = defaultdict(list)
        
    def addVertex(self, u, v):
        self.graph[u].append(v)
        
    def DFSpath(self, v, path, final):
        
        path.append(v)

        if v == final:
            print("The path from",path[0],"to",final,"is",path)
        
        for adjacent in self.graph[v]:
            if adjacent not in path:
                self.DFSpath(adjacent, path, final)
        
    def DFS(self, v, final):
        
        path = list()

        self.DFSpath(v, path, final)
        
        
v = Vertex()
v.addVertex(0,1)
v.addVertex(0,2)
v.addVertex(1,2)
v.addVertex(2,3)
v.addVertex(3,4)
v.addVertex(4,3)
v.addVertex(3,5)
v.addVertex(5,6)
v.addVertex(6,6)

v.DFS(0,4)   