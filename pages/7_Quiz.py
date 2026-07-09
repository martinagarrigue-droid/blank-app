import random
import streamlit as st
from data.quiz_data import PREGUNTAS

st.set_page_config(page_title="Quiz de autoevaluación", page_icon="❓", layout="wide")

st.title("❓ Quiz de autoevaluación")
st.caption("Preguntas de opción múltiple sobre Contratos en general, con explicación comentada.")

# --- Estado de sesión -------------------------------------------------
if "quiz_orden" not in st.session_state:
    st.session_state.quiz_orden = list(range(len(PREGUNTAS)))
    random.shuffle(st.session_state.quiz_orden)
if "quiz_respuestas" not in st.session_state:
    st.session_state.quiz_respuestas = {}
if "quiz_confirmadas" not in st.session_state:
    st.session_state.quiz_confirmadas = {}

col_a, col_b = st.columns([1, 5])
with col_a:
    if st.button("🔄 Reiniciar quiz"):
        st.session_state.quiz_orden = list(range(len(PREGUNTAS)))
        random.shuffle(st.session_state.quiz_orden)
        st.session_state.quiz_respuestas = {}
        st.session_state.quiz_confirmadas = {}
        st.rerun()

temas_disponibles = sorted(set(p["tema"] for p in PREGUNTAS))
with col_b:
    temas_filtro = st.multiselect("Filtrar por tema", temas_disponibles)

indices = st.session_state.quiz_orden
preguntas_filtradas = [
    i for i in indices
    if not temas_filtro or PREGUNTAS[i]["tema"] in temas_filtro
]

# --- Puntaje ------------------------------------------------------------
confirmadas = st.session_state.quiz_confirmadas
correctas = sum(
    1 for i in preguntas_filtradas
    if confirmadas.get(PREGUNTAS[i]["id"]) and st.session_state.quiz_respuestas.get(PREGUNTAS[i]["id"]) == PREGUNTAS[i]["correcta"]
)
total_confirmadas = sum(1 for i in preguntas_filtradas if confirmadas.get(PREGUNTAS[i]["id"]))

st.progress(
    total_confirmadas / len(preguntas_filtradas) if preguntas_filtradas else 0,
    text=f"Progreso: {total_confirmadas}/{len(preguntas_filtradas)} respondidas · ✅ {correctas} correctas",
)
st.divider()

for i in preguntas_filtradas:
    p = PREGUNTAS[i]
    st.markdown(f"**[{p['tema']}]** {p['pregunta']}")

    key_radio = f"radio_{p['id']}"
    seleccion = st.radio(
        "Elegí una opción:",
        options=list(range(len(p["opciones"]))),
        format_func=lambda x, p=p: p["opciones"][x],
        key=key_radio,
        index=None,
        label_visibility="collapsed",
    )

    col_conf, col_res = st.columns([1, 4])
    with col_conf:
        if st.button("Confirmar", key=f"btn_{p['id']}", disabled=seleccion is None):
            st.session_state.quiz_respuestas[p["id"]] = seleccion
            st.session_state.quiz_confirmadas[p["id"]] = True
            st.rerun()

    if confirmadas.get(p["id"]):
        resp = st.session_state.quiz_respuestas[p["id"]]
        if resp == p["correcta"]:
            st.success(f"✅ ¡Correcto! {p['explicacion']}")
        else:
            st.error(
                f"❌ Incorrecto. La respuesta correcta era: "
                f"**{p['opciones'][p['correcta']]}**.\n\n{p['explicacion']}"
            )
    st.divider()

if preguntas_filtradas and total_confirmadas == len(preguntas_filtradas):
    porcentaje = round(100 * correctas / len(preguntas_filtradas))
    st.balloons()
    st.subheader(f"🎓 Resultado final: {correctas}/{len(preguntas_filtradas)} ({porcentaje}%)")
