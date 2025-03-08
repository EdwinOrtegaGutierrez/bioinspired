#!/usr/bin/env python3

import streamlit as st

st.markdown(
    """
    <style>
    .stButton>button {
        width: 100%;
        background-color: #9F0E5E;
        color: white;
        border: none;
        padding: 10px 24px;
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Estado para controlar la visibilidad del panel lateral
if 'panel_visible' not in st.session_state:
    st.session_state.panel_visible = True

# Mostrar u ocultar el contenido del panel lateral
if st.session_state.panel_visible:
    # Título dentro del panel lateral
    st.sidebar.header("Menu")

    # Botones dentro del panel lateral
    if st.sidebar.button("Ant Colony"):
        st.write("Has presionado el Botón 1")

    if st.sidebar.button("Immune Systems"):
        st.write("Has presionado el Botón 2")

    if st.sidebar.button("Simulated Annealing"):
        st.write("Has presionado el Botón 3")

    if st.sidebar.button("Genetic"):
        st.write("Has presionado el Botón 4")

st.title("Bio Inspired")