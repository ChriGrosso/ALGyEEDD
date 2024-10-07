def ds_init(n):
    array = [-1] * n
    return array

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
    
lst = [ (1, 4), (3, 4), (2, 5)]

def connected(n,e):
    i=0
    while i<len(e):
        if(e[i]<0 or e[i]>n):
            return None
        i++