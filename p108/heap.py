import random
import time

#II.A.1 OK
def heap_heapify(h,i):
    if i >= len(h):
        return h
    small=h[i]
    indx=i
    izq=(2*i)+1 #Indx Hijo Izquierdo
    der=(2*i)+2 #Indx Hijo Derecho
    if izq < len(h) and h[izq]<small:
        small=h[izq]
        indx=izq
    if der < len(h) and h[der]<small:
        small=h[der]
        indx=der
    if indx == i:
        return h
    h[i],h[indx]=h[indx],h[i]
    heap_heapify(h,indx)
    return h

#II.A.2
def heap_insert(h, key):
    h += [key]
    k=len(h)-1
    while k > 0:
        p=int((k-1)/2)
        if h[k] > h[p]:
            return h
        h[k], h[p] = h[p], h[k]
        k=p

#II.A.3 OK
def heap_extract(h):
    u=h[0]
    h[0]=h[-1]
    h=h[:-1]
    h =heap_heapify(h, 0)
    return h,u 

#II.A.3 OK
def heap_create(h):
    for k in range(len(h)-1,-1,-1):
        heap_heapify(h,k)
    return h

#II.B.1
def pq_ini():
    return []

#II.B.2
def pq_insert(h, key):
    heap_insert(h, key)
    return h

def pq_extract(h):
    (h,e)=heap_extract(h)
    return h,e

