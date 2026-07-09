import streamlit as st
from data.doctrina import EJES_DOCTRINARIOS, CASO_JURISPRUDENCIAL_DESTACADO

st.set_page_config(page_title="Perspectiva de cátedra", page_icon="🎓", layout="wide")

st.title("🎓 Perspectiva crítica de cátedra")
st.caption(
    "Una lente de lectura adicional al CCyC: la mirada socioeconómica de "
    "la doctrina Weingarten/Ghersi (UBA) sobre la asimetría estructural "
    "del mercado."
)

st.warning(
    "Esta sección resume una corriente DOCTRINARIA (una interpretación "
    "crítica), no el texto de la ley. En un examen, conviene distinguir "
    "claramente cuándo estás citando el CCyC y cuándo estás exponiendo "
    "esta perspectiva de cátedra."
)

st.divider()

for eje in EJES_DOCTRINARIOS:
    with st.expander(f"**{eje['titulo']}**", expanded=False):
        st.write(eje["resumen"])

st.divider()
st.subheader("⚖️ Caso jurisprudencial destacado")
with st.container(border=True):
    st.markdown(f"**{CASO_JURISPRUDENCIAL_DESTACADO['titulo']}**")
    st.write(CASO_JURISPRUDENCIAL_DESTACADO["resumen"])

st.divider()
st.info(
    "💡 Tip para el final: cuando una pregunta pida 'analizar críticamente' "
    "un artículo, una buena estructura es (1) qué dice la norma, (2) qué "
    "objetivo persigue, y (3) qué crítica o matiz le hace la doctrina "
    "(por ejemplo, las de esta sección)."
)
