import streamlit as st
from data.articulos import obtener_todos_los_articulos

st.set_page_config(page_title="Buscador de artículos", page_icon="🔍", layout="wide")

st.title("🔍 Buscador de artículos")
st.caption(
    "Explorá todo el articulado ya desarrollado (Obligaciones, Contratos "
    "en general, Consumo y Contratos en particular) por número, palabra "
    "clave o tema."
)

articulos = obtener_todos_los_articulos()

col1, col2, col3 = st.columns([3, 1.4, 1])
with col1:
    query = st.text_input(
        "Buscar por número de artículo, palabra clave o tema",
        placeholder="Ej: '980', 'buena fe', 'leasing', 'fianza', 'imprevisión'...",
    )
with col2:
    titulos_disponibles = sorted(set(a["titulo_libro"] for a in articulos))
    filtro_titulo = st.selectbox("Filtrar por título", ["Todos"] + titulos_disponibles)
with col3:
    solo_clave = st.checkbox("⭐ Solo imprescindibles")


def coincide(art, q):
    q = q.lower().strip()
    if not q:
        return True
    campos = [
        art["num"],
        art["titulo"],
        art["resumen"],
        art["capitulo"],
        " ".join(art.get("tags", [])),
    ]
    return any(q in str(campo).lower() for campo in campos)


resultados = [a for a in articulos if coincide(a, query)]
if filtro_titulo != "Todos":
    resultados = [a for a in resultados if a["titulo_libro"] == filtro_titulo]
if solo_clave:
    resultados = [a for a in resultados if a.get("clave")]

st.markdown(f"**{len(resultados)}** resultado(s) encontrado(s)")
st.divider()

for art in resultados:
    estrella = "⭐ " if art.get("clave") else ""
    with st.container(border=True):
        st.markdown(f"#### {estrella}{art['num']} — {art['titulo']}")
        st.caption(f"{art['capitulo']} · {art['titulo_libro']}")
        st.write(art["resumen"])
        if art.get("tags"):
            st.caption("Temas: " + " · ".join(f"`{t}`" for t in art["tags"]))

if not resultados:
    st.info("No se encontraron artículos con ese criterio. Probá con otra palabra clave.")
