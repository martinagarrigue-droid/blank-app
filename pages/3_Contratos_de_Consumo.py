import streamlit as st
from data.articulos import TITULO_III_CONSUMO

st.set_page_config(page_title="Contratos de consumo", page_icon="🛒", layout="wide")

st.title("🛒 Título III – Contratos de consumo")
st.caption(TITULO_III_CONSUMO["rango"])
st.markdown(TITULO_III_CONSUMO["descripcion"])
st.divider()

solo_clave = st.checkbox("⭐ Mostrar solo los puntos 'imprescindibles'")

for cap in TITULO_III_CONSUMO["capitulos"]:
    st.subheader(cap["nombre"])
    st.caption(cap["rango"])

    articulos = cap.get("articulos")
    if articulos:
        for art in articulos:
            if solo_clave and not art.get("clave"):
                continue
            estrella = "⭐ " if art.get("clave") else ""
            with st.expander(f"{estrella}{art['num']} — {art['titulo']}"):
                st.write(art["resumen"])
                if art.get("tags"):
                    st.caption("Temas: " + " · ".join(f"`{t}`" for t in art["tags"]))
    else:
        st.write(cap.get("resumen", ""))

    st.divider()

st.info(
    "🔗 Para leer el texto legal completo, cruzá siempre estos resúmenes "
    "con el CCyC y la Ley 24.240 (Defensa del Consumidor) en InfoLeg/SAIJ."
)
