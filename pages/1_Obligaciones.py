import streamlit as st
from data.articulos import TITULO_I_OBLIGACIONES

st.set_page_config(page_title="Obligaciones en general", page_icon="🔗", layout="wide")

st.title("🔗 Título I – Obligaciones en general")
st.caption(f"{TITULO_I_OBLIGACIONES['rango']} del CCyC")
st.markdown(TITULO_I_OBLIGACIONES["descripcion"])
st.divider()

for cap in TITULO_I_OBLIGACIONES["capitulos"]:
    st.subheader(cap["nombre"])
    st.caption(cap["rango"])

    articulos = cap.get("articulos")
    if articulos:
        for art in articulos:
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
