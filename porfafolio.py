import streamlit as st

# Configuración inicial de la página
st.set_page_config(page_title="Portafolio - Tu Nombre", layout="wide")

# ----------- SIDEBAR -----------
with st.sidebar:
    st.image("assets/foto.jpg", width=150)
    st.title("Tu Nombre")
    st.markdown("Desarrollador Python 🐍")
    st.markdown("[📫 Email](mailto:tuemail@correo.com)")
    st.markdown("[💼 LinkedIn](https://linkedin.com/in/tu_usuario)")
    st.markdown("[📁 GitHub](https://github.com/tu_usuario)")

# ----------- PRESENTACIÓN -----------
col1, col2 = st.columns([1, 3])

with col1:
    st.image("assets/lucas y franco.jpg", width=200)

with col2:
    st.title("👋 ¡Hola! Soy Tu Nombre")
    st.write("""
    Soy desarrollador backend con experiencia en Python, Django y APIs REST.  
    Me apasiona automatizar tareas, resolver problemas reales con código y construir herramientas útiles para las personas.
    """)
    st.markdown("📍 **Basado en:** Ciudad, País")
    st.markdown("📚 **Habilidades:** Django · FastAPI · PostgreSQL · Pandas · Docker")

# ----------- MÉTRICAS -----------
st.markdown("## 🔢 Métricas Rápidas")
col3, col4, col5 = st.columns(3)

col3.metric("👨‍💻 Años de experiencia", "3+")
col4.metric("📂 Proyectos completados", "12")
col5.metric("🌐 Usuarios impactados", "500+")

# ----------- PROYECTOS -----------
st.markdown("## 🚀 Proyectos Destacados")

proyectos = [
    {
        "titulo": "Clasificador de Imágenes",
        "descripcion": "Red neuronal convolucional con Keras para clasificación de imágenes.",
        "imagen": "assets/barco Mateo.png",
        "link": "https://github.com/tu_usuario/clasificador-imagenes"
    },
    {
        "titulo": "Dashboard de Ventas",
        "descripcion": "Visualización interactiva de datos con Plotly y Streamlit.",
        "imagen": "assets/peñarol.png",
        "link": "https://github.com/tu_usuario/dashboard-ventas"
    },
    {
        "titulo": "Gestor de Tareas API",
        "descripcion": "API REST con Django y JWT para gestión de tareas personales.",
        "imagen": "assets/cerro fc.png",
        "link": "https://github.com/tu_usuario/api-tareas"
    }
]

cols = st.columns(3)

for i, proyecto in enumerate(proyectos):
    with cols[i % 3]:
        st.image(proyecto["imagen"], use_column_width=True)
        st.subheader(proyecto["titulo"])
        st.write(proyecto["descripcion"])
        st.markdown(f"[🔗 Ver en GitHub]({proyecto['link']})")

# ----------- FOOTER -----------
st.markdown("---")
st.markdown("© 2025 - Tu Nombre · Hecho con [Streamlit](https://streamlit.io/)")

