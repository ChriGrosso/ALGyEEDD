import random
import time

def dataprep(n):
    data = []
    for i in range(n):
        data += [random.randint(0,n)]
    idx = random.randint(0,n-1)
    
    v = max(data) + 1 #¿pq en el anexo le suma +1? para que devuelva un elemento que no está dentro de la lista
    
    return (data, v)

def two_sum(info):
    lista=info[0]
    n=info[1]
    cont1=0
    cont2=1
    long=len(lista)
    
    while cont1!=long and cont2!=long:
        v1=lista[cont1]
        v2=lista[cont2]
        res=v1+v2
        if (res != n) and (cont2 == len(lista)-1):
            cont1+=1
            cont2=cont1+1
        elif res == n:
            return True
        else:
            cont2+=1
    return False

def time_measure(f, dataprep, NList, Nrep, Nstat):
    t1=time.ctime()
    input = dataprep(10)
    res = []
    
lista=dataprep(5)
print(lista)
print(two_sum(lista))

