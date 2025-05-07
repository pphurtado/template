import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Dashboard Demo", layout="wide")

# Menú lateral (tipo hamburguesa)
with st.sidebar:
    st.title("Menú")
    seleccion = st.radio("Ir a:", ["Inicio", "Visualización", "Configuración"])
    st.markdown("---")
    st.write("Opciones adicionales")
    if seleccion == "Configuración":
        opcion_extra = st.checkbox("Activar modo avanzado")

# Área principal
st.title("🌐 Dashboard Principal")

if seleccion == "Inicio":
    st.subheader("Bienvenido al Dashboard")
    st.write("Selecciona una opción del menú para comenzar.")

elif seleccion == "Visualización":
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

elif seleccion == "Configuración":
    st.subheader("⚙️ Configuración")
    st.write("Ajusta los parámetros según tus necesidades.")
    if opcion_extra:
        st.success("Modo avanzado activado.")

