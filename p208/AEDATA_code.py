import random
import time
import statistics
import itertools

# I.A.1 
# Inicializa una estructura con n elementos, cada uno siendo un conjunto separado
def ds_init(n):
    # Creamos un array con n elementos, inicializado en -1 para indicar que cada elemento es su propio conjunto
    array = [-1] * n
    return array

# I.A.2 
# La función hace la unión por rango de los dos conjuntos representados por rep_1 y rep_2 y devuelve el representante del
# conjunto unión.
def ds_union(p_ds, rep_1, rep_2):
    # Encontramos el representante de cada conjunto
    u = ds_find(p_ds, rep_1)
    v = ds_find(p_ds, rep_2)

    # Unión por rango: conectamos el conjunto con menor rango al de mayor rango
    if (p_ds[u]<p_ds[v]):
        p_ds[v] = u
    elif (p_ds[v]<p_ds[u]):
        p_ds[u] = v
    else:
        # Si ambos tienen el mismo rango, eligimos uno ('u') como representante y aumenta su rango
        p_ds[v] = u
        p_ds[u] -= 1

# I.A.3 
# Devuelve el representante del elemento m usando compresión de camino
def ds_find(p_ds, m):
    if (m<0 or m>len(p_ds)):    # Verificar que m esté en el rango 0, ..., n − 1 y devolver None en caso contrario.
        return None
    else:
        # Encontramos el representante del conjunto, aplicando compresión de caminos
        z=m
        while (p_ds[z]>=0):
            z=p_ds[z]
        while (p_ds[m]>=0):
            p_ds[m], m = z, p_ds[m]

        return z

# I.B.1
# La funciónn recibe un entero n (el número de nodos del grafo) y una lista de pares de enteros E =[(u1,v1),...,(um,vm)]
# con ui,vi ∈ [0,n). Cada elemento de la lista indica que hay un arco (no dirigido) entre los nodos ui and vi.
# La funcionn ejecutará el algoritmo de componentes conexas y devolverá la estructura de conjuntos disjuntos que
# resulta de la ejecución.
def connected(n,e):
    # Verificamos que los nodos estén dentro del rango permitido
    for n1, n2 in e:
        if n1 > n or n1 <= 0:
            return None
        if n2 > n or n2 <= 0:
            return None
    
    # Inicializamos la estructura de conjuntos disjuntos
    p_ds=ds_init(n)
    # Unimos los nodos que están conectados por un arco
    for n1, n2 in e: 
        ds_union(p_ds,n1,n2)

    return p_ds

# I.B.2
# La función recibe en entrada la estructura de conjuntos disjuntos resultante de la llamada a connected y
# devuelve el número de componentes conexas del grafo.
def connected_count(p):
    count=0
    # Contamos el número de raíces (elementos con valor negativo) que representan componentes conexas
    for x in p:
        if x<0:
            count=count+1
    
    return count

# I.B.3
# La función recibe en entrada la estructura de conjuntos disjuntos resultante de la llamada a connected y
# devuelve una lista de listas de enteros: cada una de las listas representa una componente conexa del grafo y
# contiene los nodos que forman parte de esa componente conexa.
def connected_sets(p):
    sets = {}
    # Agrupamos nodos bajo su representante raíz
    for i in range(len(p)):
        root = ds_find(p, i)
        if root not in sets:
            sets[root] = []
        sets[root].append(i)
    # Convertimos el diccionario de componentes en una lista de listas
    return list(sets.values())

# II.A.1
# Ejecuta el algoritmo de Kruskal en el grafo. El algoritmo debe devolver un grafo (un árbol, lo recordamos,
# también es un grafo) (n,E′) donde n es el número de nodos (el mismo que en grafo inicial) y E′ es el conjunto de
# arcos que forman el árbol. Si el árbol no existe (es fácil ver que un grafo no conexto no tiene árbol abarcador),
# la función debe devolver None.
def kruskal(n, E):
    # Ordenamos los arcos por peso ascendente
    E.sort(key=lambda x: x[0])
    # Inicializamos la estructura de conjuntos disjuntos y la lista de arcos del árbol de expansión mínima
    p_ds = ds_init(n)
    mst_edges = []
    for  u, v, w in E:
        # Solo agregamos el arco si no conecta dos nodos ya conectados
        if ds_find(p_ds, u) != ds_find(p_ds, v):
            ds_union(p_ds, u, v)
            mst_edges.append((u, v, w))
        # Si ya hemos encontrado n-1 arcos, terminamos
        if len(mst_edges) == n - 1:
            break
    # Verificamos si el árbol de expansión mínima cubre todos los nodos
    if len(mst_edges) != n - 1:
        return None
    return (n, mst_edges)

# II.A.2
# Dada la lista de arcos producidos por la función kruskal, devuelve el peso del árbol
def k_weight(n, E):
    sum=0
    # Sumamos los pesos de los arcos en el árbol de expansión mínima
    for (u,v,w) in E:
        sum=sum+w
    return sum

# II.B.1 Dado los parámetros n y m construye el grafo aleatorio y devuelva la lista de arcos
def erdos_conn(n, m):
    # Inicializamos la estructura DSU y la lista de arcos
    p_ds = ds_init(n)
    arcos = []
    
    # Paso 1: Conectamos nodos para asegurar la conectividad
    for i in range(1, n):
        nodo_conectado = random.randint(0, i - 1)
        peso = round(random.uniform(0, 1),2)
        arcos.append((i, nodo_conectado, peso))
        ds_union(p_ds, i, nodo_conectado)
    
    # Paso 2: Añadimos arcos adicionales secuencialmente
    arcos_existentes = {(min(u, v), max(u, v)) for u, v, _ in arcos}
    arcos_adicionales = n * (m - 1) - 1
    
    while arcos_adicionales>=0:
        # Verificamos que el arco no exista y los nodos no estén conectados
        u=random.randint(0,n-1)
        v=random.randint(0,n-1)
        (u, v)=(min(u, v), max(u, v))
        if (u, v) not in arcos_existentes and u!=v:
            peso = round(random.uniform(0, 1),2)
            arcos.append((u, v, peso))
            arcos_existentes.add((u, v))
            arcos_adicionales -= 1

    return arcos

# II.B.2
# Dados los parametros n y m, construye n_graphs grafos aleatorios de Erdös-Renyi modificados, calcula el tiempo de ejecución
# del algoritmo de Kruskal en cada uno de ellos, y devuelve media y varianza de tal tiempo
def time_kruskal(n, m, n_graphs):
    tiempos = []
    
    # Ejecutamos múltiples veces el algoritmo de Kruskal y medimos el tiempo de cada ejecución
    for _ in range(n_graphs):
        grafo=erdos_conn(n,m)
        t_start = time.time()
        kruskal(n,grafo)
        t_end = time.time()
        elapsed_time = (t_end - t_start) * 1000 #Multiplicamos por mil para tenerlo en milisegundos
        tiempos.append(elapsed_time)

    # Calcula el tiempo promedio y la varianza
    mean_time = round(abs(statistics.mean(tiempos)),4)
    var_time = round(abs(statistics.variance(tiempos)),4)
    
    return mean_time, var_time, tiempos

# Genera una matriz simétrica de distancias aleatorias entre ciudades. La diagonal se establece en cero (distancia a sí misma), 
# y se asegura que mij = mji para mantener la simetría.
def dist_matrix(n_cities, w_max=10):
    # Creamos una matriz de distancias aleatorias
    M = [[random.uniform(0, w_max) for _ in range(n_cities)] for _ in range(n_cities)]
    for k in range(n_cities):
        M[k][k] = 0
        # Aseguramos la simetría de la matriz
        for h in range(k):
            u = (M[k][h] + M[h][k]) / 2.0
            M[h][k] = M[k][h] = u
    return M

# II.A.1
# Recibe una matriz de distancias y un nodo inicial y devuelva un circuito codiciosos como una lista con valores entre 0 y n_cities-1
# y que representa la secuencias de ciudades a recorrer
def greedy_tsp(dist_m, node_ini):
    n_cities = len(dist_m)
    visited = [False] * n_cities    # Se inicializa una lista visited para marcar las ciudades ya visitadas.
    circuit = [node_ini]            # La ciudad inicial (node_ini) se agrega al circuito
    visited[node_ini] = True        # y se marca como visitada
    current_node = node_ini

    # En cada iteración, la función busca la ciudad más cercana que aún no ha sido visitada y se mueve hacia ella, 
    # repitiendo el proceso hasta visitar todas las ciudades.
    for _ in range(n_cities - 1):
        nearest_city = None
        min_distance = float('inf') # float('inf') en Python representa el valor de infinito positivo. 
                                    # Se utiliza para representar un número que es mayor que cualquier otro número finito. 
                                    # Es útil para garantizar que cualquier distancia que encontremos en la matriz será menor 
                                    # que el valor inicial, lo que nos ayuda a identificar la ciudad más cercana correctamente

        # Encontramos la ciudad no visitada más cercana
        for next_city in range(n_cities):
            if not visited[next_city] and dist_m[current_node][next_city] < min_distance:
                nearest_city = next_city
                min_distance = dist_m[current_node][next_city]

        # Nos movemos a la ciudad más cercana encontrada
        circuit.append(nearest_city)
        visited[nearest_city] = True
        current_node = nearest_city

    # Cerramos el circuito volviendo al nodo inicial
    circuit.append(node_ini)
    
    return circuit

# II.A.2
# Recibe un circuito tal como lo ha generado greedy_tsp, una matriz de distancias, y devuelve su longitud.
def len_circuit(circuit, dist_m):
    total_length = 0
    n = len(circuit)
    
    # Sumamos las distancias entre ciudades consecutivas en el circuito
    # Se itera a través del circuito para sumar las distancias entre cada ciudad y la siguiente, usando la matriz dist_m. 
    # Por ejemplo, si el circuito es [0, 2, 1, 3], se suman las distancias de 0 -> 2, 2 -> 1 y 1 -> 3.
    for i in range(n - 1):
        total_length += dist_m[circuit[i]][circuit[i + 1]]
    
    # Añadimos la distancia de regreso desde la última ciudad a la primera
    # Después del bucle, sumamos la distancia entre la última ciudad y la primera ciudad (circuit[-1] -> circuit[0]).
    # Esto cierra el circuito.
    total_length += dist_m[circuit[-1]][circuit[0]]
    
    return total_length

def repeated_greedy_tsp(dist_m):
    n_cities = len(dist_m)
    best_circuit = None
    min_length = float('inf')
    
    # Probamos greedy_tsp comenzando desde cada ciudad
    for start_node in range(n_cities):
        # Generamos un circuito comenzando desde start_node
        circuit = greedy_tsp(dist_m, start_node)
        
        # Calculamos la longitud del circuito
        circuit_length = len_circuit(circuit, dist_m)
        
        # Si encontramos un circuito más corto, actualizamos
        if circuit_length < min_length:
            min_length = circuit_length
            best_circuit = circuit
    
    return best_circuit, min_length


def exhaustive_tsp(dist_m):
    n_cities = len(dist_m)
    best_circuit = None
    min_length = float('inf')
    
    # Generamos todas las permutaciones de las ciudades (0, ..., n_cities - 1)
    for circuit in itertools.permutations(range(n_cities)):
        # Convertimos la permutación a lista y calculamos la longitud del circuito cerrado
        circuit = list(circuit)
        circuit_length = len_circuit(circuit, dist_m)
        
        # Si la longitud del circuito actual es la mínima, actualizamos
        if circuit_length < min_length:
            min_length = circuit_length # Almacenamos la longitud mínima del circuito más corto, inicializada en float('inf')
            best_circuit = circuit      # Guardamos el circuito más corto encontrado
            
    return best_circuit, min_length