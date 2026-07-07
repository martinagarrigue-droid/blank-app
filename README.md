# ⚖️ Contratos CCyC — Guía interactiva

App educativa en Streamlit sobre el Libro Tercero (Derechos Personales:
Obligaciones y Contratos) del Código Civil y Comercial de la Nación
argentino, con la perspectiva crítica de cátedra Weingarten/Ghersi (UBA).
Contenido basado en fuentes oficiales (InfoLeg/SAIJ) y doctrina académica.

## 🚀 Cómo correrla en tu Codespace

```bash
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## 📁 Estructura del proyecto

```
streamlit_app.py                    # Página de inicio
pages/
  1_🔗_Obligaciones.py               # Título I, desarrollado por tema
  2_📚_Contratos_en_General.py       # Título II completo (incluye saneamiento)
  3_🛒_Contratos_de_Consumo.py       # Título III completo
  4_📑_Contratos_en_Particular.py    # Título IV: 100% completo (22 contratos)
  5_🎓_Perspectiva_de_Catedra.py     # Doctrina crítica Weingarten/Ghersi
  6_🔍_Buscador_de_Articulos.py      # Buscador sobre TODOS los títulos
  7_❓_Quiz.py                        # 22 preguntas comentadas
  8_🧩_Casos_Practicos.py            # 7 casos guiados paso a paso
data/
  articulos.py     # Contenido de los 4 títulos (222 artículos indexados)
  doctrina.py       # Ejes de la perspectiva de cátedra + jurisprudencia
  quiz_data.py      # Banco de preguntas
  casos_data.py     # Casos prácticos
```

## 📚 Contenido ya desarrollado en profundidad

- **Título I (Obligaciones):** elementos, garantía común, clases de
  obligaciones (dar, hacer, no hacer, dar dinero con la reforma del
  DNU 70/2023), extinción.
- **Título II (Contratos en general):** completo — principios, clasificación,
  formación del consentimiento, tratativas precontractuales, adhesión,
  objeto, causa, forma y prueba, efectos, **saneamiento** (evicción y
  vicios redhibitorios), señal, interpretación, cesión de posición
  contractual, extinción (imprevisión, frustración, lesión).
- **Título III (Consumo):** completo — vulnerabilidad estructural,
  bystander, deberes de seguridad/información/publicidad, modalidades
  a distancia y electrónicas, cláusulas abusivas, daño punitivo.
- **Título IV (Contratos en particular): ✅ COMPLETO — los 22 tipos
  contractuales**, desarrollados artículo por artículo: compraventa
  (con boleto), permuta, suministro, locación (con la reforma del DNU
  70/2023), leasing, obra y servicios (con ruina de obra), transporte,
  mandato, consignación, corretaje, depósito (con hoteles), mutuo y
  comodato, donación (con la Ley 27.587), fianza, renta vitalicia,
  juego, cesión de derechos, transacción, **arbitraje**, fideicomiso,
  **agencia, concesión y franquicia**, y contratos bancarios (con
  tarjeta de crédito y phishing).

## ✍️ Cómo seguir ampliando

Todo el Libro Tercero (Obligaciones y Contratos) tiene ya un desarrollo
sólido. Si en algún momento querés profundizar aún más algún artículo
puntual, agregar más preguntas de quiz o casos prácticos sobre un tema
específico, o sumar contenido de otros libros del Código (por ejemplo,
Derechos Reales o Sucesiones), pedímelo con el mismo formato y lo
integro.

## 🧠 Notas pedagógicas

- Cada artículo indica si es "⭐ imprescindible" para priorizar el
  repaso.
- Los resúmenes están en lenguaje propio (no son transcripción legal)
  — siempre cruzalos con el texto oficial en InfoLeg o SAIJ.
- La sección "Perspectiva de cátedra" resume una corriente doctrinaria
  (Weingarten/Ghersi), no el texto de la ley: útil para argumentar en
  preguntas de análisis crítico, distinguiéndola siempre de la norma.
