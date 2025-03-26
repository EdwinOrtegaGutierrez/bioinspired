import numpy as np
import matplotlib.pyplot as plt
import random

def immuneSystems():
    print("Immune Systems - Clonal Selection Algorithm (CLONALG)")
    
    # Parámetros del algoritmo
    pop_size = 100          # Tamaño de la población
    clone_rate = 0.1        # Tasa de clonación
    mutation_rate = 0.1     # Tasa de mutación
    memory_cells = 20       # Número de células de memoria
    generations = 100       # Número de generaciones
    
    # Función objetivo para optimizar (ejemplo: minimizar)
    def objective_function(x):
        return np.sum(x**2)  # Función simple para minimizar
    
    # Inicializar población aleatoria (anticuerpos)
    dim = 5  # Dimensionalidad del problema
    antibodies = np.random.rand(pop_size, dim)
    
    # Arreglos para almacenar el progreso
    best_fitness_history = []
    avg_fitness_history = []
    
    # Algoritmo principal
    for gen in range(generations):
        # Evaluar la afinidad (fitness) de cada anticuerpo
        affinity = np.array([objective_function(ab) for ab in antibodies])
        
        # Ordenar anticuerpos por afinidad (menor es mejor)
        sorted_indices = np.argsort(affinity)
        antibodies = antibodies[sorted_indices]
        affinity = affinity[sorted_indices]
        
        # Guardar estadísticas
        best_fitness_history.append(affinity[0])
        avg_fitness_history.append(np.mean(affinity))
        
        # Seleccionar los mejores para clonar
        n_select = int(pop_size * clone_rate)
        selected = antibodies[:n_select]
        
        # Clonar y mutar (hipermutación) proporcional a la afinidad
        new_pop = []
        for i, ab in enumerate(selected):
            # Número de clones proporcional a la afinidad
            n_clones = int((n_select - i) / n_select * memory_cells) + 1
            
            for _ in range(n_clones):
                clone = ab.copy()
                
                # Mutación inversamente proporcional a la afinidad
                mutation_strength = mutation_rate * (1.0 - i / n_select)
                
                # Aplicar mutación
                clone += np.random.normal(0, mutation_strength, dim)
                
                # Mantener valores en el rango [0, 1]
                clone = np.clip(clone, 0, 1)
                
                new_pop.append(clone)
        
        # Reemplazar la parte inferior de la población con nuevos individuos aleatorios
        n_random = pop_size - len(new_pop)
        if n_random > 0:
            new_random = np.random.rand(n_random, dim)
            antibodies = np.vstack((new_pop, new_random))
        else:
            # Seleccionar los mejores si hay demasiados clones
            antibodies = np.array(new_pop[:pop_size])
    
    # Mostrar resultados
    best_solution = antibodies[0]
    best_fitness = objective_function(best_solution)
    print(f"Mejor solución encontrada: {best_solution}")
    print(f"Mejor fitness: {best_fitness}")
    
    # Graficar convergencia
    plt.figure(figsize=(10, 5))
    plt.plot(best_fitness_history, label='Mejor fitness')
    plt.plot(avg_fitness_history, label='Fitness promedio')
    plt.xlabel('Generación')
    plt.ylabel('Fitness (menor es mejor)')
    plt.title('Convergencia del Algoritmo de Selección Clonal')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return best_solution, best_fitness

if __name__ == "__main__":
    immuneSystems()