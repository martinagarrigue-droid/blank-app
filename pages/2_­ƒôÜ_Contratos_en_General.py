import streamlit as st
from data.articulos import TITULO_II_CONTRATOS_GENERAL

st.set_page_config(page_title="Contratos en general", page_icon="📚", layout="wide")

st.title("📚 Título II – Contratos en general")
st.caption(f"{TITULO_II_CONTRATOS_GENERAL['rango']} del CCyC")
st.markdown(TITULO_II_CONTRATOS_GENERAL["descripcion"])

st.divider()

nombres_capitulos = [c["nombre"] for c in TITULO_II_CONTRATOS_GENERAL["capitulos"]]
filtro = st.multiselect(
    "Filtrar por capítulo (dejar vacío para ver todo):",
    options=nombres_capitulos,
)

solo_clave = st.checkbox("⭐ Mostrar solo los artículos 'imprescindibles' (clave = True)")

capitulos_a_mostrar = (
    TITULO_II_CONTRATOS_GENERAL["capitulos"]
    if not filtro
    else [c for c in TITULO_II_CONTRATOS_GENERAL["capitulos"] if c["nombre"] in filtro]
)

for cap in capitulos_a_mostrar:
    st.subheader(cap["nombre"])
    st.caption(cap["rango"])

    articulos = cap.get("articulos")
    if articulos:
        for art in articulos:
            if solo_clave and not art.get("clave"):
                continue
            estrella = "⭐ " if art.get("clave") else ""
            with st.expander(f"{estrella}Art. {art['num']} — {art['titulo']}"):
                st.write(art["resumen"])
                if art.get("tags"):
                    st.caption("Temas: " + " · ".join(f"`{t}`" for t in art["tags"]))
    else:
        st.write(cap.get("resumen", ""))

    st.divider()

st.info(
    "🔗 Para leer el texto legal completo de cualquier artículo, buscalo "
    "en el sitio oficial de **InfoLeg** o **SAIJ** con el número exacto "
    "citado en cada tarjeta."
)
