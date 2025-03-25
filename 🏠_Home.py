#!/usr/bin/env python3

import streamlit as st

st.title("Bio Inspired")

st.markdown("""
    <h2>Menu</h2>
""", unsafe_allow_html=True)
# Botones con funcionalidad
st.page_link("pages/1_🐜_Ant_Colony.py", label="🐜 Ant Colony", use_container_width=True)

st.page_link("pages/3_🛡️_Immune_Systems.py", label="🛡️ Immune Systems", use_container_width=True)

st.page_link("pages/4_🔥_Simulated_Annealing.py", label="🔥 Simulated Annealing", use_container_width=True)

st.page_link("pages/2_🧬_Genetic.py", label="🧬 Genetic", use_container_width=True)