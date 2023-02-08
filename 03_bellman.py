from sys import maxsize
class Graph:
    def __init__(self,V):
        self.V=V
    
    def addEdge(self,src,dest,wt):
        self.graph.append([src,dest,wt])
    
v=int(input("Enter the number of vertices: "))
e=int(input("Enter the number of edges: "))
graph=Graph(v)
print("Enter the source,destination and weight of the edges: ")
for i in range(e):
    src=int(input("Enter the source node: "))
    dest=int(input("Enter the destination node: "))
    weight=int(input("Enter the weight of the edges: "))
    graph.addEdge(src,dest,weight)

source=int(input("Enter the source node: "))
graph.bellmanford(source)