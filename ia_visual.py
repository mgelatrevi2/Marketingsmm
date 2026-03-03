import streamlit as st

st.set_page_config(page_title="Adsmarket Neon AI", layout="wide")

# Estilo Neón para la página
st.markdown("""
    <style>
    .main { background-color: #000000; color: #00f2ff; }
    .stButton>button { 
        background-color: #000000; 
        color: #ff00ff; 
        border: 2px solid #ff00ff;
        box-shadow: 0 0 10px #ff00ff;
    }
    h1 { text-shadow: 2px 2px 10px #00f2ff; color: #00f2ff; }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Generador de Webs Adsmarket")
palabra = st.text_input("Ingresá tu palabra mágica (ej: NEON):")

if palabra.upper() == "NEON":
    st.write("### ✅ ¡Página Generada con éxito!")
    st.markdown("""
        <div style="border: 5px solid #ff00ff; padding: 20px; box-shadow: 0 0 20px #00f2ff;">
            <h2 style="color: #00f2ff;">BIENVENIDO A ADSMARKET</h2>
            <p style="color: #ffffff;">Tu sitio web neón está listo para vender.</p>
            <button style="color: #ff00ff; background: black; border: 1px solid #ff00ff;">VER PROYECTO</button>
        </div>
    """, unsafe_allow_html=True)
