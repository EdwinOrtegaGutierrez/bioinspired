import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def distance(point1, point2):
    """
    Calcula la distancia euclidiana entre dos puntos en un espacio 3D.
    
    Parámetros:
    point1 (numpy array): Coordenadas del primer punto.
    point2 (numpy array): Coordenadas del segundo punto.
    
    Retorna:
    float: Distancia entre los dos puntos.
    """
    return np.sqrt(np.sum((point1 - point2)**2))

def ant_colony_optimization(points, n_ants, n_iterations, alpha, beta, evaporation_rate, Q):
    """
    Implementa el algoritmo de optimización de colonia de hormigas (ACO) para encontrar el camino más corto que visita todos los puntos.
    
    Parámetros:
    points (numpy array): Array de puntos en el espacio 3D.
    n_ants (int): Número de hormigas que explorarán el espacio.
    n_iterations (int): Número de iteraciones del algoritmo.
    alpha (float): Parámetro que controla la influencia de la feromona.
    beta (float): Parámetro que controla la influencia de la distancia.
    evaporation_rate (float): Tasa de evaporación de la feromona.
    Q (float): Cantidad de feromona depositada por las hormigas.
    
    Retorna:
    None: La función muestra un gráfico 3D del mejor camino encontrado y otros caminos explorados.
    """
    n_points = len(points)
    pheromone = np.ones((n_points, n_points))  # Inicializa la matriz de feromonas
    best_path = None
    best_path_length = np.inf  # Inicializa la longitud del mejor camino con infinito
    
    for iteration in range(n_iterations):
        paths = []  # Almacena los caminos de todas las hormigas
        path_lengths = []  # Almacena las longitudes de los caminos de todas las hormigas
        
        for ant in range(n_ants):
            visited = [False]*n_points  # Lista para rastrear los puntos visitados
            current_point = np.random.randint(n_points)  # Punto inicial aleatorio
            visited[current_point] = True
            path = [current_point]  # Inicializa el camino con el punto inicial
            path_length = 0  # Inicializa la longitud del camino
            
            while False in visited:  # Mientras haya puntos no visitados
                unvisited = np.where(np.logical_not(visited))[0]  # Encuentra los puntos no visitados
                probabilities = np.zeros(len(unvisited))  # Inicializa las probabilidades de transición
                
                for i, unvisited_point in enumerate(unvisited):
                    # Calcula la probabilidad de moverse a un punto no visitado
                    probabilities[i] = pheromone[current_point, unvisited_point]**alpha / distance(points[current_point], points[unvisited_point])**beta
                
                probabilities /= np.sum(probabilities)  # Normaliza las probabilidades
                
                next_point = np.random.choice(unvisited, p=probabilities)  # Elige el siguiente punto basado en las probabilidades
                path.append(next_point)  # Añade el punto al camino
                path_length += distance(points[current_point], points[next_point])  # Actualiza la longitud del camino
                visited[next_point] = True  # Marca el punto como visitado
                current_point = next_point  # Actualiza el punto actual
            
            paths.append(path)  # Almacena el camino de la hormiga
            path_lengths.append(path_length)  # Almacena la longitud del camino de la hormiga
            
            if path_length < best_path_length:  # Si este camino es el mejor hasta ahora
                best_path = path  # Actualiza el mejor camino
                best_path_length = path_length  # Actualiza la longitud del mejor camino
        
        pheromone *= evaporation_rate  # Evapora la feromona
        
        for path, path_length in zip(paths, path_lengths):
            for i in range(n_points-1):
                # Deposita feromona en los caminos recorridos por las hormigas
                pheromone[path[i], path[i+1]] += Q/path_length
            pheromone[path[-1], path[0]] += Q/path_length  # Cierra el ciclo
    
    # Visualización del mejor camino encontrado y otros caminos explorados
    fig = plt.figure(figsize=(12, 9))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:,0], points[:,1], points[:,2], c='r', marker='o', label='Puntos')
    
    # Trazar todos los caminos explorados en azul
    for path in paths:
        for i in range(n_points-1):
            ax.plot([points[path[i],0], points[path[i+1],0]],
                    [points[path[i],1], points[path[i+1],1]],
                    [points[path[i],2], points[path[i+1],2]],
                    c='b', linestyle='-', linewidth=0.5, alpha=0.3)
    
    # Trazar las conexiones entre todos los puntos en naranja
    for i in range(n_points):
        for j in range(i+1, n_points):
            ax.plot([points[i,0], points[j,0]],
                    [points[i,1], points[j,1]],
                    [points[i,2], points[j,2]],
                    c='orange', linestyle='--', linewidth=0.2, alpha=0.2)
    
    # Trazar el mejor camino en verde
    for i in range(n_points-1):
        ax.plot([points[best_path[i],0], points[best_path[i+1],0]],
                [points[best_path[i],1], points[best_path[i+1],1]],
                [points[best_path[i],2], points[best_path[i+1],2]],
                c='g', linestyle='-', linewidth=2, marker='o', label='Mejor camino' if i == 0 else "")
        
    ax.plot([points[best_path[0],0], points[best_path[-1],0]],
            [points[best_path[0],1], points[best_path[-1],1]],
            [points[best_path[0],2], points[best_path[-1],2]],
            c='g', linestyle='-', linewidth=2, marker='o')
    
    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')
    plt.legend()
    plt.title(f'Mejor camino encontrado con longitud: {best_path_length:.2f}')
    plt.show()
    
    # Imprimir resultados en la consola
    print(f"Mejor camino encontrado: {best_path}")
    print(f"Longitud del mejor camino: {best_path_length:.2f}")

# Ejemplo de uso
points = np.random.rand(10, 3)  # Genera 10 puntos aleatorios en 3D
ant_colony_optimization(points, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1)