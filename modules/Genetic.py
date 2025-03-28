import numpy as np
import matplotlib.pyplot as plt
import random

def genetic_algorithm():
    """Implementación de un algoritmo genético que retorna resultados en un objeto"""
    
    # Parámetros del algoritmo
    params = {
        'pop_size': 100,          # Tamaño de la población
        'crossover_rate': 0.8,    # Tasa de cruce
        'mutation_rate': 0.1,     # Tasa de mutación
        'tournament_size': 3,     # Tamaño del torneo para selección
        'generations': 100,       # Número de generaciones
        'elitism': 2,             # Número de individuos elite
        'dimension': 5            # Dimensionalidad del problema
    }
    
    # Función objetivo para optimizar (ejemplo: minimizar)
    def objective_function(x):
        return np.sum(x**2)  # Función simple para minimizar
    
    # Inicializar población aleatoria
    population = np.random.rand(params['pop_size'], params['dimension'])
    
    # Historial de convergencia
    history = {
        'best_fitness': [],
        'avg_fitness': [],
        'best_solutions': []
    }
    
    # Función de selección por torneo
    def tournament_selection(population, fitness):
        selected_indices = np.random.choice(len(population), params['tournament_size'])
        selected_fitness = [fitness[i] for i in selected_indices]
        winner_index = selected_indices[np.argmin(selected_fitness)]  # Menor es mejor
        return population[winner_index].copy()
    
    # Operador de cruce - cruce en un punto
    def crossover(parent1, parent2):
        if random.random() < params['crossover_rate']:
            crossover_point = random.randint(1, params['dimension'] - 1)
            child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
            child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
            return child1, child2
        return parent1.copy(), parent2.copy()
    
    # Operador de mutación
    def mutate(individual):
        for i in range(params['dimension']):
            if random.random() < params['mutation_rate']:
                individual[i] += random.uniform(-0.1, 0.1)
                individual[i] = max(0, min(1, individual[i]))  # Mantener en [0, 1]
        return individual
    
    # Algoritmo principal
    for gen in range(params['generations']):
        # Evaluar fitness
        fitness = np.array([objective_function(ind) for ind in population])
        
        # Ordenar población por fitness
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]
        fitness = fitness[sorted_indices]
        
        # Guardar estadísticas
        history['best_fitness'].append(fitness[0])
        history['avg_fitness'].append(np.mean(fitness))
        history['best_solutions'].append(population[0].copy())
        
        # Crear nueva población
        new_population = []
        
        # Elitismo
        new_population.extend(population[:params['elitism']])
        
        # Generar nueva población
        while len(new_population) < params['pop_size']:
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)
            
            child1, child2 = crossover(parent1, parent2)
            
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            new_population.append(child1)
            if len(new_population) < params['pop_size']:
                new_population.append(child2)
        
        population = np.array(new_population)
    
    # Resultados finales
    fitness = np.array([objective_function(ind) for ind in population])
    best_idx = np.argmin(fitness)
    
    # Crear figura de convergencia
    fig = plt.figure(figsize=(10, 5))
    plt.plot(history['best_fitness'], label='Mejor fitness')
    plt.plot(history['avg_fitness'], label='Fitness promedio')
    plt.xlabel('Generación')
    plt.ylabel('Fitness (menor es mejor)')
    plt.title('Convergencia del Algoritmo Genético')
    plt.legend()
    plt.grid(True)
    
    # Retornar objeto con resultados
    return {
        'parameters': params,
        'best_solution': population[best_idx].tolist(),
        'best_fitness': float(fitness[best_idx]),
        'convergence_history': {
            'best_fitness': [float(x) for x in history['best_fitness']],
            'avg_fitness': [float(x) for x in history['avg_fitness']],
            'best_solutions': [x.tolist() for x in history['best_solutions']]
        },
        'image': fig
    }