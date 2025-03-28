import streamlit as st
from modules.SimulatedAnnealing import simulated_annealing

st.title("Simulated Annealing 🔥")

if st.button('Run Code!'):
    results = simulated_annealing()
    
    st.write("Mejor solución encontrada:")
    bestSolution = {}
    for clase, profesor in results['best_solution'].items():
        bestSolution[clase] = profesor
    st.write(bestSolution)

    st.write("Costo total", results['best_cost'])
    
    st.write("Parámetros utilizados:")
    for param, value in results['algorithm_params'].items():
        st.write(f"* {param}: {value}")
    
    st.pyplot(results['image'])