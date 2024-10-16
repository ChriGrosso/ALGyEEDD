#I.A.1
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

def connected_count(p):
    count=0
    for x in p:
        if x<0:
            count=count+1
    
    return count

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

lst = [ (1, 4), (3, 4), (2, 5)]
s = connected(6, lst)
n = connected_count(s)
ccp = connected_sets(s)
print(ccp)
