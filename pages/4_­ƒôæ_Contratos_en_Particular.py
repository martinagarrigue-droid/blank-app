import streamlit as st
from data.articulos import TITULO_IV_PARTICULARES

st.set_page_config(page_title="Contratos en particular", page_icon="📑", layout="wide")

st.title("📑 Título IV – Contratos en particular")
st.caption(f"{TITULO_IV_PARTICULARES['rango']} del CCyC")
st.markdown(TITULO_IV_PARTICULARES["descripcion"])
st.divider()

busqueda = st.text_input("🔎 Filtrar por nombre de contrato (ej: 'leasing', 'fianza', 'transporte')")

capitulos = TITULO_IV_PARTICULARES["capitulos"]
if busqueda:
    capitulos = [c for c in capitulos if busqueda.lower() in c["nombre"].lower()]

desarrollados = [c for c in capitulos if c.get("articulos")]
resumidos = [c for c in capitulos if not c.get("articulos")]

if desarrollados:
    st.markdown("### 📗 Contratos desarrollados en profundidad")
    for cap in desarrollados:
        with st.expander(f"**{cap['nombre']}** · {cap['rango']}", expanded=False):
            for art in cap["articulos"]:
                estrella = "⭐ " if art.get("clave") else ""
                st.markdown(f"**{estrella}{art['num']} — {art['titulo']}**")
                st.write(art["resumen"])
                if art.get("tags"):
                    st.caption("Temas: " + " · ".join(f"`{t}`" for t in art["tags"]))
                st.markdown("---")

if resumidos:
    st.markdown("### 📘 Otros contratos (resumen introductorio)")
    cols = st.columns(2)
    for i, cap in enumerate(resumidos):
        with cols[i % 2]:
            with st.container(border=True):
                st.markdown(f"**{cap['nombre']}**")
                st.caption(cap["rango"])
                st.write(cap["resumen"])

st.divider()
st.success(
    "✅ **Título IV completo:** los 22 tipos contractuales están "
    "desarrollados artículo por artículo (compraventa, locación, "
    "leasing, obra y servicios, transporte, mandato, consignación, "
    "corretaje, depósito, mutuo/comodato, donación, fianza, renta "
    "vitalicia, juego, cesión, transacción, arbitraje, fideicomiso, "
    "agencia/concesión/franquicia y contratos bancarios). Si querés que "
    "profundice algún artículo puntual con más detalle, decime cuál."
)
