import streamlit as st
from modules.Genetic import genetic_algorithm

st.title("Genetic 🧬")


if st.button('Run Code!'):
    results = genetic_algorithm()
    st.write("Best Solution:", results['best_solution'])
    st.write("Best Fitness:", results['best_fitness'])
    st.pyplot(results['image'])
    #st.write("Convergence History:", results['convergence_history'])