import numpy as np
import matplotlib.pyplot as plt
import random

def genetic():
    print("Genetic Algorithm (GA)")
    
    # Parámetros del algoritmo
    pop_size = 100          # Tamaño de la población
    crossover_rate = 0.8    # Tasa de cruce
    mutation_rate = 0.1     # Tasa de mutación
    tournament_size = 3     # Tamaño del torneo para selección
    generations = 100       # Número de generaciones
    elitism = 2             # Número de individuos elite que pasan directamente
    
    # Función objetivo para optimizar (ejemplo: minimizar)
    def objective_function(x):
        return np.sum(x**2)  # Función simple para minimizar
    
    # Inicializar población aleatoria
    dim = 5  # Dimensionalidad del problema
    population = np.random.rand(pop_size, dim)
    
    # Arreglos para almacenar el progreso
    best_fitness_history = []
    avg_fitness_history = []
    
    # Función de selección por torneo
    def tournament_selection(population, fitness):
        selected_indices = np.random.choice(len(population), tournament_size)
        selected_fitness = [fitness[i] for i in selected_indices]
        winner_index = selected_indices[np.argmin(selected_fitness)]  # Menor es mejor
        return population[winner_index].copy()
    
    # Operador de cruce - cruce en un punto
    def crossover(parent1, parent2):
        if random.random() < crossover_rate:
            crossover_point = random.randint(1, dim - 1)
            child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
            child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
            return child1, child2
        return parent1.copy(), parent2.copy()
    
    # Operador de mutación
    def mutate(individual):
        for i in range(dim):
            if random.random() < mutation_rate:
                # Añadir un valor aleatorio pequeño
                individual[i] += random.uniform(-0.1, 0.1)
                # Mantener valores en el rango [0, 1]
                individual[i] = max(0, min(1, individual[i]))
        return individual
    
    # Algoritmo principal
    for gen in range(generations):
        # Evaluar fitness de cada individuo
        fitness = np.array([objective_function(ind) for ind in population])
        
        # Ordenar población por fitness (menor es mejor)
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]
        fitness = fitness[sorted_indices]
        
        # Guardar estadísticas
        best_fitness_history.append(fitness[0])
        avg_fitness_history.append(np.mean(fitness))
        
        # Crear nueva población
        new_population = []
        
        # Elitismo: pasar mejores individuos directamente
        new_population.extend(population[:elitism])
        
        # Generar el resto de la población mediante selección, cruce y mutación
        while len(new_population) < pop_size:
            # Selección
            parent1 = tournament_selection(population, fitness)
            parent2 = tournament_selection(population, fitness)
            
            # Cruce
            child1, child2 = crossover(parent1, parent2)
            
            # Mutación
            child1 = mutate(child1)
            child2 = mutate(child2)
            
            # Agregar a la nueva población
            new_population.append(child1)
            if len(new_population) < pop_size:
                new_population.append(child2)
        
        # Actualizar la población
        population = np.array(new_population)
    
    # Evaluar última generación
    fitness = np.array([objective_function(ind) for ind in population])
    best_idx = np.argmin(fitness)
    
    # Mostrar resultados
    best_solution = population[best_idx]
    best_fitness = fitness[best_idx]
    print(f"Mejor solución encontrada: {best_solution}")
    print(f"Mejor fitness: {best_fitness}")
    
    # Graficar convergencia
    plt.figure(figsize=(10, 5))
    plt.plot(best_fitness_history, label='Mejor fitness')
    plt.plot(avg_fitness_history, label='Fitness promedio')
    plt.xlabel('Generación')
    plt.ylabel('Fitness (menor es mejor)')
    plt.title('Convergencia del Algoritmo Genético')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    return best_solution, best_fitness

if __name__ == "__main__":
    genetic()