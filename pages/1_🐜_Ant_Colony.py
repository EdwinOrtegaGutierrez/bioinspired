import streamlit as st
import numpy as np
from modules.AntColony import ant_colony_optimization


st.title("Ant Colony Optimization 🐜")

if st.button('Run Code!'):
    points = np.random.rand(10, 3)  # Genera 10 puntos aleatorios en 3D
    
    result = ant_colony_optimization(points, n_ants=10, n_iterations=100, alpha=1, beta=1, evaporation_rate=0.5, Q=1)
    
    st.write("Best path found", result['bestWay'])
    st.write("Path length", result['long'])
    st.pyplot(result['image'])