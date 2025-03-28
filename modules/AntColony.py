# Importación de librerías necesarias
import numpy as np  # Para operaciones numéricas
import matplotlib.pyplot as plt  # Para visualización
from mpl_toolkits.mplot3d import Axes3D  # Para gráficos 3D
import streamlit as st  # Para crear la aplicación web

# Función para calcular la distancia euclidiana entre dos puntos
def distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2)**2))

# Algoritmo de Optimización por Colonias de Hormigas (ACO)
def ant_colony_optimization(points, n_ants=10, n_iterations=100, alpha=1, beta=1, 
                          evaporation_rate=0.5, Q=100):
    """
    Parámetros:
    - points: array de coordenadas de los puntos/ciudades a visitar
    - n_ants: número de hormigas en la colonia
    - n_iterations: número de iteraciones del algoritmo
    - alpha: peso de la feromona en la selección de ruta
    - beta: peso de la distancia en la selección de ruta
    - evaporation_rate: tasa de evaporación de feromonas
    - Q: constante para depositar feromonas
    """
    
    n_points = len(points)
    pheromone = np.ones((n_points, n_points))  # Matriz de feromonas inicializada en 1
    best_path = None  # Mejor ruta encontrada
    best_path_length = np.inf  # Longitud de la mejor ruta (inicialmente infinita)
    
    # Bucle principal de iteraciones
    for iteration in range(n_iterations):
        paths = []  # Almacena todas las rutas de esta iteración
        path_lengths = []  # Almacena las longitudes de las rutas
        
        # Cada hormiga construye su ruta
        for ant in range(n_ants):
            visited = [False]*n_points  # Lista de ciudades visitadas
            current_point = np.random.randint(n_points)  # Ciudad inicial aleatoria
            visited[current_point] = True
            path = [current_point]  # Ruta de la hormiga
            path_length = 0  # Longitud acumulada
            
            # Construcción de la ruta hasta visitar todas las ciudades
            while False in visited:
                unvisited = np.where(np.logical_not(visited))[0]  # Ciudades no visitadas
                probabilities = np.zeros(len(unvisited))  # Probabilidades de transición
                
                # Cálculo de probabilidades para cada ciudad no visitada
                for i, unvisited_point in enumerate(unvisited):
                    probabilities[i] = pheromone[current_point, unvisited_point]**alpha / \
                                     distance(points[current_point], points[unvisited_point])**beta
                
                probabilities /= np.sum(probabilities)  # Normalización
                next_point = np.random.choice(unvisited, p=probabilities)  # Selección
                path.append(next_point)
                path_length += distance(points[current_point], points[next_point])
                visited[next_point] = True
                current_point = next_point
            
            # Almacenar ruta y longitud
            paths.append(path)
            path_lengths.append(path_length)
            
            # Actualizar mejor ruta global
            if path_length < best_path_length:
                best_path = path
                best_path_length = path_length
        
        # Evaporación de feromonas
        pheromone *= evaporation_rate
        
        # Deposición de feromonas según calidad de rutas
        for path, path_length in zip(paths, path_lengths):
            for i in range(n_points-1):
                pheromone[path[i], path[i+1]] += Q/path_length
            pheromone[path[-1], path[0]] += Q/path_length  # Volver al inicio
    
    # Visualización de resultados
    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    # Graficar todos los puntos (ciudades)
    ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o', s=50, label='Ciudades')
    
    # Graficar todas las rutas (transparentes)
    for path in paths:
        path_points = points[path]
        ax.plot(path_points[:,0], path_points[:,1], path_points[:,2], 
                'b-', alpha=0.1, linewidth=0.5)
    
    # Graficar la mejor ruta
    best_path_points = points[best_path]
    ax.plot(best_path_points[:,0], best_path_points[:,1], best_path_points[:,2], 
            'g-', linewidth=2, marker='o', markersize=5, label='Mejor Ruta')
    
    # Conectar el final con el inicio
    ax.plot([best_path_points[-1,0], best_path_points[0,0]],
            [best_path_points[-1,1], best_path_points[0,1]],
            [best_path_points[-1,2], best_path_points[0,2]],
            'g-', linewidth=2)
    
    # Configuración del gráfico
    ax.set_xlabel('Coordenada X')
    ax.set_ylabel('Coordenada Y')
    ax.set_zlabel('Coordenada Z')
    plt.title(f'Longitud de la Mejor Ruta: {best_path_length:.2f}')
    plt.legend()
    
    # Retornar resultados
    return {
        "bestWay": [int(x) for x in best_path],  # Mejor ruta encontrada
        "long": best_path_length,  # Longitud de la mejor ruta
        "image": fig  # Objeto de figura para visualización
    }