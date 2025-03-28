import numpy as np
import matplotlib.pyplot as plt
import random

def immune_algorithm():
    """Implementación del algoritmo de selección clonal que retorna resultados en un objeto"""
    
    # Parámetros del algoritmo
    params = {
        'pop_size': 100,          # Tamaño de la población
        'clone_rate': 0.1,        # Tasa de clonación
        'mutation_rate': 0.1,     # Tasa de mutación base
        'memory_cells': 20,       # Número máximo de células de memoria
        'generations': 100,       # Número de generaciones
        'dimension': 5            # Dimensionalidad del problema
    }
    
    # Función objetivo para optimizar (minimizar)
    def objective_function(x):
        return np.sum(x**2)  # Función esférica
    
    # Inicializar población de anticuerpos
    antibodies = np.random.rand(params['pop_size'], params['dimension'])
    
    # Historial de convergencia
    history = {
        'best_fitness': [],
        'avg_fitness': [],
        'best_solutions': []
    }
    
    # Algoritmo principal
    for gen in range(params['generations']):
        # Evaluar afinidad (fitness)
        affinity = np.array([objective_function(ab) for ab in antibodies])
        
        # Ordenar por afinidad (menor es mejor)
        sorted_indices = np.argsort(affinity)
        antibodies = antibodies[sorted_indices]
        affinity = affinity[sorted_indices]
        
        # Registrar estadísticas
        history['best_fitness'].append(affinity[0])
        history['avg_fitness'].append(np.mean(affinity))
        history['best_solutions'].append(antibodies[0].copy())
        
        # Selección para clonación
        n_select = int(params['pop_size'] * params['clone_rate'])
        selected = antibodies[:n_select]
        
        # Proceso de clonación y mutación
        new_population = []
        for i, ab in enumerate(selected):
            # Número de clones proporcional al ranking
            n_clones = max(1, int((n_select - i) / n_select * params['memory_cells']))
            
            for _ in range(n_clones):
                clone = ab.copy()
                
                # Fuerza de mutación inversamente proporcional al ranking
                mutation_strength = params['mutation_rate'] * (1.0 - i / n_select)
                
                # Aplicar mutación gaussiana
                clone += np.random.normal(0, mutation_strength, params['dimension'])
                clone = np.clip(clone, 0, 1)  # Mantener en rango [0,1]
                
                new_population.append(clone)
        
        # Completar población con nuevos anticuerpos aleatorios
        n_random = params['pop_size'] - len(new_population)
        if n_random > 0:
            new_random = np.random.rand(n_random, params['dimension'])
            antibodies = np.vstack((new_population, new_random))
        else:
            antibodies = np.array(new_population[:params['pop_size']])
    
    # Resultados finales
    final_affinity = np.array([objective_function(ab) for ab in antibodies])
    best_idx = np.argmin(final_affinity)
    
    # Crear figura de convergencia
    fig = plt.figure(figsize=(10, 5))
    plt.plot(history['best_fitness'], label='Mejor fitness')
    plt.plot(history['avg_fitness'], label='Fitness promedio')
    plt.xlabel('Generación')
    plt.ylabel('Fitness (menor es mejor)')
    plt.title('Convergencia del Algoritmo de Selección Clonal')
    plt.legend()
    plt.grid(True)
    
    # Retornar objeto con resultados
    return {
        'parameters': params,
        'best_solution': antibodies[best_idx].tolist(),
        'best_fitness': float(final_affinity[best_idx]),
        'convergence_history': {
            'best_fitness': [float(x) for x in history['best_fitness']],
            'avg_fitness': [float(x) for x in history['avg_fitness']],
            'best_solutions': [x.tolist() for x in history['best_solutions']]
        },
        'image': fig
    }