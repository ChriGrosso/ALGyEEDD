import time
import matplotlib.pyplot as plt
import numpy as np
import random

# I.A.1
def time_measure(f, dataprep, Nlst, Nrep=1000, Nstat=100):
    results = []

    if(f==two_sum):
        for n in Nlst:
            times = []
            for _ in range(Nstat):
                data, target = dataprep(n)  # data es la lista, target es el número objetivo
                t_start = time.time()
                for _ in range(Nrep):
                    f(data, target)  # Llamamos a f pasando dos parámetros
                t_end = time.time()
                elapsed_time = (t_end - t_start) / Nrep
                times.append(elapsed_time)
            
            mean_time = np.mean(times)
            var_time = np.var(times)
            results.append((mean_time, var_time))
        return results
    elif (f==rec_bs or f==itr_bs):
        for n in Nlst:
            times = []
            for _ in range(Nstat):
                data, lft, rgt, target = dataprep(n)  # data es la lista, target es el número objetivo
                t_start = time.time()
                for _ in range(Nrep):
                    f(data, lft, rgt, target)  # Llamamos a f pasando dos parámetros
                t_end = time.time()
                elapsed_time = (t_end - t_start) / Nrep
                times.append(elapsed_time)
            
            mean_time = np.mean(times)
            var_time = np.var(times)
            results.append((mean_time, var_time))
        return results

# I.A.2
def two_sum(lst, target):
    seen = set()
    for num in lst:
        if target - num in seen:
            return True
        seen.add(num)
    return False

# Función para generar datos aleatorios para el two_sum
def dataprep_ts(n):
    return [random.randint(0, n) for _ in range(n)], random.randint(0, 2 * n)

# Función para generar datos aleatorios para las funciones de busqueda binaria
def dataprep_bs(n):
    data = []
    for i in range(n):
        data += [random.randint(0,n)]
    idx = random.randint(0,n-1)
    
    v = max(data) + 1
    lft = 0
    rgt = n-1

    return data, lft, rgt, v

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

# Lista de tamaños N para medir
Nlst = list(range(10, 10001, 100))

# Medimos el tiempo de ejecución
results = time_measure(itr_bs, dataprep_bs, Nlst)

# Extraemos los tiempos medios y las varianzas
mean_times = [r[0] for r in results]
var_times = [r[1] for r in results]

# Crear gráfica con matplotlib de two_sum
plt.figure(figsize=(10, 6))
plt.plot(Nlst, mean_times, label='Tiempo medio', color='b')
plt.fill_between(Nlst, 
                 np.array(mean_times) - np.sqrt(var_times), 
                 np.array(mean_times) + np.sqrt(var_times), 
                 color='b', alpha=0.2, label='Varianza')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función two_sum')
plt.legend()
plt.grid(True)

# Guardar la gráfica en measure.pdf
plt.savefig('two_sum.pdf')

# Crear gráfica con matplotlib de itr_bs
plt.figure(figsize=(10, 6))
plt.plot(Nlst, mean_times, label='Tiempo medio', color='b')
plt.fill_between(Nlst, 
                 np.array(mean_times) - np.sqrt(var_times), 
                 np.array(mean_times) + np.sqrt(var_times), 
                 color='b', alpha=0.2, label='Varianza')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función itr_bs')
plt.legend()
plt.grid(True)

# Guardar la gráfica en measure.pdf
plt.savefig('itr.pdf')

print("Gráfica guardada en measure.pdf")