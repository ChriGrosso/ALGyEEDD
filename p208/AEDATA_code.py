#I.A.1
import random
import time
import statistics

def ds_init(n):
    array = [-1] * n
    return array

#I.A.2
def ds_union(p_ds, rep_1, rep_2):
    u = ds_find(p_ds, rep_1)
    v = ds_find(p_ds, rep_2)

    if (p_ds[u]<p_ds[v]):
        p_ds[v] = u
    elif (p_ds[v]<p_ds[u]):
        p_ds[u] = v
    else:
        p_ds[v] = u
        p_ds[u] -= 1

#I.A.3
def ds_find(p_ds, m):
    if (m<0 or m>len(p_ds)):
        return None
    else:
        z=m

        while (p_ds[z]>=0):
            z=p_ds[z]
        while (p_ds[m]>=0):
            p_ds[m], m = z, p_ds[m]
        
        return z
    
#Test
lst = [ -1, -1, 0, 0, 1, 4, 1, 4]
print(ds_find(lst, 7))    


#I.B.1
# La funciónn recibe un entero n (el número de nodos del grafo) y una lista de pares de enteros E =[(u1,v1),...,(um,vm)]
# con ui,vi ∈ [0,n). Cada elemento de la lista indica que hay un arco (no dirigido) entre los nodos ui and vi.
# La funcionn ejecutará el algoritmo de componentes conexas y devolverá la estructura de conjuntos disjuntos que
# resulta de la ejecución.
def connected(n,e):
    for n1, n2 in e:
        if n1 > n or n1 <= 0:
            return None
        if n2 > n or n2 <= 0:
            return None
        
    p_ds=ds_init(n)
    for n1, n2 in e: 
        ds_union(p_ds,n1,n2)

    return p_ds

#I.B.2
# La función recibe en entrada la estructura de conjuntos disjuntos resultante de la llamada a connected y
# devuelve el número de componentes conexas del grafo.
def connected_count(p):
    count=0
    for x in p:
        if x<0:
            count=count+1
    
    return count

#I.B.3
# La función recibe en entrada la estructura de conjuntos disjuntos resultante de la llamada a connected y
# devuelve una lista de listas de enteros: cada una de las listas representa una componente conexa del grafo y
# contiene los nodos que forman parte de esa componente conexa.
def connected_sets(p_ds):
    sets = {}
    for i in range(len(p_ds)):
        root = ds_find(p_ds, i)
        if root not in sets:
            sets[root] = []
        sets[root].append(i)
    return list(sets.values())

lst = [ (1, 4), (3, 4), (2, 5)]
s = connected(6, lst)
n = connected_count(s)
ccp = connected_sets(s)
print(ccp)

#II.A.1
# Ejecuta el algoritmo de Kruskal en el grafo. El algoritmo debe devolver un grafo (un árbol, lo recordamos,
# también es un grafo) (n,E′) donde n es el número de nodos (el mismo que en grafo inicial) y E′ es el conjunto de
# arcos que forman el árbol. Si el árbol no existe (es fácil ver que un grafo no conexto no tiene árbol abarcador),
# la función debe devolver None.
def kruskal(n, E):
    E.sort(key=lambda x: x[0])
    p_ds = ds_init(n)
    mst_edges = []
    for  u, v, w in E:
        if ds_find(p_ds, u) != ds_find(p_ds, v):
            ds_union(p_ds, u, v)
            mst_edges.append((u, v, w))
        if len(mst_edges) == n - 1:
            break
    if len(mst_edges) != n - 1:
        return None
    return (n, mst_edges)

#II.A.2
# Dada la lista de arcos producidos por la función kruskal, devuelve el peso del árbol
def k_weight(n, E):
    sum=0
    for (u,v,w) in E:
        sum=sum+w
    return sum

#Test
n = 4
E = [(0, 1, 1),(0, 2, 4),(1, 2, 3),(1, 3, 2),(2, 3, 5)]
n,mst = kruskal(n, E)
print(n, mst)
z=k_weight(n,mst)
print(z)

#II.B.1

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

# Ejemplo de uso
E=erdos_conn(10,2)
#print(E)
#print(kruskal(10,E))

def time_kruskal(n, m, n_graphs):
    tiempos = []
    
    for _ in range(n_graphs):
        grafo=erdos_conn(n,m)
        t_start = time.time()
        kruskal(n,grafo)
        t_end = time.time()
        elapsed_time = (t_end - t_start) * 1000 #Multiplicamos por mil para tenerlo en milisegundos
        tiempos.append(elapsed_time)

    mean_time = round(statistics.mean(tiempos),4)
    var_time = round(statistics.variance(tiempos),4)
    
    return mean_time, var_time, tiempos

print(time_kruskal(1000,50,100))