import random
import time
#import matplotlib.pyplot as plt

def dataprep_ts(n):
    data = []
    for i in range(n):
        data += [random.randint(0,n)]
    idx = random.randint(0,n-1)
    
    v = max(data) + 1 #¿pq en el anexo le suma +1? para que devuelva un elemento que no está dentro de la lista
    
    return data, v

def dataprep_bs(n):
    lst = []
    for i in range(n):
        data += [random.randint(0,n)]
    idx = random.randint(0,n-1)
    
    v = max(data) + 1 #¿pq en el anexo le suma +1? para que devuelva un elemento que no está dentro de la lista
    lft = lst[0]
    rgt = lst[n-1]

    return lst, lft, rgt, v

#1.A.2
def two_sum(h,n):
    cont1=0
    cont2=1
    long=len(h)
    
    while cont1!=long and cont2!=long:
        v1=h[cont1]
        v2=h[cont2]
        res=v1+v2
        if (res != n) and (cont2 == len(h)-1):
            cont1+=1
            cont2=cont1+1
        elif res == n:
            return True
        else:
            cont2+=1
    return False

#1.A.1
def time_measure(f, dataprep, NList, Nrep, Nstat):
    res=[]
    if (f == two_sum):
        for n in NList:
            partial=[]
            for s in range(Nstat):
                input1,input2  = dataprep(n)
                t1 = time.time()
                for i in range(Nrep):
                    _ = f(input1,input2)
                t2 = time.time()
                partial += [ float(t2-t1)/float(Nrep) ]
            res += [partial]
            ave = []
            var = []
            worst = []
        for k in range(len(NList)):
            ave += [ sum(res[k])/float(Nstat) ]
            worst += [max(res[k])]
        for k in range(len(NList)):
            var += [ sum([(res[k][u]-ave[k])**2 for u in range(Nstat)])/float(Nstat) ]
        return list(zip(ave, var))
    elif (f==rec_bs or f==itr_bs):
        for n in NList:
            partial=[]
            for s in range(Nstat):
                input1,input2,input3,input4  = dataprep_bs(n)
                t1 = time.time()
                for i in range(Nrep):
                    _ = f(input1,input2,input3,input4)
                t2 = time.time()
                partial += [ float(t2-t1)/float(Nrep) ]
            res += [partial]
            ave = []
            var = []
            worst = []
        for k in range(len(NList)):
            ave += [ sum(res[k])/float(Nstat) ]
            worst += [max(res[k])]
        for k in range(len(NList)):
            var += [ sum([(res[k][u]-ave[k])**2 for u in range(Nstat)])/float(Nstat) ]
        return list(zip(ave, var))


#I.B.1
def rec_bs(lst, lft, rgt, key):
    if lft > rgt:
        return None
    mid = (lft + rgt) // 2
    if lst[mid] == key:
        return mid
    elif key < lst[mid]:
        return rec_bs(lst, lft, mid - 1, key)
    else:
        return rec_bs(lst, mid + 1, rgt, key)

#I.B.2
def itr_bs(lst, lft, rgt, key):
    while lft <= rgt:
        mid = (lft + rgt) // 2
        
        if lst[mid] == key:
            return mid
        elif key < lst[mid]:
            rgt = mid - 1
        else:
            lft = mid + 1
    return None


############
# II. Heap # 
############

#II.A.1
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

#II.A.3
def heap_extract(h):
    u=h[0]
    h[0]=h[-1]
    h=h[:-1]
    h =heap_heapify(h, 0)
    return h,u #ritorno lista modificata e elemento estratto

#II.A.3






#Main
#lista = list(range(10, 10001, 100))
#print(lista)

#print(time_measure(two_sum,dataprep_ts,lista,1000,100))



