from typing import Set, List, Tuple, KeysView, Iterable
from collections import deque
'''import matplotlib.pyplot as plt'''
import random

class Graph:
    
    def __init__(self):
        self._V = dict()  
        self._E = dict()  
    
    def add_node(self, vertex) -> None:
        ''' Agrega un nodo al grafo si no existe. '''
        if vertex not in self._V:  # Solo agrega si el nodo no está en el grafo
            self._init_node(vertex)
            self._E[vertex] = set()  # Inicializa el conjunto de aristas del nodo
    
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
        
    def _init_node(self, vertex) -> None:
        ''' Inicializa los atributos básicos de un nodo (color, padre, tiempo de descubrimiento y finalización). '''
        self._V[vertex] = {'color': 'WHITE', 'parent': None, 'd_time': None, 'f_time': None}
    
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
                result.append(f"{v}: {{{', '.join(edges)}}}")
        return "\n".join(result)
    
def graph_conjugate(G: Graph) -> Graph:
    """
    Crea el grafo traspuesto del grafo G
    """
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
    """
    Devuelve un grafo aleatorio dirigido basado en el modelo Erdös-Rényi.
    n: número de nodos del grafo.
    m: número medio de vecinos por nodo.
    
    El número de vecinos se determina con una probabilidad p = m/n.
    """
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
    """
    Genera un grafo dirigido aleatorio de parámetros n y m y calcula el tamaño de la mayor SCC.
    Devuelve una tupla con el tamaño normalizado de la mayor SCC y el valor de m.
    """
    G = erdos_renyi(n, m)
    sccs = G.tarjan()  # Obtiene todas las SCC
    max_scc_size = max(len(scc) for scc in sccs)  # Tamaño de la mayor SCC
    return max_scc_size / n, m  # Tamaño normalizado y m


def grafica ( points , file =' percolation . png ') -> None :
    ''' Genera una grafica en el fichero file '''

    y , x = zip (* points ) # Desempaqueta los points

    fig , ax = plt . subplots (1 , 1, figsize =(6 , 4) )
    ax . scatter (x , y , alpha =0.6 , s =3)
    ax . set_ylabel (f'Tamano normalizado mayor scc ')
    ax . set_xlabel (f'Valor esperado de vecinos por nodo ')
    ax . grid ()
    plt . savefig ( file )
     # plt . show ()

def edit_distance(str_1: str, str_2: str) -> int:
    """
    Calcula la distancia de edición entre dos cadenas usando memoria optimizada.
    Se permite insertar, eliminar o sustituir caracteres.
    
    :param str1: Primera cadena
    :param str_2: Segunda cadena
    :return: Distancia de edición mínima entre las dos cadenas
    """
    # Asegurarnos de que str1 sea la cadena más corta para minimizar memoria
    if len(str_1) > len(str_2):
        str_1, str_2 = str_2, str_1
    
    # Longitudes de las cadenas
    len1, len2 = len(str_1), len(str_2)
    
    # Solo necesitamos dos filas: la actual y la previa
    prev_row = list(range(len2 + 1))
    current_row = [0] * (len2 + 1)
    
    # Iterar sobre cada carácter de la primera cadena
    for i in range(1, len1 + 1):
        current_row[0] = i  # Inicializar la primera columna
        for j in range(1, len2 + 1):
            # Si los caracteres coinciden, no hay costo adicional
            cost = 0 if str_1[i - 1] == str_2[j - 1] else 1
            # Calcular el mínimo costo entre: insertar, eliminar o sustituir
            current_row[j] = min(
                current_row[j - 1] + 1,   # Inserción
                prev_row[j] + 1,         # Eliminación
                prev_row[j - 1] + cost   # Sustitución
            )
        # Actualizar la fila previa
        prev_row, current_row = current_row, prev_row
    
    # La distancia de edición está en la última posición de prev_row
    return prev_row[-1]


# Ejemplo de uso
G = Graph()
G.add_edge("0", "1")
G.add_edge("2", "1")
G.add_edge("1", "4")
G.add_edge("4", "3")
G.add_edge("3", "0")
G.add_edge("5", "4")
G.add_edge("5", "2")

print(f"DFS forest: {G.dfs()}")
print()
print(G)
print()
print(f"SCC: {G.tarjan()}")

n = 1000  # Número de nodos en el grafo
ms = [i * 0.1 for i in range(1, 50)]  # Valores de m de 0.1 a 5.0 en pasos de 0.1
points = []

for m in ms:
    scc_size, m_value = size_max_scc(n, m)
    points.append((scc_size, m_value))
    print(f"m = {m_value:.2f}, tamaño normalizado mayor SCC = {scc_size:.4f}")

grafica(points, 'percolation.png')

# Calcular la distancia de edición entre "casa" y "calle"
result = edit_distance("casa", "calle")
print(f"Distancia de edición: {result}")
