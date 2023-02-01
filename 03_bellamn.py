from sys import maxsize
class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[]
    def addEdge(self,u,v,wt):
        self.graph.append([u,v,wt])
    def bellmanFord(self,src):
        dist=[maxsize]*self.v
        
v=int(input("Enter the number of vertices: "))
e=int(input("Enter the number of edges: "))

graph=Graph(v)
print("Enter the src and destination weights of edges")
for _ in range(e):
    u,v,wt=map(int,input().split())
    graph.addEdge(u,v,wt)
source=int(input("Enter the source node: "))
graph.bellmanFord(source)