from typing import Set, List, Generator, Tuple, KeysView, Iterable
import os
from collections import deque


class Graph:
    
    def __init__(self):
        self._V = dict()             # Dictionary with G nodes: Dict[str, Dict[str]] 
        self._E = dict()             # Dictionary with G edges: Dict[str, Set]
    

    def add_node(self, vertex) -> None:
        ''' Add a single node if it is not in the graph
        '''
        for clave in self._V.keys():
            if(clave==vertex):
                return None
        self._init_node(vertex)
        self._E[vertex]=set()
        pass

    
    def add_edge(self, vertex_from, vertex_to) -> None:
        ''' Add an edge from vertex_from to vertex_to. The nodes will be 
            added if they are not already in the graph.
        '''
        self.add_node(vertex_from)
        self.add_node(vertex_to)
        self._E[vertex_from].add(vertex_to)
        pass
   
    def nodes(self) -> KeysView[str]:
        '''Devuelve las keys de los nodos del grafo'''
        return self._V.keys()
        pass
                      
    def adj(self, vertex) -> Set[str]:
        '''Devuelve los nodos adyacentes a vertex '''
        return self._E.get(vertex, set())
        pass

    def exists_edge(self, vertex_from, vertex_to)-> bool:
        ''' Devuelve True/False si vertex_to se encuentra en la
            lista de adyacencia de vertex_from
        '''
        if(self._E[vertex_from] in self.adj(self,vertex_to)):
            return True
        else:
            return False
        
    def _init_node(self, vertex) -> None:
        ''' Set vertex initial values'''

        self._V[vertex] = {'color': 'WHITE', 'parent': None, 
                           'd_time': None, 'f_time': None}
        
    def __str__(self) -> str:
        result = ["Vertices:"]
        for v, attrs in self._V.items():
            result.append(f"{v}: {attrs}")
        result.append("\nAristas:")
        for v, edges in self._E.items():
            if edges:  # Only show nodes with edges
                result.append(f"{v}: {sorted(edges)}")
        return "\n".join(result)

    def dfs(self, nodes_sorted: Iterable[str] = None) -> List[List[Tuple]]:
        ''' Depth find search driver
        nodes_sorted: Si se le pasa un iterable el bucle principal de DFS
        se iteraria segun el orden del iterable (eg en Tarjan)
        Devuelve un bosque dfs en la que cada una de las sublistas es un
        arbol dfs. Cada elemnto del arbol es una tupla (vertex, parent)
        '''
    pass

            
### Auxiliary functions to manage graphs ########
                
def read_adjlist(file: str) -> Graph:
    ''' Read graph in adjacency list format from file.
    '''
    G = Graph()
    with open(file,'r') as f:
        for line in f:
            l = line.split()
            if l:           
                u = l[0]
                G.add_node(u)
                for v in l[1:]:
                    G.add_edge(u, v)
    return G
        

def write_adjlist(G: Graph, file: str) -> None:
    '''Write graph G in single-line adjacency-list format to file.'''
    file_path = os.path.join(os.path.dirname(__file__), file) 
    with open(file_path,'r') as f:
        for u in G.nodes():
            f.write(f'{u}')
            f.writelines([f' {v}' for v in G.adj(u)])
            f.write('\n')

    
### Driver code

# if __name__ == '__main__':
#     G = read_adjlist('./graph.txt')
#     print(G)

# G=Graph()
# G.add_node(1)
# G.add_node(2)
# G.add_node(2)
# claves=G.nodes()
# print(claves)
# print(G._V[1]["color"])
# for clave in G._V.keys():
#     print(clave)

G = Graph ()
G.add_edge (0, 1)
G.add_edge (2, 1)
G.add_edge (1, 4)
G.add_edge (4, 3)
G.add_edge (5, 4)
G.add_edge (3, 0)
G.add_edge (5, 2)

print(G)