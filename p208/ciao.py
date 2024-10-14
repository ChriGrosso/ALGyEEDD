def connected_sets(p_ds):
    sets = {}
    
    # Para cada nodo, encontramos su raíz y lo añadimos al conjunto correspondiente
    for i in range(len(p_ds)):
        root = ds_find(p_ds, i)
        if root not in sets:
            sets[root] = []
        sets[root].append(i)
    
    # Convertimos el diccionario en una lista de listas
    return list(sets.values())