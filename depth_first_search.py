class Graph(object):
    def __init__(self,*args,**kwargs):
        self.node_neighbors={}
        self.visited={}
    def add_nodes(self,nodelist):
        for node in nodelist:
            self.add_node(node)
    def add_node(self,node):
        if not node in self.nodes():
            self.node_neighbors[node]=[]
    def add_edge(self,edge):
        u,v=edge
        if (v not in self.node_neighbors[u]) and (u not in self.node_neighbors[v]):
            self.node_neighbors[u].append(v)
            if(u!=v):
                self.node_neighbors[v].append(u)
    def nodes(self):
        return self.node_neighbors.keys()
    def depth_first_search(self,root=None):
        order=[]
        def dfs(node):
            self.visited[node] = True
            order.append(node)
            print(order)
            for n in self.node_neighbors[node]:
                if not n in self.visited:
                    dfs(n)
        if root:
            dfs(root)

        print (order)
        return order
if __name__=='__main__':
    g=Graph()
g.add_nodes([i+1 for i in range(8)])
g.add_edge((1,2))
g.add_edge((1,3))
g.add_edge((2,4))
g.add_edge((2,5))
g.add_edge((4,8))
g.add_edge((5,8))
g.add_edge((3,6))
g.add_edge((3,7))
g.add_edge((6,7))
print('nodes:',g.nodes())

order=g.depth_first_search(1)