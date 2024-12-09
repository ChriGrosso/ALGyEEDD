from typing import Set, List, Generator, Tuple, KeysView, Iterable
import os
import random
import matplotlib.pyplot as plt

class Graph:
    
    def __init__(self):
        self._V = dict()             # Dictionary with G nodes: Dict[str, Dict[str]] 
        self._E = dict()             # Dictionary with G edges: Dict[str, Set]
    
    def add_node(self, vertex) -> None:
        ''' Agrega un nodo al grafo si no existe. '''
        if vertex not in self._V:  # Solo agrega si el nodo no está en el grafo
            self._init_node(vertex)
            self._E[vertex] = set()  # Inicializa el conjunto de aristas del nodo
        pass

    def add_edge(self, vertex_from, vertex_to) -> None:
        ''' Agrega una arista del nodo vertex_from al nodo vertex_to. Los nodos se agregan si no existen. '''
        self.add_node(vertex_from)
        self.add_node(vertex_to)
        self._E[vertex_from].add(vertex_to)  # Agrega una arista dirigida desde vertex_from hacia vertex_to
    
    def nodes(self) -> KeysView[str]:
        ''' Devuelve todas las claves de los nodos en el grafo. '''
        return self._V.keys()
    
    def adj(self, vertex) -> Set[str]:
        ''' Devuelve el conjunto de nodos adyacentes al nodo dado. '''
        return self._E.get(vertex, set())  # Retorna los adyacentes o un conjunto vacío si no tiene aristas

    def exists_edge(self, vertex_from, vertex_to) -> bool:
        ''' Devuelve True/False si vertex_to se encuentra en la
            lista de adyacencia de vertex_from'''
        return vertex_to in self.adj(vertex_from)
        
    def dfs(self, nodes_sorted: Iterable[str] = None) -> List[List[Tuple]]:
        ''' Implementación de búsqueda en profundidad (DFS) en el grafo, devolviendo un bosque DFS. '''
        
        # Si no se especifica un orden, usa los nodos en el orden natural
        if nodes_sorted is None:
            nodes_sorted = self.nodes()

        dfs_forest = []  # Bosque DFS que contiene listas de árboles DFS
        time = 0  # Tiempo de descubrimiento y finalización para nodos en DFS

        def dfs_visit(vertex, parent):
            nonlocal time  # Permite que dfs_visit modifique la variable 'time' en dfs
            # Código de dfs_visit que modifica y usa 'time'
            self._V[vertex]['color'] = 'GRAY'  # Nodo en proceso de exploración
            self._V[vertex]['d_time'] = time = time + 1  # Marca el tiempo de descubrimiento
            tree.append((vertex, parent))  # Agrega el nodo al árbol DFS

            for adj in self.adj(vertex):  # Recorre los nodos adyacentes
                if self._V[adj]['color'] == 'WHITE':  # Solo visita nodos no explorados
                    self._V[adj]['parent'] = vertex
                    dfs_visit(adj, vertex)

            self._V[vertex]['color'] = 'BLACK'  # Nodo completamente explorado
            self._V[vertex]['f_time'] = time = time + 1  # Marca el tiempo de finalización

        # Ejecuta DFS para cada componente en el orden especificado
        for node in nodes_sorted:
            if self._V[node]['color'] == 'WHITE':  # Solo comienza DFS si el nodo no fue explorado
                tree = []
                dfs_visit(node, None)
                dfs_forest.append(tree)  # Agrega el árbol DFS al bosque

        return dfs_forest
    
    def tarjan(self) -> List[List[str]]:
        """
        Implementación del algoritmo de Tarjan para encontrar las componentes fuertemente conexas (SCC).
        Devuelve una lista de listas, donde cada lista representa una SCC.
        """
        # Paso 1: Realizar DFS en el grafo original para calcular tiempos de finalización
        self.dfs()  # Realiza el recorrido DFS para llenar los tiempos de finalización

        # Ordenar los nodos por tiempo de finalización (mayor a menor)
        nodes_sorted_by_finish_time = sorted(
            self._V.keys(),
            key=lambda node: self._V[node]['f_time'],
            reverse=True,
        )

        # Paso 2: Crear el grafo transpuesto
        transposed_graph = graph_conjugate(self)

        # Paso 3: Realizar DFS en el grafo transpuesto usando el orden inverso
        # Cada componente del bosque DFS será una SCC
        sccs = transposed_graph.dfs(nodes_sorted_by_finish_time)

        # Convertir cada árbol del bosque en una lista simple de nodos
        return [[node for node, _ in tree] for tree in sccs]

        
    def _init_node(self, vertex) -> None:
        ''' Inicializa los atributos básicos de un nodo (color, padre, tiempo de descubrimiento y finalización). '''
        self._V[vertex] = {'color': 'WHITE', 'parent': None, 'd_time': None, 'f_time': None}
    
    def __str__(self) -> str:
        ''' Genera una representación en string del grafo mostrando los nodos y sus aristas en el formato solicitado. '''
        result = ["Vertices:"]
        # Imprime cada nodo y sus atributos
        for v, attrs in self._V.items():
            result.append(f"{v}: {attrs}")
        
        result.append("\nAristas:")
        # Imprime cada nodo y sus aristas con llaves para formato
        for v, edges in self._E.items():
            if edges:  # Solo muestra nodos con aristas
                # Inicializar la cadena de las aristas
                edge_str = "{"
                # Iterar sobre las aristas de un nodo
                for i, edge in enumerate(edges):
                    edge_str += str(edge)  # Convertir a cadena
                    if i < len(edges) - 1:  # Si no es la última arista, agregar coma
                        edge_str += ", "
                edge_str += "}"
                result.append(f"{v}: {edge_str}")
        
        return "\n".join(result)


            
### Auxiliary functions to manage graphs ########
                
def read_adjlist(file: str) -> Graph:
    ''' Read graph in adjacency list format from file.'''
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

def graph_conjugate(G: Graph) -> Graph:
    """Crea el grafo traspuesto del grafo G"""
    # Crea nuevo grafo
    transposed_graph = Graph()
    # Anade todo los nodos
    for node in G.nodes():
        transposed_graph.add_node(node)
    # Inverte todas las aristas
    for node in G.nodes():
        for adj_node in G.adj(node):
            transposed_graph.add_edge(adj_node, node)
    return transposed_graph
