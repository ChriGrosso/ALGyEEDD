import graph_24 as g
G = g.Graph ()
G. add_edge (0, 1)
G. add_edge (2, 1)
G. add_edge (1, 4)
G. add_edge (4, 3)
G. add_edge (5, 4)
G. add_edge (3, 0)
G. add_edge (5, 2)
print(G)

print (f' DFS forest : {G . dfs ()} ')
print ()
print (G)
print ()
print (f' scc : {G . tarjan ()} ')