import graph_24 as g
import random
from typing import Set, List, Generator, Tuple, KeysView, Iterable
import matplotlib.pyplot as plt

def erdos_renyi(n: int, m: float = 1.) -> g.Graph:
    """Devuelve un grafo aleatorio dirigido basado en el modelo Erdös-Rényi.
    n: número de nodos del grafo.
    m: número medio de vecinos por nodo.
    El número de vecinos se determina con una probabilidad p = m/n. """
    p = m / n  # Probabilidad de conexión
    G = g.Graph()
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
    plt . show ()

if __name__ == '__main__':
    G = g.Graph()
    G. add_edge (0, 1)
    G. add_edge (2, 1)
    G. add_edge (1, 4)
    G. add_edge (4, 3)
    G. add_edge (5, 4)
    G. add_edge (3, 0)
    G. add_edge (5, 2)

    print (G)

    print('Nodes:')
    print(G.nodes())
    print('Adyacentesnodo5')
    print(G.adj(5))
    print('¿Es 2 adyacente de 5?')
    print(G.exists_edge(5,2))
    print('¿Es 3 adyacente de 5?')
    print(G.exists_edge(5,3))

    print (f' DFS forest : {G.dfs ()} ')
    print ()
    print (G)
    print ()
    print (f' scc : {G . tarjan ()} ')

    
    n = 1000  # Número de nodos en el grafo
    ms = [i * 0.01 for i in range(10, 500)]  # Valores de m de 0.1 a 5.0 en pasos de 0.1
    points = []

    for m in ms:
        scc_size, m_value = size_max_scc(n, m)
        points.append((scc_size, m_value))
        print(f"m = {m_value:.2f}, tamaño normalizado mayor SCC = {scc_size:.4f}")

    grafica(points, 'percolation.png')

    print(edit_distance("casa", "calle"))  # Salida: 3
    print(max_subsequence_length("abcde", "ace"))  # Salida: 3
    print(max_common_subsequence("abcde", "ace"))  # Salida: "ace"

    # Dimensiones de matrices: M1 (2x1), M2 (1x3), M3 (3x4)
    l_dims = [2,1,3,4]
    # Calcular el costo mínimo
    print(min_mult_matrix(l_dims))  # Salida: 30000