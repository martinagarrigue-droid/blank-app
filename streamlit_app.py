import streamlit as st

st.set_page_config(
    page_title="Contratos CCyC | Guía interactiva",
    page_icon="⚖️",
    layout="wide",
)

st.title("⚖️ Contratos en el Código Civil y Comercial de la Nación")
st.caption(
    "Guía interactiva de nivel universitario sobre el Libro Tercero "
    "(Derechos Personales) — Obligaciones y Contratos"
)

st.markdown(
    """
Bienvenido/a. Esta aplicación te acompaña en el estudio de la teoría
general de las obligaciones y los contratos en el derecho privado
argentino, con base en el **Código Civil y Comercial de la Nación**
(Ley 26.994 y sus modificaciones — DNU 70/2023, Ley 27.587, entre
otras), la **Ley de Defensa del Consumidor** (24.240) y jurisprudencia
relevante. Incorpora también la **perspectiva crítica de cátedra**
(línea Weingarten/Ghersi, UBA) sobre la asimetría estructural del
mercado.

### ¿Cómo está organizada?
"""
)

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
#### 📚 Contenido teórico
- **🔗 Obligaciones en general** — elementos, clases (dar, hacer, no
  hacer, dar dinero con la reforma del DNU 70/2023), extinción.
- **📚 Contratos en general** — definición, principios (buena fe,
  abuso del derecho, orden público), clasificación, formación,
  efectos, **saneamiento** (evicción y vicios redhibitorios),
  interpretación y extinción — desarrollado artículo por artículo.
- **🛒 Contratos de consumo** — vulnerabilidad estructural, deberes
  del proveedor, modalidades a distancia y electrónicas, cláusulas
  abusivas, daño punitivo.
- **📑 Contratos en particular** — **completo, los 22 tipos**:
  compraventa, permuta, suministro, locación, leasing, obra y
  servicios, transporte, mandato, consignación, corretaje, depósito,
  mutuo y comodato, donación, fianza, renta vitalicia y juego, cesión
  de derechos, transacción, **arbitraje**, fideicomiso, **agencia,
  concesión y franquicia**, y contratos bancarios (con tarjeta de
  crédito).
- **🎓 Perspectiva de cátedra** — la mirada crítica socioeconómica
  (consentimiento vs. asentimiento, órdenes públicos, interés
  positivo/negativo) para argumentar con profundidad en el final.
"""
    )

with col2:
    st.markdown(
        """
#### 🎮 Herramientas interactivas
- **🔍 Buscador de artículos** — explorá TODO el articulado ya
  desarrollado (los 4 títulos) por número, palabra clave o tema.
- **❓ Quiz de autoevaluación** — 18 preguntas comentadas que cubren
  desde formación del contrato hasta leasing, fianza y phishing
  bancario.
- **🧩 Casos prácticos** — 6 casos guiados paso a paso, incluyendo
  cláusulas abusivas, imprevisión, leasing, fianza y responsabilidad
  bancaria por ciberestafas.
"""
    )

st.divider()

st.info(
    "💡 **Cómo usar esta guía:** navegá con el menú de la izquierda. "
    "Cada tema cita el número de artículo correspondiente — usalo "
    "siempre para volver a la fuente oficial (InfoLeg / SAIJ) y "
    "contrastar el texto legal con la explicación pedagógica."
)

st.warning(
    "⚠️ Los resúmenes de esta app son material de estudio con fines "
    "educativos, redactados en lenguaje propio para facilitar la "
    "comprensión. No reemplazan la lectura del texto legal vigente ni "
    "constituyen asesoramiento jurídico."
)

st.divider()
st.subheader("📖 Estructura del Libro Tercero – Derechos Personales")

st.markdown(
    """
| Título | Contenido | Artículos | Estado en la app |
|---|---|---|---|
| **Título I** | Obligaciones en general | 724 a 956 | Desarrollado por tema |
| **Título II** | Contratos en general | 957 a 1091 | Desarrollado completo |
| **Título III** | Contratos de consumo | 1092 a 1122 | Desarrollado completo |
| **Título IV** | Contratos en particular | 1123 a 1881 | ✅ Completo — 22 contratos (222 artículos indexados en total) |
| **Título V** | Otras fuentes de las obligaciones | 1708 a 1881 | Pendiente |
"""
)

st.caption(
    "Fuente estructural: Código Civil y Comercial de la Nación, "
    "Ministerio de Justicia y Derechos Humanos / InfoLeg / SAIJ."
)
