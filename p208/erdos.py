import random

def erdos_conn(n, m):
    # Inicializamos la lista de arcos
    arcos = []
    
    # Paso i) - Garantizamos la conectividad
    for i in range(1, n):
        # Elegimos un nodo aleatorio entre 0 e i-1
        nodo_aleatorio = random.randint(0, i - 1)
        # Generamos un peso aleatorio entre 0 y 1
        peso = random.uniform(0, 1)
        # Añadimos el arco (i, nodo_aleatorio, peso)
        arcos.append((i, nodo_aleatorio, peso))
    
    # Paso ii) - Añadimos arcos aleatorios adicionales hasta alcanzar n*(m-1)
    total_arcos_adicionales = n * (m - 1) - (n - 1)
    
    # Set para evitar arcos duplicados
    arcos_existentes = set((min(u, v), max(u, v)) for u, v, _ in arcos)
    
    while total_arcos_adicionales > 0:
        # Elegimos dos nodos aleatorios u y v que no estén ya conectados
        u, v = random.sample(range(n), 2)
        u, v = min(u, v), max(u, v)  # Aseguramos que u < v para evitar duplicados inversos
        if (u, v) not in arcos_existentes:
            # Generamos un peso aleatorio entre 0 y 1
            peso = random.uniform(0, 1)
            # Añadimos el arco (u, v, peso)
            arcos.append((u, v, peso))
            arcos_existentes.add((u, v))  # Añadimos al conjunto de arcos ya creados
            total_arcos_adicionales -= 1
    
    return arcos

# Ejemplo de uso
n = 10  # Número de nodos
m = 3   # Promedio de vecinos por nodo
grafo = erdos_conn(n, m)
for arco in grafo:
    print(arco)
