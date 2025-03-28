import streamlit as st
from modules.ImmuneSystems import immune_algorithm


st.title("Immune Systems 🛡️")

if st.button('Run Code!'):
    results = immune_algorithm()
    st.write("Best Solution:", results['best_solution'])
    st.write("Best Fitness:", results['best_fitness'])
    st.pyplot(results['image'])
#    st.write("Convergence History:", results['convergence_history'])