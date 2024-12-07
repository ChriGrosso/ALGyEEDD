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
    
    def exists_edge(self, vertex_from, vertex_to)-> bool:
        ''' Devuelve True/False si vertex_to se encuentra en la
            lista de adyacencia de vertex_from'''
        if(self._E[vertex_from] in self.adj(self,vertex_to)):
            return True
        else:
            return False
        
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

def erdos_renyi(n: int, m: float = 1.) -> Graph:
    """Devuelve un grafo aleatorio dirigido basado en el modelo Erdös-Rényi.
    n: número de nodos del grafo.
    m: número medio de vecinos por nodo.
    El número de vecinos se determina con una probabilidad p = m/n. """
    p = m / n  # Probabilidad de conexión
    G = Graph()
    for i in range(n):
        G.add_node(str(i))  # Los nodos son cadenas "0", "1", ..., "n-1"
    
    for i in range(n):
        for j in range(n):
            if i != j and random.random() < p:  # Evitar bucles (i -> i)
                G.add_edge(str(i), str(j))
    return G

def size_max_scc(n: int, m: float) -> Tuple[float, float]:
    """Genera un grafo dirigido aleatorio de parámetros n y m y calcula el tamaño de la mayor SCC.
    Devuelve una tupla con el tamaño normalizado de la mayor SCC y el valor de m."""
    G = erdos_renyi(n, m)
    sccs = G.tarjan()  # Obtiene todas las SCC
    max_scc_size = max(len(scc) for scc in sccs)  # Tamaño de la mayor SCC
    return max_scc_size / n, m  # Tamaño normalizado y m

def edit_distance(str_1: str, str_2: str) -> int:
    n, m = len(str_1), len(str_2)

    # Inicializar dos filas: actual y previa
    prev = list(range(m + 1))
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        curr[0] = i
        for j in range(1, m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                curr[j] = prev[j - 1]  # Sin costo si los caracteres coinciden
            else:
                curr[j] = 1 + min(prev[j],    # Eliminación
                                  curr[j - 1], # Inserción
                                  prev[j - 1]) # Sustitución
        prev, curr = curr, prev  # Intercambiar las filas

    return prev[m]

def max_subsequence_length(str_1: str, str_2: str) -> int:
    n, m = len(str_1), len(str_2)

    # Inicializar dos filas: actual y previa
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                curr[j] = prev[j - 1] + 1  # Carácter coincide
            else:
                curr[j] = max(prev[j], curr[j - 1])  # Tomar el mejor resultado
        prev, curr = curr, prev  # Intercambiar las filas

    return prev[m]

def max_common_subsequence(str_1: str, str_2: str) -> str:
    n, m = len(str_1), len(str_2)

    # Crear matriz completa para la subsecuencia
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Rellenar la matriz
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_1[i - 1] == str_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruir la subsecuencia desde la matriz
    i, j = n, m
    result = []
    while i > 0 and j > 0:
        if str_1[i - 1] == str_2[j - 1]:
            result.append(str_1[i - 1])  # Carácter común
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1  # Subimos
        else:
            j -= 1  # Nos movemos a la izquierda

    return ''.join(reversed(result))

def min_mult_matrix(l_dims: List[int]) -> int:
    """
    Calcula el número mínimo de multiplicaciones necesarias para multiplicar una lista de matrices.
    l_dims: Lista de dimensiones de matrices. Si hay n matrices, entonces l_dims tiene n+1 elementos.
    Devuelve: Mínimo número de operaciones escalares necesarias.
    """
    n = len(l_dims) - 1  # Número de matrices
    
    # Crear una tabla para almacenar los costos mínimos
    dp = [[0] * n for _ in range(n)]
    
    # Llenar dp[i][i] = 0, porque multiplicar una matriz consigo misma no tiene costo
    for i in range(n):
        dp[i][i] = 0

    # Llenar la tabla dp en orden creciente de longitud de subproblema
    for length in range(2, n + 1):  # length es el número de matrices consideradas
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')  # Inicializar con infinito
            # Probar todas las particiones posibles para matrices A[i..j]
            for k in range(i, j):
                cost = (
                    dp[i][k]           # Costo de multiplicar matrices A[i..k]
                    + dp[k + 1][j]     # Costo de multiplicar matrices A[k+1..j]
                    + l_dims[i] * l_dims[k + 1] * l_dims[j + 1]  # Costo de combinar el resultado
                )
                dp[i][j] = min(dp[i][j], cost)

    return dp[0][n - 1]  # El costo mínimo para multiplicar todas las matrices

def grafica ( points , file =' percolation . png ') -> None :
    ''' Genera una grafica en el fichero file '''

    y, x = zip (* points ) # Desempaqueta los points

    fig, ax = plt.subplots (1 , 1, figsize =(6 , 4) )
    ax.scatter (x , y , alpha =0.6 , s =3)
    ax.set_ylabel (f'Tamano normalizado mayor scc ')
    ax.set_xlabel (f'Valor esperado de vecinos por nodo ')
    ax.grid ()
    plt . savefig ( file )
     # plt . show ()

    
### Driver code

if __name__ == '__main__':
    G = read_adjlist('./graph.txt')
    print(G)
    print('Nodes:')
    print(G.nodes())
    print('Adyacentes nodo 5')
    print(G.adj('5'))
    # print('¿Es 2 adyacente de 5?')
    # print(G.exists_edge('5','2'))
    # print('¿Es 3 adyacente de 5?')
    # print(G.exists_edge('5','3'))
    G.dfs()
    print(G.tarjan())
    n = 1000  # Número de nodos en el grafo
    ms = [i * 0.01 for i in range(10, 500)]  # Valores de m de 0.1 a 5.0 en pasos de 0.1
    points = []

    for m in ms:
        scc_size, m_value = size_max_scc(n, m)
        points.append((scc_size, m_value))
        print(f"m = {m_value:.2f}, tamaño normalizado mayor SCC = {scc_size:.4f}")

    grafica(points, 'percolation.png')

    print(edit_distance("kitten", "sitting"))  # Salida: 3
    print(max_subsequence_length("abcde", "ace"))  # Salida: 3
    print(max_common_subsequence("abcde", "ace"))  # Salida: "ace"

    # Dimensiones de matrices: M1 (2x1), M2 (1x3), M3 (3x4)
    l_dims = [2,1,3,4]
    # Calcular el costo mínimo
    print(min_mult_matrix(l_dims))  # Salida: 30000


