import streamlit as st
from data.articulos import obtener_todos_los_articulos

st.set_page_config(page_title="Buscador de artículos", page_icon="🔍", layout="wide")

st.title("🔍 Buscador de artículos")
st.caption(
    "Explorá todo el articulado ya desarrollado (Obligaciones, Contratos "
    "en general, Consumo y Contratos en particular) por número, palabra "
    "clave o tema."
)

# 1. Obtenemos los datos con tu función existente
articulos = obtener_todos_los_articulos()

# 2. Extraemos todos los temas (tags) únicos automáticamente para el menú
todos_los_tags = sorted(set(tag for art in articulos for tag in art.get("tags", [])))

# 3. Interfaz de filtros reorganizada
col1, col2 = st.columns(2)
with col1:
    query = st.text_input(
        "Buscar por palabra clave o número",
        placeholder="Ej: '980', 'buena fe', 'imprevisión'...",
    )
with col2:
    # Nuevo filtro interactivo por etiquetas
    tags_seleccionados = st.multiselect("Filtrar por temas", todos_los_tags)

col3, col4, col5 = st.columns([2, 2, 1])
with col3:
    titulos_disponibles = sorted(set(a["titulo_libro"] for a in articulos))
    filtro_titulo = st.selectbox("Filtrar por título", ["Todos"] + titulos_disponibles)
with col4:
    st.write("") # Espaciador invisible para alinear el checkbox
    solo_clave = st.checkbox("⭐ Solo imprescindibles")

# 4. Lógica de filtrado combinada
def coincide(art, q, tags_sel):
    # Validar texto
    q = q.lower().strip()
    coincide_texto = True
    if q:
        campos = [art["num"], art["titulo"], art["resumen"], art["capitulo"]]
        coincide_texto = any(q in str(campo).lower() for campo in campos)
        
    # Validar temas
    coincide_tags = True
    if tags_sel:
        art_tags = art.get("tags", [])
        # Es True si el artículo tiene al menos uno de los temas elegidos
        coincide_tags = any(tag in tags_sel for tag in art_tags)
        
    return coincide_texto and coincide_tags

# Aplicación de los filtros
resultados = [a for a in articulos if coincide(a, query, tags_seleccionados)]

if filtro_titulo != "Todos":
    resultados = [a for a in resultados if a["titulo_libro"] == filtro_titulo]
if solo_clave:
    resultados = [a for a in resultados if a.get("clave")]

# 5. Renderizado
st.markdown(f"**{len(resultados)}** resultado(s) encontrado(s)")
st.divider()

for art in resultados:
    estrella = "⭐ " if art.get("clave") else ""
    with st.container(border=True):
        st.markdown(f"#### {estrella}{art['num']} — {art['titulo']}")
        st.caption(f"{art['capitulo']} · {art['titulo_libro']}")
        st.write(art["resumen"])
        
        # Mejora de UI: st.pills para lectura más fluida
        art_tags = art.get("tags", [])
        if art_tags:
            try:
                st.pills("Temas:", art_tags, key=f"pills_{art['num']}")
            except AttributeError:
                st.caption("Temas: " + " · ".join(f"`{t}`" for t in art_tags))

if not resultados:
    st.info("No se encontraron artículos con ese criterio. Probá con otra palabra clave o quitando filtros.")
