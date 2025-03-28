import random
import math
import matplotlib.pyplot as plt

def simulated_annealing():
    """Implementación de recocido simulado para asignación de clases que retorna un objeto con resultados"""
    
    # Definición del problema
    problem_data = {
        'profesores': ['Prof1', 'Prof2', 'Prof3', 'Prof4'],
        'aulas': ['Aula1', 'Aula2', 'Aula3', 'Aula4'],
        'clases': ['Clase1', 'Clase2', 'Clase3', 'Clase4']
    }
    
    # Parámetros del algoritmo
    params = {
        'temperatura_inicial': 10000,
        'temperatura_final': 1,
        'tasa_enfriamiento': 0.95,
        'iteraciones_max': 1000,
        'penalizacion_sin_profesor': 10  # Costo por clase sin profesor asignado
    }
    
    # Función de evaluación
    def evaluar_asignacion(asignacion):
        costo = 0
        for clase, profesor in asignacion.items():
            if profesor == "Ninguno":
                costo += params['penalizacion_sin_profesor']
        return costo
    
    # Generar solución inicial
    def generar_solucion_inicial():
        return {clase: random.choice(problem_data['profesores'] + ["Ninguno"]) for clase in problem_data['clases']}
    
    # Historial de convergencia
    history = {
        'temperaturas': [],
        'costos_actuales': [],
        'mejores_costos': [],
        'soluciones_actuales': []
    }
    
    # Algoritmo principal
    solucion_actual = generar_solucion_inicial()
    solucion_mejor = solucion_actual.copy()
    costo_actual = evaluar_asignacion(solucion_actual)
    costo_mejor = costo_actual
    temperatura = params['temperatura_inicial']
    
    for iteracion in range(params['iteraciones_max']):
        # Generar solución vecina
        solucion_vecina = solucion_actual.copy()
        clase_random = random.choice(problem_data['clases'])
        profesor_random = random.choice(problem_data['profesores'] + ["Ninguno"])
        solucion_vecina[clase_random] = profesor_random
        
        costo_vecina = evaluar_asignacion(solucion_vecina)
        
        # Criterio de aceptación
        if costo_vecina < costo_actual or random.random() < math.exp((costo_actual - costo_vecina) / temperatura):
            solucion_actual = solucion_vecina
            costo_actual = costo_vecina
            
            if costo_vecina < costo_mejor:
                solucion_mejor = solucion_vecina.copy()
                costo_mejor = costo_vecina
        
        # Enfriamiento
        temperatura *= params['tasa_enfriamiento']
        
        # Registrar historial
        history['temperaturas'].append(temperatura)
        history['costos_actuales'].append(costo_actual)
        history['mejores_costos'].append(costo_mejor)
        history['soluciones_actuales'].append(solucion_actual.copy())
        
        # Criterio de terminación
        if temperatura < params['temperatura_final']:
            break
    
    # Crear gráfico de convergencia
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico de costos
    ax1.plot(history['costos_actuales'], 'b-', alpha=0.5, label='Costo actual')
    ax1.plot(history['mejores_costos'], 'r-', label='Mejor costo')
    ax1.set_ylabel('Costo')
    ax1.set_title('Convergencia del Recocido Simulado')
    ax1.legend()
    ax1.grid(True)
    
    # Gráfico de temperatura
    ax2.plot(history['temperaturas'], 'g-')
    ax2.set_yscale('log')
    ax2.set_xlabel('Iteración')
    ax2.set_ylabel('Temperatura (log)')
    ax2.grid(True)
    
    plt.tight_layout()
    
    # Retornar objeto con resultados
    return {
        'problem_data': problem_data,
        'algorithm_params': params,
        'best_solution': solucion_mejor,
        'best_cost': costo_mejor,
        'convergence_history': {
            'temperatures': history['temperaturas'],
            'current_costs': history['costos_actuales'],
            'best_costs': history['mejores_costos'],
            'current_solutions': history['soluciones_actuales']
        },
        'image': fig,
        'final_iteration': iteracion + 1
    }
