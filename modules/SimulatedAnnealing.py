import random
import math

profesores = ['Prof1', 'Prof2', 'Prof3', 'Prof4']
aulas = ['Aula1', 'Aula2', 'Aula3', 'Aula4']
clases = ['Clase1', 'Clase2', 'Clase3', 'Clase4']

def evaluar_asignacion(asignacion):
    costo = 0
    for clase, profesor in asignacion.items():
        if profesor == "Ninguno":
            costo += 10  
    return costo

def generar_solucion_inicial():
    asignacion = {}
    for clase in clases:
        asignacion[clase] = random.choice(profesores + ["Ninguno"])  
    return asignacion

def recocido_simulado():
    # Parámetros
    temperatura_inicial = 10000
    temperatura_final = 1
    tasa_enfriamiento = 0.95
    iteraciones = 1000

    solucion_actual = generar_solucion_inicial()
    solucion_mejor = solucion_actual
    costo_actual = evaluar_asignacion(solucion_actual)
    costo_mejor = costo_actual
    temperatura = temperatura_inicial

    for _ in range(iteraciones):
        solucion_vecina = solucion_actual.copy()
        clase_random = random.choice(clases)
        profesor_random = random.choice(profesores + ["Ninguno"])
        solucion_vecina[clase_random] = profesor_random

        costo_vecina = evaluar_asignacion(solucion_vecina)

        if costo_vecina < costo_actual or random.random() < math.exp((costo_actual - costo_vecina) / temperatura):
            solucion_actual = solucion_vecina
            costo_actual = costo_vecina

            if costo_vecina < costo_mejor:
                solucion_mejor = solucion_vecina
                costo_mejor = costo_vecina

        temperatura *= tasa_enfriamiento

        if temperatura < temperatura_final:
            break

    return solucion_mejor, costo_mejor

solucion, costo = recocido_simulado()

print("Mejor solución encontrada:")
for clase, profesor in solucion.items():
    print(f"{clase} -> {profesor}")
print(f"Costo total: {costo}")
