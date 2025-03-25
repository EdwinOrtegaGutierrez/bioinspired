import streamlit as st
import numpy as np
from AntColony import ant_colony_optimization

st.title("Ant Colony Optimization")

# Parámetros configurables por el usuario
n_points = st.sidebar.slider("Número de puntos", min_value=5, max_value=20, value=10)
n_ants = st.sidebar.slider("Número de hormigas", min_value=5, max_value=50, value=10)
n_iterations = st.sidebar.slider("Número de iteraciones", min_value=50, max_value=200, value=100)
alpha = st.sidebar.slider("Alpha (influencia de la feromona)", min_value=0.1, max_value=2.0, value=1.0)
beta = st.sidebar.slider("Beta (influencia de la distancia)", min_value=0.1, max_value=2.0, value=1.0)
evaporation_rate = st.sidebar.slider("Tasa de evaporación", min_value=0.1, max_value=1.0, value=0.5)
Q = st.sidebar.slider("Cantidad de feromona (Q)", min_value=0.1, max_value=2.0, value=1.0)

# Generar puntos aleatorios en 3D
points = np.random.rand(n_points, 3)

# Ejecutar el algoritmo de optimización de colonia de hormigas
if st.button("Ejecutar ACO"):
    st.write("Ejecutando el algoritmo de colonia de hormigas...")
    ant_colony_optimization(points, n_ants, n_iterations, alpha, beta, evaporation_rate, Q)