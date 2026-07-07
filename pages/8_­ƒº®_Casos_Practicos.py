import streamlit as st
from data.casos_data import CASOS

st.set_page_config(page_title="Casos prácticos", page_icon="🧩", layout="wide")

st.title("🧩 Casos prácticos guiados")
st.caption("Resolvé casos paso a paso, como en un examen o en la práctica profesional.")

nombres = [f"{c['titulo']} · {c['nivel']}" for c in CASOS]
idx = st.selectbox("Elegí un caso:", options=range(len(CASOS)), format_func=lambda i: nombres[i])
caso = CASOS[idx]

state_key = f"caso_{caso['id']}_paso"
if state_key not in st.session_state:
    st.session_state[state_key] = 0

st.subheader(caso["titulo"])
st.caption(f"Nivel: {caso['nivel']}")
with st.container(border=True):
    st.markdown("**📋 Enunciado**")
    st.write(caso["enunciado"])

st.divider()

paso_actual = st.session_state[state_key]
total_pasos = len(caso["pasos"])

if paso_actual < total_pasos:
    st.markdown(f"### Paso {paso_actual + 1} de {total_pasos}")
    p = caso["pasos"][paso_actual]
    st.markdown(f"**{p['pregunta']}**")

    resp_key = f"{caso['id']}_resp_{paso_actual}"
    seleccion = st.radio(
        "Elegí tu respuesta:",
        options=list(range(len(p["opciones"]))),
        format_func=lambda x, p=p: p["opciones"][x],
        key=resp_key,
        index=None,
    )

    confirmado_key = f"{caso['id']}_confirmado_{paso_actual}"
    if confirmado_key not in st.session_state:
        st.session_state[confirmado_key] = False

    if not st.session_state[confirmado_key]:
        if st.button("Confirmar respuesta", disabled=seleccion is None):
            st.session_state[confirmado_key] = True
            st.session_state[f"{caso['id']}_elegida_{paso_actual}"] = seleccion
            st.rerun()
    else:
        elegida = st.session_state[f"{caso['id']}_elegida_{paso_actual}"]
        if elegida == p["correcta"]:
            st.success(f"✅ {p['explicacion']}")
        else:
            st.error(f"❌ {p['explicacion']}")
        if st.button("Siguiente paso ➡️" if paso_actual + 1 < total_pasos else "Ver conclusión 🏁"):
            st.session_state[state_key] += 1
            st.rerun()
else:
    st.success("🏁 **Caso resuelto**")
    with st.container(border=True):
        st.markdown("**💡 Conclusión y repaso de conceptos**")
        st.write(caso["conclusion"])
    if st.button("🔄 Volver a empezar este caso"):
        for k in list(st.session_state.keys()):
            if k.startswith(caso["id"]):
                del st.session_state[k]
        st.session_state[state_key] = 0
        st.rerun()
