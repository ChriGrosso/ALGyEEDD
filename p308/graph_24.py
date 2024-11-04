from typing import Set, List, Generator, Tuple, KeysView, Iterable
import os


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
        self._V[vertex] = dict()
        pass

    
    def add_edge(self, vertex_from, vertex_to) -> None:
        ''' Add an edge from vertex_from to vertex_to. The nodes will be 
            added if they are not already in the graph.
        '''
        pass
   
    def nodes(self) -> KeysView[str]:
        '''Devuelve las keys de los nodos del grafo'''
        return self._V.keys()
        pass
                      
    def adj(self, vertex) -> Set[str]:
        '''Devuelve los nodos adjacentes a vertex '''
        pass

    def exists_edge(self, vertex_from, vertex_to)-> bool:
        ''' Devuelve True/False si vertex_to se encuentra en la
            lista de adyacencia de vertex_from
        '''
        pass
        
    def _init_node(self, vertex) -> None:
        ''' Set vertex initial values'''

        self._V[vertex] = {'color': 'WHITE', 'parent': None, 
                           'd_time': None, 'f_time': None}
        
    def __str__(self) -> str:
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
    '''Write graph G in single-line adjacency-list format to file.
    '''

    file_path = os.path.join(os.path.dirname(__file__), file) 
    with open(file_path,'r') as f:
        for u in G.nodes():
            f.write(f'{u}')
            f.writelines([f' {v}' for v in G.adj(u)])
            f.write('\n')

    
### Driver code

#if __name__ == '__main__':
    #G = read_adjlist('./graph.txt')
    #print(G)

G=Graph()
G.add_node(1)
G.add_node(2)
claves=G.nodes()
print(claves)
# for clave in G._V.keys():
#     print(clave)