import random
import time

def dataprep_ts(n):
    data = []
    for i in range(n):
        data += [random.randint(0,n)]
    idx = random.randint(0,n-1)
    
    v = max(data) + 1 #¿pq en el anexo le suma +1? para que devuelva un elemento que no está dentro de la lista
    
    return data, v

def two_sum(lst,n):
    cont1=0
    cont2=1
    long=len(lst)
    
    while cont1!=long and cont2!=long:
        v1=lst[cont1]
        v2=lst[cont2]
        res=v1+v2
        if (res != n) and (cont2 == len(lst)-1):
            cont1+=1
            cont2=cont1+1
        elif res == n:
            return True
        else:
            cont2+=1
    return False

def time_measure(f, dataprep_ts, NList, Nrep, Nstat):
    res=[]

    for n in NList:
        partial=[]
        for s in range(Nstat):
            input1,input2  = dataprep_ts(n)
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
    

#Main
lista = list(range(10, 10001, 100))
#print(lista)

#print(time_measure(two_sum,dataprep_ts,lista,2,2))
print(time_measure(two_sum,dataprep_ts,lista,1000,100))



