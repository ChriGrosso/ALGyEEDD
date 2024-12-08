import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple  # Importar los tipos necesarios
from graph_24 import size_max_scc, erdos_renyi

def compute_confidence_intervals(n: int, m_values: List[float], n_rep: int) -> List[Tuple[float, float, float]]:
    """
    Calcula el tamaño normalizado promedio de la mayor SCC y su intervalo de confianza.
    
    Args:
        n: Número de nodos en el grafo.
        m_values: Lista de valores de m (número promedio de vecinos por nodo).
        n_rep: Número de repeticiones para cada valor de m.
    
    Returns:
        Una lista de tuplas (media, límite inferior, límite superior) para cada m.
    """
    results = []
    for m in m_values:
        sizes = []
        for _ in range(n_rep):
            normalized_size, _ = size_max_scc(n, m)
            sizes.append(normalized_size)
        mean_size = np.mean(sizes)
        std_dev = np.std(sizes)
        # Intervalo de confianza del 95%: media ± 1.96 * sigma
        lower_bound = mean_size - 1.96 * std_dev
        upper_bound = mean_size + 1.96 * std_dev
        results.append((mean_size, lower_bound, upper_bound))
    return results

def plot_with_confidence_intervals(results: List[Tuple[float, float, float]], m_values: List[float], file: str = "confidence_intervals.png"):
    """
    Genera una gráfica con intervalos de confianza para el tamaño de la mayor SCC.
    
    Args:
        results: Lista de resultados (media, límite inferior, límite superior).
        m_values: Valores de m asociados.
        file: Nombre del archivo de salida.
    """
    mean_sizes, lower_bounds, upper_bounds = zip(*results)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.errorbar(m_values, mean_sizes, 
                yerr=[np.array(mean_sizes) - np.array(lower_bounds), 
                      np.array(upper_bounds) - np.array(mean_sizes)],
                fmt='o', ecolor='red', capsize=5, label='Tamaño normalizado mayor SCC')
    ax.set_xlabel("Valor esperado de vecinos por nodo (m)")
    ax.set_ylabel("Tamaño normalizado mayor SCC")
    ax.set_title("Tamaño de la mayor SCC con intervalos de confianza")
    ax.legend()
    ax.grid(True)
    plt.savefig(file)
    plt.show()

# Parámetros
n = 1000  # Número de nodos en el grafo
m_values = np.linspace(0.5, 6, 50)  # Valores de m a analizar
n_rep = 50  # Número de repeticiones para cada m

# Cálculo de intervalos de confianza
confidence_results = compute_confidence_intervals(n, m_values, n_rep)

# Graficar resultados con intervalos
plot_with_confidence_intervals(confidence_results, m_values)
