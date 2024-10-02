import matplotlib.pyplot as plt
import numpy as np
import measure as m

# Lista de tamaños N para medir
Nlst = list(range(10, 10001, 100))

# Medimos el tiempo de ejecución de two_sum
results_ts = m.time_measure(m.two_sum, m.dataprep_ts, Nlst)

# Extraemos los tiempos medios y las varianzas
mean_times_ts = [r[0] for r in results_ts]
var_times_ts = [r[1] for r in results_ts]

# Crear gráfica con matplotlib de two_sum
plt.figure(figsize=(10, 6))
plt.plot(Nlst, mean_times_ts, label='Tiempo medio', color='b')
plt.fill_between(Nlst, 
                 np.array(mean_times_ts) - np.sqrt(var_times_ts), 
                 np.array(mean_times_ts) + np.sqrt(var_times_ts), 
                 color='b', alpha=0.2, label='Varianza')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función two_sum')
plt.legend()
plt.grid(True)

# Guardar la gráfica en two_sum.pdf
plt.savefig('two_sum.pdf')


# Medimos el tiempo de ejecución de itr_bs
results_itrbs = m.time_measure(m.itr_bs, m.dataprep_bs, Nlst)

# Extraemos los tiempos medios y las varianzas
mean_times_itrbs = [r[0] for r in results_itrbs]
var_times_itrbs = [r[1] for r in results_itrbs]

# Crear gráfica con matplotlib de itr_bs
plt.figure(figsize=(10, 6))
plt.plot(Nlst, mean_times_itrbs, label='Tiempo medio', color='b')
plt.fill_between(Nlst, 
                 np.array(mean_times_itrbs) - np.sqrt(var_times_itrbs), 
                 np.array(mean_times_itrbs) + np.sqrt(var_times_itrbs), 
                 color='b', alpha=0.2, label='Varianza')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función itr_bs')
plt.legend()
plt.grid(True)

# Guardar la gráfica en measure.pdf
plt.savefig('itr.pdf')


# Medimos el tiempo de ejecución de itr_bs
results_recbs = m.time_measure(m.rec_bs, m.dataprep_bs, Nlst)

# Extraemos los tiempos medios y las varianzas
mean_times_recbs = [r[0] for r in results_recbs]
var_times_recbs = [r[1] for r in results_recbs]

# Crear gráfica con matplotlib de itr_bs
plt.figure(figsize=(10, 6))
plt.plot(Nlst, mean_times_recbs, label='Tiempo medio', color='b')
plt.fill_between(Nlst, 
                 np.array(mean_times_recbs) - np.sqrt(var_times_recbs), 
                 np.array(mean_times_recbs) + np.sqrt(var_times_recbs), 
                 color='b', alpha=0.2, label='Varianza')

plt.xlabel('Tamaño de la entrada (n)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.title('Tiempo de ejecución de la función rec_bs')
plt.legend()
plt.grid(True)

# Guardar la gráfica en measure.pdf
plt.savefig('rec.pdf')

print("Gráficas guardadas en sus correspondientes pdf")