import matplotlib.pyplot as plt
import AEDATA_code as aedata
# Genera y grafica los tiempos de ejecución de Kruskal para diferentes tamaños de grafo
def plot_kruskal_times(n_values, m_values, n_graphs=10):
    plt.figure(figsize=(10, 6))
    
    # Realizamos mediciones de tiempo para cada combinación de n y m en n_values y m_values
    for m in m_values:
        mean_times = []
        for n in n_values:
            mean_time, _, _ = aedata.time_kruskal(n, m, n_graphs) # Obtiene el tiempo promedio para cada tamaño de grafo y número de arcos
            mean_times.append(mean_time)
        
        # Graficamos el tiempo promedio para cada n con el valor fijo de m
        plt.plot(n_values, mean_times, marker='o', label=f'm = {m}')
    
    # Configuración de la gráfica
    plt.xlabel("Número de Nodos (n)")
    plt.ylabel("Tiempo de Ejecución Promedio (ms)")
    plt.title("Tiempo de Ejecución de Kruskal en Función del Tamaño del Grafo")
    plt.legend(title="Número de Arcos/Nodo (m)")
    plt.grid()
    
    # Guardamos la gráfica en un archivo PDF
    plt.savefig("AEDATA_time.pdf")
    plt.show()

# Ejecutar la función con ejemplos de valores
n_values = [100, 200, 400, 800, 1600]  # Ejemplo de diferentes tamaños de grafo
m_values = [1, 2, 5, 10]                # Ejemplo de diferentes densidades de arcos por nodo
plot_kruskal_times(n_values, m_values)
