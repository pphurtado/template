import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboard Demo", layout="wide")

# Menú lateral (tipo hamburguesa)
with st.sidebar:
    st.title("Home")
    seleccion = st.radio("Ir a:", ["Home", "View", "Settings"])
    st.markdown("---")
    st.write("Opciones adicionales")
    if seleccion == "Settings":
        opcion_extra = st.checkbox("Activar modo avanzado")
#Para Cargar Loto
import base64

# Cargar la imagen y convertirla en base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

img_base64 = get_base64_image("DeltaS_Logo_20250510_01.png")

# Insertar la imagen y el título
st.markdown(
    f"""
    <div style='display: flex; align-items: center;'>
        <img src='data:image/png;base64,{img_base64}' width='40' style='margin-right:10px;'/>
        <h1 style='display:inline;'>Dashboard for Statistical Physics</h1>
    </div>
    """,
    unsafe_allow_html=True
)

# Área principal
#st.title("🌐 Dashboard Principal")

if seleccion == "Home":
    st.subheader("Bienvenido al Dashboard")
    st.write("Selecciona una opción del menú para comenzar.")

elif seleccion == "View":
    st.subheader("📊 Visualización de Datos")
    st.write("Aquí podrías insertar un gráfico, tabla o resultado.")
    # Ejemplo con gráfico
    import pandas as pd
    import numpy as np
    import altair as alt

    df = pd.DataFrame({
        "x": range(10),
        "y": np.random.randn(10)
    })
    chart = alt.Chart(df).mark_line().encode(x="x", y="y")
    st.altair_chart(chart, use_container_width=True)

elif seleccion == "Settings":
    st.subheader("⚙️ Settings")
    st.write("Ajusta los parámetros según tus necesidades.")
    if opcion_extra:
        st.success("Modo avanzado activado.")

