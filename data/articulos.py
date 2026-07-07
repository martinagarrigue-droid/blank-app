"""
Contenido educativo basado en el Libro Tercero (Derechos Personales) del
Código Civil y Comercial de la Nación (Ley 26.994), incluyendo las
modificaciones introducidas por el DNU 70/2023, la Ley 27.587 (donaciones),
la Ley 25.065 (tarjetas de crédito), la Ley 24.240 (defensa del consumidor)
y leyes complementarias. Incorpora también, en una sección aparte
("doctrina.py"), la perspectiva crítica de la cátedra Weingarten/Ghersi
(UBA) sobre la asimetría estructural del mercado.

IMPORTANTE: Los "resumen" son explicaciones pedagógicas en lenguaje propio,
NO transcripción literal del articulado ni de ningún apunte. Se cita el
número de artículo para que el estudiante pueda ir siempre a la fuente
oficial (InfoLeg / SAIJ) y contrastar.
"""

# ---------------------------------------------------------------------------
# TÍTULO I - OBLIGACIONES EN GENERAL (arts. 724 a 956) - desarrollo por tema
# ---------------------------------------------------------------------------
TITULO_I_OBLIGACIONES = {
    "nombre": "Título I – Obligaciones en general",
    "rango": "arts. 724 a 956",
    "descripcion": (
        "La obligación es el vínculo jurídico por el cual el acreedor tiene "
        "derecho a exigir del deudor una prestación, y ante el incumplimiento, "
        "a obtener forzadamente la satisfacción de su interés. Todo contrato "
        "genera obligaciones: son la 'correa de transmisión' con la que "
        "circulan bienes, servicios y crédito en la economía."
    ),
    "capitulos": [
        {
            "nombre": "Disposiciones generales y elementos",
            "rango": "arts. 724-747",
            "articulos": [
                {
                    "num": "724",
                    "titulo": "Definición",
                    "resumen": (
                        "La obligación es una relación jurídica en virtud de la "
                        "cual el acreedor tiene derecho a exigir del deudor una "
                        "prestación destinada a satisfacer un interés lícito, y "
                        "ante el incumplimiento, a obtener forzadamente la "
                        "satisfacción de dicho interés."
                    ),
                    "clave": True,
                    "tags": ["definición"],
                },
                {
                    "num": "725-728",
                    "titulo": "Requisitos de la prestación",
                    "resumen": (
                        "El objeto de la obligación (la prestación) debe ser "
                        "material y jurídicamente posible, lícito, determinado o "
                        "determinable, susceptible de valoración económica y "
                        "corresponder a un interés patrimonial o extrapatrimonial "
                        "del acreedor."
                    ),
                    "tags": ["objeto de la obligación"],
                },
                {
                    "num": "726",
                    "titulo": "Causa fuente",
                    "resumen": (
                        "No hay obligación sin causa (hecho idóneo para "
                        "producirla, de conformidad con el ordenamiento "
                        "jurídico). Responde a la pregunta '¿por qué se debe?': "
                        "el contrato, el hecho ilícito, la ley o el "
                        "enriquecimiento sin causa son las fuentes típicas."
                    ),
                    "clave": True,
                    "tags": ["causa fuente"],
                },
            ],
        },
        {
            "nombre": "Acciones y garantía común de los acreedores",
            "rango": "arts. 743-745",
            "articulos": [
                {
                    "num": "743",
                    "titulo": "Garantía común",
                    "resumen": (
                        "Los bienes presentes y futuros del deudor constituyen "
                        "la garantía común de sus acreedores. Todos los "
                        "acreedores pueden ejecutar esos bienes en posición "
                        "igualitaria, salvo causas legítimas de preferencia "
                        "(privilegios)."
                    ),
                    "clave": True,
                    "tags": ["garantía común"],
                },
                {
                    "num": "739-742",
                    "titulo": "Acción subrogatoria y acción directa",
                    "resumen": (
                        "Acción subrogatoria: el acreedor ejerce los derechos "
                        "patrimoniales de su deudor inactivo, ingresando lo "
                        "obtenido al patrimonio de este (beneficia a todos sus "
                        "acreedores). Acción directa: en los casos que la ley "
                        "prevé, un acreedor puede reclamar directamente a un "
                        "deudor de su deudor, cobrando para sí mismo (ej. art. "
                        "1216, acción directa del sublocatario)."
                    ),
                    "clave": True,
                    "tags": ["acción subrogatoria", "acción directa"],
                },
            ],
        },
        {
            "nombre": "Clases de obligaciones según el objeto",
            "rango": "arts. 746-772",
            "articulos": [
                {
                    "num": "746-747",
                    "titulo": "Obligaciones de dar cosa cierta",
                    "resumen": (
                        "El deudor debe conservar la cosa en el estado en que "
                        "se encontraba al contraerse la obligación, y entregarla "
                        "con sus accesorios en tiempo y lugar convenidos. "
                        "Ejemplo típico: la entrega de maquinaria con "
                        "especificaciones técnicas en una cadena de suministro "
                        "industrial."
                    ),
                    "tags": ["obligación de dar", "cosa cierta"],
                },
                {
                    "num": "759-760",
                    "titulo": "Obligación de dar para restituir",
                    "resumen": (
                        "Cuando la obligación de dar tiene por objeto la "
                        "restitución de la cosa a su dueño (por ejemplo, al "
                        "finalizar una locación, un leasing o un comodato), el "
                        "deudor la detenta como simple tenedor y debe "
                        "devolverla al vencer el plazo o cumplirse la "
                        "condición."
                    ),
                    "tags": ["restitución", "tenencia precaria"],
                },
                {
                    "num": "765",
                    "titulo": "Obligaciones de dar dinero (texto reformado por el DNU 70/2023)",
                    "resumen": (
                        "Hay obligación de dar dinero cuando el deudor debe "
                        "cierta cantidad de moneda, sea o no de curso legal en "
                        "el país. Bajo el texto ORIGINAL de 2015, si se pactaba "
                        "pagar en moneda extranjera, el deudor podía liberarse "
                        "dando el equivalente en pesos (obligación facultativa). "
                        "El DNU 70/2023 (arts. 250-251) cambió esto de raíz: "
                        "ahora el deudor SOLO se libera entregando la moneda "
                        "exactamente pactada, y los jueces NO PUEDEN modificar "
                        "la moneda ni la forma de pago convenidas."
                    ),
                    "clave": True,
                    "tags": ["obligación dineraria", "DNU 70/2023", "moneda extranjera"],
                },
                {
                    "num": "766",
                    "titulo": "Obligación del deudor (reformado)",
                    "resumen": (
                        "El deudor debe entregar la cantidad correspondiente de "
                        "la especie designada, tenga o no curso legal en el "
                        "país. Es el correlato del nuevo art. 765: refuerza el "
                        "principio nominalista y la intangibilidad de la moneda "
                        "pactada."
                    ),
                    "tags": ["obligación dineraria", "DNU 70/2023"],
                },
                {
                    "num": "772",
                    "titulo": "Obligaciones de valor",
                    "resumen": (
                        "Su objeto no es una suma de dinero sino un valor "
                        "abstracto o una utilidad (por ejemplo, la reparación "
                        "integral de un daño). Esa deuda de valor recién se "
                        "traduce a una suma de dinero al momento del pago, lo "
                        "que protege al acreedor de la licuación inflacionaria."
                    ),
                    "clave": True,
                    "tags": ["obligación de valor", "inflación"],
                },
            ],
        },
        {
            "nombre": "Obligaciones de hacer y de no hacer",
            "rango": "arts. 773-778",
            "articulos": [
                {
                    "num": "773",
                    "titulo": "Obligación de hacer",
                    "resumen": (
                        "Tiene por objeto la prestación de un servicio o la "
                        "realización de un hecho, en el tiempo, lugar y modo "
                        "acordados."
                    ),
                    "tags": ["obligación de hacer"],
                },
                {
                    "num": "774",
                    "titulo": "Prestación de servicios: medios, resultado y resultado eficaz",
                    "resumen": (
                        "El Código distingue tres grados de compromiso del "
                        "prestador: (a) desplegar una actividad con diligencia "
                        "apropiada, sin garantizar el éxito (obligación de "
                        "MEDIOS: ej. abogado defensor, médico clínico); (b) "
                        "procurar un resultado concreto con independencia de su "
                        "eficacia (ej. presentar un escrito o un balance en "
                        "término); (c) procurar el resultado EFICAZ prometido "
                        "(obligación de RESULTADO/garantía: ej. cirujano "
                        "estético, constructora, transportista). En esta "
                        "última, la responsabilidad es objetiva y solo se exime "
                        "con caso fortuito o culpa de la víctima."
                    ),
                    "clave": True,
                    "tags": ["obligación de medios", "obligación de resultado"],
                },
                {
                    "num": "778",
                    "titulo": "Obligación de no hacer",
                    "resumen": (
                        "El deudor se compromete a una abstención específica "
                        "(tolerar o no hacer algo que lícitamente podría hacer). "
                        "Ejemplos económicos: cláusulas de no competencia, "
                        "acuerdos de confidencialidad, exclusividad territorial "
                        "en franquicias."
                    ),
                    "tags": ["obligación de no hacer"],
                },
            ],
        },
        {
            "nombre": "Extinción de las obligaciones",
            "rango": "arts. 865-935",
            "articulos": [
                {
                    "num": "865",
                    "titulo": "Pago",
                    "resumen": (
                        "Es el cumplimiento de la prestación que constituye el "
                        "objeto de la obligación: el modo normal y querido de "
                        "extinción."
                    ),
                    "tags": ["pago"],
                },
                {
                    "num": "varios",
                    "titulo": "Modos anormales de extinción",
                    "resumen": (
                        "Novación (se reemplaza la obligación por otra nueva), "
                        "compensación (cuando dos personas son recíprocamente "
                        "acreedoras y deudoras), confusión (la calidad de "
                        "acreedor y deudor se reúnen en una misma persona), "
                        "renuncia y remisión de deuda (el acreedor abandona su "
                        "derecho) e imposibilidad de cumplimiento sobrevenida, "
                        "objetiva y absoluta, no imputable al deudor."
                    ),
                    "tags": ["novación", "compensación", "confusión", "remisión"],
                },
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# TÍTULO II - CONTRATOS EN GENERAL (arts. 957 a 1091) - DESARROLLO COMPLETO
# ---------------------------------------------------------------------------
TITULO_II_CONTRATOS_GENERAL = {
    "nombre": "Título II – Contratos en general",
    "rango": "arts. 957 a 1091",
    "descripcion": (
        "El núcleo de la teoría general del contrato: qué es, cómo se "
        "clasifica, cómo se forma, qué efectos produce, cómo se sanea y cómo "
        "se extingue."
    ),
    "capitulos": [
        {
            "nombre": "Capítulo 1 – Disposiciones generales",
            "rango": "arts. 957-964",
            "articulos": [
                {
                    "num": "957",
                    "titulo": "Definición de contrato",
                    "resumen": (
                        "El contrato es el acto jurídico bilateral (o "
                        "plurilateral) por el cual dos o más partes "
                        "manifiestan su consentimiento para crear, regular, "
                        "modificar, transferir o extinguir relaciones "
                        "jurídicas patrimoniales. Tres notas clave: (1) "
                        "requiere pluralidad de partes con voluntades "
                        "coincidentes; (2) el objeto son relaciones "
                        "jurídicas *patrimoniales*; (3) es la principal fuente "
                        "de obligaciones. La cátedra Weingarten/Ghersi advierte "
                        "que esta definición presupone un modelo de "
                        "'consentimiento' paritario que hoy solo describe una "
                        "porción minoritaria del tráfico real (ver sección "
                        "'Perspectiva de cátedra')."
                    ),
                    "clave": True,
                    "tags": ["definición", "elementos"],
                },
                {
                    "num": "958",
                    "titulo": "Libertad de contratación",
                    "resumen": (
                        "Las partes son libres para celebrar un contrato y "
                        "determinar su contenido, dentro de los límites "
                        "impuestos por la ley, el orden público, la moral y "
                        "las buenas costumbres."
                    ),
                    "clave": True,
                    "tags": ["autonomía de la voluntad", "límites"],
                },
                {
                    "num": "959",
                    "titulo": "Efecto vinculante (pacta sunt servanda)",
                    "resumen": (
                        "Todo contrato válidamente celebrado es obligatorio "
                        "para las partes. Solo puede ser modificado o "
                        "extinguido por acuerdo de partes o en los supuestos "
                        "que la ley autoriza (imprevisión, resolución por "
                        "incumplimiento, nulidad de cláusulas abusivas, etc.)."
                    ),
                    "clave": True,
                    "tags": ["fuerza obligatoria", "pacta sunt servanda"],
                },
                {
                    "num": "961",
                    "titulo": "Buena fe",
                    "resumen": (
                        "Los contratos deben celebrarse, interpretarse y "
                        "ejecutarse de buena fe, obligando a todo lo que "
                        "razonablemente se deriva de ellos. Se distingue la "
                        "buena fe SUBJETIVA (creencia/confianza) de la buena fe "
                        "OBJETIVA (lealtad, probidad, cooperación activa entre "
                        "las partes)."
                    ),
                    "clave": True,
                    "tags": ["buena fe", "principio general"],
                },
                {
                    "num": "962-964",
                    "titulo": "Normas supletorias, prelación e integración",
                    "resumen": (
                        "Las normas legales sobre contratos son, salvo que "
                        "digan lo contrario, supletorias de la voluntad de las "
                        "partes. Frente a concurrencia de normas del Código y "
                        "de leyes especiales, el orden de prelación es: normas "
                        "indisponibles > cláusulas particulares del contrato > "
                        "normas supletorias de la ley especial > normas "
                        "supletorias del Código. El contrato se integra además "
                        "con los usos y prácticas razonables del lugar."
                    ),
                    "tags": ["normas supletorias", "prelación normativa"],
                },
            ],
        },
        {
            "nombre": "Capítulo 1 bis – Principios generales del derecho contractual",
            "rango": "arts. 9 a 12 (Título Preliminar)",
            "articulos": [
                {
                    "num": "9",
                    "titulo": "Principio de buena fe",
                    "resumen": (
                        "Norma general del Título Preliminar: los derechos "
                        "deben ejercerse de buena fe. Se proyecta al derecho "
                        "contractual en el art. 961 (celebración, "
                        "interpretación y ejecución de buena fe)."
                    ),
                    "clave": True,
                    "tags": ["buena fe", "principios generales"],
                },
                {
                    "num": "10",
                    "titulo": "Ejercicio abusivo del derecho",
                    "resumen": (
                        "La ley no ampara el ejercicio abusivo de los derechos: "
                        "aquel que contraría los fines que la ley tuvo en mira "
                        "al reconocerlos, o que excede los límites de la buena "
                        "fe, la moral y las buenas costumbres. Ejemplo: usar "
                        "una cláusula de resolución formalmente lícita para "
                        "asfixiar económicamente a la contraparte o forzar "
                        "renegociaciones. El juez puede ordenar el cese del "
                        "abuso y fijar indemnización."
                    ),
                    "clave": True,
                    "tags": ["abuso del derecho"],
                },
                {
                    "num": "11",
                    "titulo": "Abuso de posición dominante",
                    "resumen": (
                        "Lo dispuesto para el abuso de derecho se aplica "
                        "también cuando se abusa de una posición dominante en "
                        "el mercado. Ocupar una posición dominante no es "
                        "ilícito en sí mismo (puede derivar de eficiencia o "
                        "innovación); lo que se sanciona es el ABUSO de esa "
                        "posición: cláusulas leoninas, precios predatorios o "
                        "excesivos impuestos unilateralmente, barreras a la "
                        "competencia."
                    ),
                    "clave": True,
                    "tags": ["posición dominante", "mercado"],
                },
                {
                    "num": "12",
                    "titulo": "Orden público",
                    "resumen": (
                        "Las convenciones particulares no pueden dejar sin "
                        "efecto las leyes en cuya observancia está interesado "
                        "el orden público. La cátedra distingue tres funciones "
                        "del orden público: (1) DE COORDINACIÓN (concepción "
                        "liberal clásica: solo controla la licitud genérica de "
                        "lo pactado entre partes iguales); (2) DE DIRECCIÓN "
                        "(el Estado orienta la macroeconomía: control de "
                        "cambios, tarifas de servicios públicos, retenciones); "
                        "(3) DE PROTECCIÓN (pilar del derecho del consumo: "
                        "tutela imperativa e irrenunciable de la parte débil, "
                        "expurgando cláusulas abusivas bajo el principio in "
                        "dubio pro consumidor)."
                    ),
                    "clave": True,
                    "tags": ["orden público"],
                },
            ],
        },
        {
            "nombre": "Capítulo 2 – Clasificación de los contratos",
            "rango": "arts. 966-970",
            "articulos": [
                {
                    "num": "966",
                    "titulo": "Unilaterales y bilaterales",
                    "resumen": (
                        "Bilaterales: ambas partes se obligan recíproca y "
                        "correlativamente (compraventa). Unilaterales: solo "
                        "una parte se obliga (donación sin cargo). No debe "
                        "confundirse con 'acto jurídico unilateral' (como el "
                        "testamento): el contrato SIEMPRE es un acto jurídico "
                        "bilateral porque exige el acuerdo de dos voluntades "
                        "para formarse, aunque las obligaciones que genere "
                        "pesen sobre una sola parte. De la bilateralidad "
                        "derivan institutos exclusivos: suspensión del "
                        "cumplimiento (art. 1031), tutela preventiva (art. "
                        "1032) y resolución por incumplimiento (arts. "
                        "1083-1089)."
                    ),
                    "clave": True,
                    "tags": ["clasificación"],
                },
                {
                    "num": "967",
                    "titulo": "Oneroso y gratuito",
                    "resumen": (
                        "Oneroso: las ventajas que procura una parte le son "
                        "concedidas por una prestación que ella hizo o se "
                        "obliga a hacer (compraventa, locación). Gratuito: una "
                        "parte procura una ventaja a la otra sin recibir "
                        "contraprestación (donación, comodato). La distinción "
                        "tiene efectos prácticos concretos: garantías de "
                        "saneamiento (solo en onerosos), acción por lesión "
                        "(solo en onerosos), reglas de interpretación distintas "
                        "(arts. 1068) y régimen de la acción de fraude a "
                        "acreedores (más gravoso para actos gratuitos)."
                    ),
                    "clave": True,
                    "tags": ["clasificación"],
                },
                {
                    "num": "968",
                    "titulo": "Conmutativo y aleatorio",
                    "resumen": (
                        "Oneroso conmutativo: las ventajas para las partes son "
                        "ciertas (compraventa). Oneroso aleatorio: dependen de "
                        "un acontecimiento incierto (seguro, renta vitalicia, "
                        "juego)."
                    ),
                    "tags": ["clasificación"],
                },
                {
                    "num": "969-970",
                    "titulo": "Formal / nominado e innominado",
                    "resumen": (
                        "Formales: la ley exige una forma determinada, con "
                        "distintos grados de rigor (solemne absoluta, solemne "
                        "relativa, para prueba). Nominados: tienen regulación "
                        "legal específica; innominados o atípicos: carecen de "
                        "ella y se rigen por la voluntad de las partes, las "
                        "normas generales de contratos, los usos y los "
                        "contratos afines."
                    ),
                    "tags": ["forma", "atipicidad"],
                },
            ],
        },
        {
            "nombre": "Capítulo 3 – Formación del consentimiento",
            "rango": "arts. 971-983",
            "articulos": [
                {
                    "num": "971",
                    "titulo": "Formación del consentimiento",
                    "resumen": (
                        "El contrato se concluye con la recepción de la "
                        "aceptación de una oferta, o por una conducta de las "
                        "partes que sea suficiente para demostrar la "
                        "existencia de un acuerdo."
                    ),
                    "clave": True,
                    "tags": ["consentimiento", "formación"],
                },
                {
                    "num": "972",
                    "titulo": "Oferta",
                    "resumen": (
                        "Manifestación dirigida a persona determinada o "
                        "determinable, con intención de obligarse y con las "
                        "precisiones necesarias para establecer los efectos "
                        "que debe producir de ser aceptada."
                    ),
                    "clave": True,
                    "tags": ["oferta"],
                },
                {
                    "num": "973",
                    "titulo": "Invitación a ofertar (y su crítica en el derecho de consumo)",
                    "resumen": (
                        "La oferta dirigida a personas indeterminadas se "
                        "considera invitación a ofertar, salvo que de sus "
                        "términos resulte la intención de contratar. Crítica "
                        "de la cátedra: este artículo, pensado para el "
                        "contrato paritario, resulta inaplicable en las "
                        "relaciones de consumo. Allí, la publicidad masiva "
                        "constituye una OFERTA VINCULANTE al público (art. 7 "
                        "Ley 24.240 y art. 1103 CCyC): si el proveedor "
                        "publicita un producto, queda obligado por esos "
                        "términos."
                    ),
                    "clave": True,
                    "tags": ["oferta", "invitación a ofertar", "consumo"],
                },
                {
                    "num": "974-976",
                    "titulo": "Fuerza obligatoria, retractación y caducidad de la oferta",
                    "resumen": (
                        "La oferta obliga al proponente, salvo retractación "
                        "eficaz (recibida antes o junto con la oferta), plazo "
                        "de caducidad, o muerte/incapacidad del oferente o "
                        "destinatario antes de la aceptación."
                    ),
                    "tags": ["oferta", "retractación", "caducidad"],
                },
                {
                    "num": "978",
                    "titulo": "Aceptación",
                    "resumen": (
                        "Debe expresar plena conformidad con la oferta. "
                        "Cualquier modificación introducida por el aceptante "
                        "no vale como aceptación, sino como propuesta de un "
                        "nuevo contrato (contraoferta): el sistema exige "
                        "congruencia total, no tolera aceptaciones parciales."
                    ),
                    "clave": True,
                    "tags": ["aceptación"],
                },
                {
                    "num": "980-981",
                    "titulo": "Perfeccionamiento (teoría de la recepción) y retractación de la aceptación",
                    "resumen": (
                        "Entre presentes, el contrato se perfecciona al "
                        "manifestarse la aceptación; entre ausentes, cuando es "
                        "recibida por el proponente durante la vigencia de la "
                        "oferta (teoría de la recepción, no de la expedición "
                        "ni del conocimiento). La aceptación puede retractarse "
                        "si la retractación se recibe antes o junto con ella."
                    ),
                    "clave": True,
                    "tags": ["perfeccionamiento", "teoría de la recepción"],
                },
                {
                    "num": "982-983",
                    "titulo": "Acuerdos parciales y teoría de la recepción",
                    "resumen": (
                        "Los acuerdos parciales concluyen el contrato si todas "
                        "las partes acuerdan sobre los elementos esenciales "
                        "particulares. La doctrina de la cátedra advierte un "
                        "riesgo: en la práctica, la parte fuerte puede usar "
                        "esta figura para 'atar' contractualmente al débil "
                        "antes de que comprenda la totalidad del negocio; por "
                        "eso, en caso de duda, el contrato se tiene por NO "
                        "concluido. La manifestación de voluntad se considera "
                        "'recibida' cuando el destinatario la conoce o debió "
                        "conocerla (art. 983)."
                    ),
                    "tags": ["formación", "acuerdo parcial"],
                },
            ],
        },
        {
            "nombre": "Capítulo 4 – Tratativas contractuales",
            "rango": "arts. 990-993",
            "articulos": [
                {
                    "num": "990",
                    "titulo": "Libertad de negociación",
                    "resumen": (
                        "Las partes son libres para promover tratativas y "
                        "para abandonarlas en cualquier momento, siempre "
                        "respetando el principio de buena fe."
                    ),
                    "clave": True,
                    "tags": ["precontractual", "buena fe"],
                },
                {
                    "num": "991",
                    "titulo": "Deber de buena fe en las tratativas",
                    "resumen": (
                        "Durante las tratativas las partes deben obrar de "
                        "buena fe para no frustrarlas injustificadamente. "
                        "Quien las frustra arbitrariamente responde por el "
                        "daño al interés negativo (los gastos en que incurrió "
                        "la otra parte confiando en el negocio), no por el "
                        "cumplimiento del contrato que nunca se celebró."
                    ),
                    "clave": True,
                    "tags": ["responsabilidad precontractual"],
                },
                {
                    "num": "992",
                    "titulo": "Deber de confidencialidad",
                    "resumen": (
                        "Si una parte accede a información secreta o reservada "
                        "de la otra durante las negociaciones (por ejemplo, en "
                        "un due diligence), tiene el deber de no revelarla ni "
                        "usarla en su propio beneficio, aun si el negocio no "
                        "se concreta."
                    ),
                    "tags": ["confidencialidad"],
                },
                {
                    "num": "993",
                    "titulo": "Cartas de intención",
                    "resumen": (
                        "Documentos donde las partes expresan su voluntad de "
                        "negociar sobre ciertas bases. Se interpretan "
                        "restrictivamente: no constituyen oferta vinculante, "
                        "salvo pacto en contrario."
                    ),
                    "tags": ["cartas de intención"],
                },
            ],
        },
        {
            "nombre": "Capítulo 5 – Contratos preliminares y por adhesión",
            "rango": "arts. 984-999",
            "articulos": [
                {
                    "num": "994",
                    "titulo": "Promesa de contrato: plazo máximo",
                    "resumen": (
                        "El contrato preliminar debe contener el núcleo de los "
                        "elementos esenciales del contrato definitivo. Rige un "
                        "plazo de caducidad de 1 año (o el menor pactado), "
                        "renovable. Es un tope de orden público pensado para "
                        "evitar 'cautiverios negociales' que traben la "
                        "circulación de la riqueza, aunque la doctrina discute "
                        "si resulta demasiado breve para negocios complejos "
                        "(megaobras, fideicomisos)."
                    ),
                    "tags": ["contrato preliminar"],
                },
                {
                    "num": "996",
                    "titulo": "Contrato de opción",
                    "resumen": (
                        "El otorgante queda ligado a su declaración de "
                        "voluntad, y el optante tiene el derecho potestativo "
                        "de concluir el contrato definitivo con la sola "
                        "notificación, sin que el otorgante pueda retractarse."
                    ),
                    "tags": ["contrato de opción"],
                },
                {
                    "num": "997-999",
                    "titulo": "Pacto de preferencia y contrato sujeto a conformidad",
                    "resumen": (
                        "Pacto de preferencia: si el obligado decide "
                        "transferir un bien, debe dar prioridad al titular del "
                        "pacto en igualdad de condiciones. Contrato sujeto a "
                        "conformidad: su eficacia depende de una autorización "
                        "o aprobación posterior (venta 'a ensayo', aprobación "
                        "de una asamblea)."
                    ),
                    "tags": ["pacto de preferencia"],
                },
                {
                    "num": "984-989",
                    "titulo": "Contratos por adhesión a cláusulas generales predispuestas",
                    "resumen": (
                        "Aquellos en los que una parte adhiere a cláusulas "
                        "redactadas unilateralmente por la otra (o un "
                        "tercero), sin haber participado en su redacción "
                        "(art. 984). Requisitos: cláusulas claras, completas y "
                        "autosuficientes; las que remiten a textos no "
                        "entregados se tienen por no convenidas (art. 985). "
                        "Las cláusulas particulares negociadas prevalecen "
                        "sobre las generales (art. 986). Interpretación contra "
                        "el predisponente en caso de ambigüedad (art. 987, "
                        "regla contra proferentem). Son abusivas (arts. "
                        "988-989) las cláusulas que desnaturalizan las "
                        "obligaciones del predisponente, importan renuncia o "
                        "restricción de derechos del adherente, o no son "
                        "razonablemente previsibles: se tienen por no "
                        "escritas, y el juez integra el contrato si puede "
                        "subsistir sin ellas."
                    ),
                    "clave": True,
                    "tags": ["adhesión", "cláusulas abusivas"],
                },
            ],
        },
        {
            "nombre": "Capítulo 6 – Objeto del contrato",
            "rango": "arts. 1003-1011",
            "articulos": [
                {
                    "num": "1003-1004",
                    "titulo": "Requisitos del objeto",
                    "resumen": (
                        "El objeto debe ser lícito, posible, determinado o "
                        "determinable, y susceptible de valoración económica. "
                        "No pueden ser objeto los hechos imposibles o "
                        "prohibidos, ni lo que afecte la dignidad humana. La "
                        "doctrina distingue tres 'estratos': el objeto del "
                        "CONTRATO (la operación jurídica integral, ej. la "
                        "'cuenta corriente bancaria' como sistema), el efecto "
                        "del contrato (el plexo de obligaciones que genera) y "
                        "el objeto de la OBLIGACIÓN (la prestación concreta: "
                        "dar, hacer o no hacer)."
                    ),
                    "clave": True,
                    "tags": ["objeto"],
                },
                {
                    "num": "1007-1011",
                    "titulo": "Bienes futuros y determinación por tercero",
                    "resumen": (
                        "Los bienes futuros pueden ser objeto de los "
                        "contratos. Cuando el objeto se refiere a bienes "
                        "indeterminados al momento de contratar, el contrato "
                        "es válido si su determinación se deja al arbitrio de "
                        "un tercero."
                    ),
                    "tags": ["objeto", "bienes futuros"],
                },
            ],
        },
        {
            "nombre": "Capítulo 7 – Causa",
            "rango": "arts. 281-283 y 1012-1014",
            "articulos": [
                {
                    "num": "281",
                    "titulo": "Causa fin",
                    "resumen": (
                        "Responde a '¿para qué se contrata?'. Es el fin "
                        "inmediato autorizado por el ordenamiento jurídico que "
                        "determinó la voluntad de las partes, sumado a los "
                        "motivos exteriorizados cuando son lícitos, esenciales "
                        "y compartidos por la contraparte. Tiene una dimensión "
                        "OBJETIVA (la función económico-social típica de cada "
                        "contrato) y una SUBJETIVA (los móviles particulares "
                        "de esas partes en ese caso concreto)."
                    ),
                    "clave": True,
                    "tags": ["causa fin"],
                },
                {
                    "num": "282-283",
                    "titulo": "Presunción de causa y acto abstracto",
                    "resumen": (
                        "Se presume que la causa existe y es lícita aunque no "
                        "esté expresada. El acto abstracto (títulos valores, "
                        "cheques) opera con independencia de su causa para dar "
                        "celeridad al crédito, pero la discusión causal puede "
                        "renacer en las acciones de regreso."
                    ),
                    "tags": ["causa", "acto abstracto"],
                },
                {
                    "num": "1013-1014",
                    "titulo": "Necesidad de causa y causa ilícita",
                    "resumen": (
                        "La causa debe existir al momento de la formación del "
                        "contrato y subsistir durante su ejecución. El "
                        "contrato es nulo si su causa es contraria a la moral, "
                        "al orden público o a las buenas costumbres, o si "
                        "ambas partes lo concluyeron por un motivo ilícito "
                        "común."
                    ),
                    "tags": ["causa ilícita", "nulidad"],
                },
                {
                    "num": "1090",
                    "titulo": "Frustración de la finalidad (remisión)",
                    "resumen": (
                        "La consagración de la causa subjetiva alcanza su "
                        "máxima expresión en esta figura: ver capítulo 15 "
                        "(extinción)."
                    ),
                    "tags": ["frustración del fin"],
                },
            ],
        },
        {
            "nombre": "Capítulo 8 – Forma y prueba",
            "rango": "arts. 1015-1020",
            "articulos": [
                {
                    "num": "1015",
                    "titulo": "Libertad de formas",
                    "resumen": (
                        "Solo son formales los contratos a los que la ley les "
                        "impone una forma determinada. Es el principio "
                        "general, orientado a agilizar el tráfico."
                    ),
                    "clave": True,
                    "tags": ["forma"],
                },
                {
                    "num": "1016-1017",
                    "titulo": "Paralelismo de formas y escritura pública",
                    "resumen": (
                        "Toda modificación de un contrato formal debe hacerse "
                        "con la misma solemnidad (paralelismo de formas). "
                        "Deben otorgarse por escritura pública, entre otros: "
                        "los contratos sobre derechos reales de inmuebles, la "
                        "división de cosa común y las donaciones de "
                        "inmuebles."
                    ),
                    "tags": ["forma", "escritura pública"],
                },
                {
                    "num": "1018",
                    "titulo": "Conversión del negocio jurídico (forma ad probationem)",
                    "resumen": (
                        "Cuando la forma exigida es solo para producir "
                        "determinados efectos (no ad solemnitatem), la "
                        "omisión no anula el contrato: vale como un contrato "
                        "distinto por el cual las partes se obligan a "
                        "otorgar la formalidad pendiente (ej. el boleto de "
                        "compraventa inmobiliaria obliga a escriturar)."
                    ),
                    "clave": True,
                    "tags": ["forma", "conversión"],
                },
                {
                    "num": "1019-1020",
                    "titulo": "Medios de prueba",
                    "resumen": (
                        "Los contratos pueden probarse por todos los medios "
                        "aptos, valorados según la sana crítica. Los que sea "
                        "de uso instrumentar por escrito no pueden probarse "
                        "solo por testigos, salvo principio de prueba por "
                        "escrito o imposibilidad de obtenerlo. En el comercio "
                        "electrónico, la Ley 25.506 distingue FIRMA DIGITAL "
                        "(presunción de autoría; quien la impugna carga con la "
                        "prueba) de FIRMA ELECTRÓNICA (sin esa presunción; "
                        "quien la invoca debe probar su autoría) — y en "
                        "consumo, el art. 53 LDC traslada la carga probatoria "
                        "dinámica al proveedor, que controla los servidores."
                    ),
                    "tags": ["prueba", "firma digital"],
                },
            ],
        },
        {
            "nombre": "Capítulo 9 – Efectos del contrato",
            "rango": "arts. 1021-1032",
            "articulos": [
                {
                    "num": "1021",
                    "titulo": "Regla general (efecto relativo)",
                    "resumen": (
                        "El contrato solo tiene efecto entre las partes; no lo "
                        "tiene respecto de terceros, salvo excepciones legales "
                        "(estipulación a favor de tercero, sucesores "
                        "universales). Es la traducción del adagio romano res "
                        "inter alios acta."
                    ),
                    "clave": True,
                    "tags": ["efecto relativo"],
                },
                {
                    "num": "1022-1024",
                    "titulo": "Situación de terceros y sucesores universales",
                    "resumen": (
                        "El contrato no genera obligaciones a cargo de "
                        "terceros ni ellos pueden invocarlo para imponer "
                        "obligaciones a las partes. Sin embargo, el tercero "
                        "debe respetar el derecho ajeno nacido del contrato "
                        "(deber general de no dañar); si lo lesiona con dolo o "
                        "culpa, responde por responsabilidad civil aquiliana. "
                        "Los efectos se extienden a los sucesores universales, "
                        "salvo que la obligación sea intuitu personae o esté "
                        "prohibida su transmisión."
                    ),
                    "tags": ["efecto relativo", "sucesores"],
                },
                {
                    "num": "1025-1030",
                    "titulo": "Incorporación de terceros al contrato",
                    "resumen": (
                        "El Código regula varias figuras: contratación a "
                        "nombre de tercero (ineficaz hasta que este ratifique, "
                        "con efecto retroactivo); promesa del hecho de tercero "
                        "(obligación de medios o de resultado según lo "
                        "prometido); estipulación a favor de tercero (el "
                        "beneficiario adquiere un derecho directo al aceptar, "
                        "clave en seguros de vida y fideicomisos); contrato "
                        "para persona a designar (se reserva nominar a un "
                        "tercero que ocupará la posición, típico en "
                        "compraventas 'en comisión'); y contrato por cuenta de "
                        "quien corresponda (el destinatario final se "
                        "determinará después, común en mercaderías en "
                        "tránsito)."
                    ),
                    "tags": ["terceros", "estipulación a favor de tercero"],
                },
                {
                    "num": "1073-1075",
                    "titulo": "Contratos conexos: la crisis del efecto relativo",
                    "resumen": (
                        "En redes de contratos vinculados por una finalidad "
                        "económica común (ej. compraventa de un auto "
                        "financiada por una entidad asociada a la "
                        "concesionaria), el Código admite que los efectos, "
                        "vicios e incumplimientos de un contrato de la red "
                        "puedan expandirse a los demás eslabones, superando el "
                        "efecto relativo clásico y evitando que las empresas "
                        "'atomicen' su responsabilidad frente al consumidor."
                    ),
                    "clave": True,
                    "tags": ["contratos conexos", "conexidad"],
                },
                {
                    "num": "1031",
                    "titulo": "Suspensión del cumplimiento (exceptio non adimpleti contractus)",
                    "resumen": (
                        "En contratos bilaterales, una parte puede suspender "
                        "el cumplimiento de su propia prestación hasta que la "
                        "otra cumpla u ofrezca cumplir la suya, salvo que deba "
                        "cumplir primero según lo pactado o la ley."
                    ),
                    "clave": True,
                    "tags": ["excepción de incumplimiento"],
                },
                {
                    "num": "1032",
                    "titulo": "Tutela preventiva",
                    "resumen": (
                        "Una parte puede suspender su propio cumplimiento, aun "
                        "si es exigible, si los derechos de la otra sufren una "
                        "amenaza grave de daño por un menoscabo significativo "
                        "en su solvencia o aptitud de cumplir (ej. apertura de "
                        "concurso de la contraparte). La suspensión cede si la "
                        "otra parte cumple o da garantías suficientes."
                    ),
                    "clave": True,
                    "tags": ["tutela preventiva"],
                },
            ],
        },
        {
            "nombre": "Capítulo 10 – Obligación de saneamiento (evicción y vicios redhibitorios)",
            "rango": "arts. 1033-1058",
            "articulos": [
                {
                    "num": "1033-1034",
                    "titulo": "Obligación de saneamiento: sujetos obligados",
                    "resumen": (
                        "Protege que el equilibrio pactado se mantenga en la "
                        "ejecución del contrato. Están obligados al "
                        "saneamiento: el transmitente a título oneroso, quien "
                        "ha dividido bienes con otros (particiones, "
                        "condominios) y los antecesores en la cadena de "
                        "transmisiones onerosas. Si la operación es de "
                        "consumo, el art. 13 LDC impone responsabilidad "
                        "objetiva y solidaria a toda la cadena de "
                        "comercialización."
                    ),
                    "clave": True,
                    "tags": ["saneamiento"],
                },
                {
                    "num": "1039-1040",
                    "titulo": "Opciones del acreedor y responsabilidad por daños",
                    "resumen": (
                        "Ante evicción o vicio, el adquirente puede: (a) "
                        "reclamar el saneamiento del título o la subsanación "
                        "del vicio; (b) reclamar un bien equivalente (cosas "
                        "fungibles); (c) declarar la resolución del contrato "
                        "(improcedente si el defecto es subsanable y el "
                        "garante ofrece reparación oportuna). Además, puede "
                        "reclamar los daños, salvo eximentes (el adquirente "
                        "conocía el riesgo, transmisión a su propio riesgo, o "
                        "venta en subasta judicial)."
                    ),
                    "tags": ["saneamiento", "opciones del acreedor"],
                },
                {
                    "num": "1043",
                    "titulo": "Límites a las cláusulas de dispensa",
                    "resumen": (
                        "El garante no puede excusarse alegando su ignorancia "
                        "o error. Las cláusulas que dispensan o limitan la "
                        "responsabilidad por saneamiento se interpretan "
                        "restrictivamente, y se tienen por no convenidas si el "
                        "enajenante actuó con dolo, o si es profesional frente "
                        "a un adquirente profano. En consumo, esa nulidad es "
                        "absoluta."
                    ),
                    "clave": True,
                    "tags": ["saneamiento", "cláusulas de dispensa"],
                },
                {
                    "num": "1044-1050",
                    "titulo": "Garantía de evicción",
                    "resumen": (
                        "La evicción es la privación o turbación, total o "
                        "parcial, del derecho transmitido a título oneroso, "
                        "por una causa de fecha anterior o contemporánea a la "
                        "adquisición (reclamos de terceros, de propiedad "
                        "intelectual, o turbaciones de hecho del propio "
                        "transmitente). El adquirente debe citar por evicción "
                        "al enajenante en el juicio que promueva un tercero; "
                        "si no lo hace (o se allana o va a arbitraje sin su "
                        "conformidad), pierde la garantía."
                    ),
                    "clave": True,
                    "tags": ["evicción"],
                },
                {
                    "num": "1051-1058",
                    "titulo": "Vicios redhibitorios",
                    "resumen": (
                        "Son defectos materiales ocultos que hacen a la cosa "
                        "impropia para su destino, o disminuyen su utilidad de "
                        "tal modo que, de haberlos conocido, el adquirente no "
                        "la habría adquirido o habría pagado un precio menor. "
                        "No hay garantía si el defecto era ostensible o "
                        "surgió después de la adquisición. Plazos de "
                        "caducidad: 3 años para inmuebles, 6 meses para "
                        "muebles, desde la recepción; denuncia dentro de los "
                        "60 días de conocido el vicio; prescripción de la "
                        "acción: 1 año."
                    ),
                    "clave": True,
                    "tags": ["vicios redhibitorios"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Crítica: la derogación de la acción estimatoria (quanti minoris)",
                    "resumen": (
                        "El Código de Vélez preveía la acción estimatoria: "
                        "ante un vicio, el adquirente podía RETENER la cosa "
                        "reclamando una quita proporcional del precio. El "
                        "CCyC no la incluyó entre las opciones del art. 1039 "
                        "(solo reparación, cambio o resolución), lo que la "
                        "cátedra critica como ineficiente. Sin embargo, en "
                        "relaciones de CONSUMO, el art. 17 LDC revive "
                        "efectivamente esta opción: el consumidor puede pedir "
                        "sustitución, resolución con restitución, o una quita "
                        "proporcional del precio, cuando la garantía legal del "
                        "art. 11 LDC (6 meses para cosas muebles no "
                        "consumibles) no resulta satisfactoria."
                    ),
                    "clave": True,
                    "tags": ["acción estimatoria", "consumo", "vicios redhibitorios"],
                },
            ],
        },
        {
            "nombre": "Capítulo 11 – Señal o arras",
            "rango": "arts. 1059-1060",
            "articulos": [
                {
                    "num": "1059-1060",
                    "titulo": "Señal confirmatoria (regla general)",
                    "resumen": (
                        "La señal se presume CONFIRMATORIA del contrato (a "
                        "diferencia del Código de Vélez, donde era penitencial "
                        "por defecto). Si el contrato se cumple, se tiene como "
                        "parte del precio; si es penitencial (por pacto "
                        "expreso), autoriza a arrepentirse: quien la dio la "
                        "pierde, y quien la recibió debe restituirla "
                        "duplicada."
                    ),
                    "clave": True,
                    "tags": ["señal", "arras"],
                },
            ],
        },
        {
            "nombre": "Capítulo 12 – Interpretación",
            "rango": "arts. 1061-1068",
            "articulos": [
                {
                    "num": "1061",
                    "titulo": "Intención común y buena fe",
                    "resumen": (
                        "El contrato debe interpretarse conforme a la "
                        "intención común de las partes y al principio de "
                        "buena fe: se protege lo que ambas buscaron "
                        "conjuntamente, no la voluntad interna no exteriorizada "
                        "de una sola de ellas."
                    ),
                    "clave": True,
                    "tags": ["interpretación"],
                },
                {
                    "num": "1062-1067",
                    "titulo": "Interpretación restrictiva, contextual, actos propios",
                    "resumen": (
                        "Interpretación restrictiva (literal) cuando la ley o "
                        "el contrato lo prevé, típico de la fianza. Las "
                        "cláusulas se interpretan las unas por medio de las "
                        "otras (contextual), y ante insuficiencia, se recurre "
                        "a las circunstancias de celebración y a la conducta "
                        "de las partes. Rige el principio de conservación "
                        "(preferir el sentido que dé eficacia al acto) y la "
                        "protección de la confianza (teoría de los actos "
                        "propios: nadie puede contradecir su propia conducta "
                        "anterior)."
                    ),
                    "tags": ["interpretación", "actos propios"],
                },
                {
                    "num": "1068",
                    "titulo": "Expresiones oscuras",
                    "resumen": (
                        "Si persisten dudas: en contratos gratuitos, se "
                        "interpreta en el sentido menos gravoso para el "
                        "obligado; en onerosos, en el sentido que produzca un "
                        "ajuste equitativo de los intereses de ambas partes."
                    ),
                    "tags": ["interpretación"],
                },
                {
                    "num": "1094-1095",
                    "titulo": "Interpretación en contratos de consumo (remisión)",
                    "resumen": (
                        "En consumo rige un régimen distinto y más protector: "
                        "in dubio pro consumidor (ver Título III)."
                    ),
                    "tags": ["interpretación", "consumo"],
                },
            ],
        },
        {
            "nombre": "Capítulo 13 – Subcontrato y Capítulo 14 – Cesión de posición contractual",
            "rango": "arts. 1069-1072 y 1636-1640",
            "articulos": [
                {
                    "num": "1069",
                    "titulo": "Subcontrato",
                    "resumen": (
                        "Nuevo contrato mediante el cual el subcontratante "
                        "crea a favor del subcontratado una nueva posición "
                        "derivada de la que aquel tiene en el contrato "
                        "principal (ej. sublocación). Solo posible en "
                        "contratos de ejecución continuada o diferida."
                    ),
                    "tags": ["subcontrato"],
                },
                {
                    "num": "1636-1640",
                    "titulo": "Cesión de posición contractual",
                    "resumen": (
                        "En contratos con prestaciones pendientes, una parte "
                        "puede transmitir su posición contractual entera "
                        "(derechos y deberes) a un tercero. La teoría "
                        "'unitaria' (adoptada por el CCyC) entiende que se "
                        "transmite la 'calidad de parte' como una "
                        "universalidad indivisible, no una suma de cesión de "
                        "créditos más asunción de deudas. Requiere el "
                        "CONSENTIMIENTO del contratante cedido (antes, "
                        "simultáneo o posterior), porque este no puede ser "
                        "forzado a aceptar un nuevo deudor sin su anuencia. Al "
                        "prestarlo, el cedente originario queda liberado. Las "
                        "garantías de terceros que respaldaban al cedente "
                        "original CADUCAN (no pasan al cesionario), salvo "
                        "autorización expresa de esos garantes (art. 1640)."
                    ),
                    "clave": True,
                    "tags": ["cesión de posición contractual"],
                },
            ],
        },
        {
            "nombre": "Capítulo 15 – Extinción, modificación y adecuación",
            "rango": "arts. 1076-1091",
            "articulos": [
                {
                    "num": "1076",
                    "titulo": "Rescisión bilateral (distracto)",
                    "resumen": (
                        "Extinción por mutuo acuerdo: las mismas voluntades "
                        "que crearon el contrato lo extinguen. Produce efectos "
                        "hacia el futuro (ex nunc) y no afecta derechos de "
                        "terceros ni las prestaciones divisibles ya "
                        "cumplidas."
                    ),
                    "tags": ["extinción", "rescisión bilateral"],
                },
                {
                    "num": "1077",
                    "titulo": "Rescisión unilateral",
                    "resumen": (
                        "Extinción por voluntad de una sola parte, facultada "
                        "por la ley o por cláusula convencional (ej. locación "
                        "de servicios, agencia, concesión). Produce efectos "
                        "hacia el futuro. Exige un preaviso razonable: si se "
                        "ejerce intempestivamente sin aviso, corresponde "
                        "indemnizar el lucro cesante limitado al plazo que "
                        "debió durar el preaviso y la falta de amortización de "
                        "inversiones."
                    ),
                    "clave": True,
                    "tags": ["extinción", "rescisión unilateral"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Revocación (concepto doctrinario)",
                    "resumen": (
                        "Retractación unilateral de la voluntad en actos "
                        "fundados en la confianza personal (intuitu personae): "
                        "mandato, donación por ingratitud, fideicomiso. "
                        "Efectos hacia el futuro; lo actuado frente a terceros "
                        "de buena fe antes de la revocación conserva validez."
                    ),
                    "tags": ["revocación"],
                },
                {
                    "num": "1084-1088",
                    "titulo": "Resolución por incumplimiento (pacto comisorio expreso e implícito)",
                    "resumen": (
                        "Ante el incumplimiento esencial, la parte cumplidora "
                        "puede resolver el contrato: si hay pacto comisorio "
                        "EXPRESO, opera de pleno derecho al comunicar la "
                        "voluntad de resolver; si es IMPLÍCITO, requiere "
                        "previo emplazamiento a cumplir en un plazo no menor a "
                        "15 días, bajo apercibimiento de resolución. A "
                        "diferencia de la rescisión, la resolución produce "
                        "efectos RETROACTIVOS (ex tunc, art. 1079): obliga a "
                        "restituirse lo entregado, salvo en contratos de "
                        "tracto sucesivo donde las prestaciones cumplidas y "
                        "equivalentes quedan firmes."
                    ),
                    "clave": True,
                    "tags": ["resolución", "pacto comisorio"],
                },
                {
                    "num": "1090",
                    "titulo": "Frustración de la finalidad",
                    "resumen": (
                        "Si una alteración extraordinaria, ajena e "
                        "imprevisible destruye la razón de ser que motivó a "
                        "las partes (la causa fin subjetiva compartida), "
                        "aunque la prestación siga siendo físicamente posible, "
                        "la parte perjudicada puede resolver el contrato. Es "
                        "distinta de la imprevisión: aquí el cumplimiento no "
                        "es ruinoso, sino que perdió todo sentido de utilidad "
                        "práctica (ej.: alquilar un balcón para ver un desfile "
                        "que se suspende)."
                    ),
                    "clave": True,
                    "tags": ["frustración del fin"],
                },
                {
                    "num": "1091",
                    "titulo": "Imprevisión (excesiva onerosidad sobreviniente)",
                    "resumen": (
                        "Si en un contrato de ejecución diferida o continuada, "
                        "la prestación de una parte se torna excesivamente "
                        "onerosa por una alteración EXTRAORDINARIA e "
                        "imprevisible de las circunstancias existentes al "
                        "contratar, ajena a las partes y que supera el riesgo "
                        "propio del negocio, esa parte puede plantear la "
                        "resolución total o parcial, o su adecuación "
                        "(reajuste equitativo). No alcanza con que el negocio "
                        "se vuelva 'menos conveniente': el estándar es "
                        "exigente."
                    ),
                    "clave": True,
                    "tags": ["imprevisión", "excesiva onerosidad"],
                },
                {
                    "num": "332",
                    "titulo": "Lesión (vicio genético, no extintivo)",
                    "resumen": (
                        "A diferencia de la imprevisión (sobreviniente), la "
                        "lesión es un vicio de ORIGEN del contrato. Exige tres "
                        "elementos concurrentes: (a) subjetivo de la víctima: "
                        "necesidad, debilidad psíquica o inexperiencia; (b) "
                        "subjetivo del lesionante: aprovechamiento consciente; "
                        "(c) objetivo: ventaja patrimonial evidentemente "
                        "desproporcionada. Habilita pedir la nulidad o el "
                        "reajuste equitativo. Frente a terceros subadquirentes "
                        "de buena fe y a título oneroso, la reivindicación es "
                        "inoponible (art. 392): la víctima solo tendrá acción "
                        "de daños contra su cocontratante original."
                    ),
                    "clave": True,
                    "tags": ["lesión", "nulidad"],
                },
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# TÍTULO III - CONTRATOS DE CONSUMO (arts. 1092-1122) - DESARROLLO AMPLIADO
# ---------------------------------------------------------------------------
TITULO_III_CONSUMO = {
    "nombre": "Título III – Contratos de consumo",
    "rango": "arts. 1092 a 1122 CCyC, más Ley 24.240 (LDC) y art. 42 CN",
    "descripcion": (
        "Incorpora al Código, con jerarquía de sistema general, la "
        "protección del consumidor. Se aplica a toda relación de consumo "
        "entre un consumidor final y un proveedor profesional. La cátedra "
        "Weingarten/Ghersi sostiene que este microsistema —y no el contrato "
        "paritario— es hoy la regla, no la excepción, del tráfico jurídico "
        "real (ver 'Perspectiva de cátedra')."
    ),
    "capitulos": [
        {
            "nombre": "Relación de consumo, sujetos y vulnerabilidad estructural",
            "rango": "arts. 1092-1099 CCyC, art. 1 y 2 LDC, art. 42 CN",
            "articulos": [
                {
                    "num": "1092 / art. 1 LDC",
                    "titulo": "Consumidor y relación de consumo",
                    "resumen": (
                        "Consumidor: persona humana o jurídica que adquiere o "
                        "utiliza bienes o servicios, en forma gratuita u "
                        "onerosa, como destinatario final, en beneficio propio "
                        "o de su grupo familiar o social. La RELACIÓN DE "
                        "CONSUMO (art. 42 CN, art. 3 LDC) es más amplia que el "
                        "'contrato de consumo': abarca las etapas "
                        "precontractual, contractual y poscontractual, no "
                        "requiere un contrato formal, y permite imputar "
                        "responsabilidad objetiva y solidaria a toda la "
                        "cadena de comercialización (fabricante, distribuidor, "
                        "vendedor)."
                    ),
                    "clave": True,
                    "tags": ["consumidor", "relación de consumo"],
                },
                {
                    "num": "art. 2 LDC",
                    "titulo": "Proveedor",
                    "resumen": (
                        "Toda persona humana o jurídica, pública o privada, "
                        "que desarrolle profesionalmente actividades de "
                        "producción, montaje, transformación, importación, "
                        "distribución o comercialización de bienes y "
                        "servicios. Al introducir el riesgo en el mercado y "
                        "lucrar con él, asume el deber de soportar las "
                        "externalidades lesivas de su actividad, con "
                        "prescindencia de su culpa (imputación objetiva)."
                    ),
                    "tags": ["proveedor"],
                },
                {
                    "num": "1096",
                    "titulo": "El 'bystander' o consumidor expuesto",
                    "resumen": (
                        "El microsistema de prácticas comerciales alcanza a "
                        "personas determinables o no, incluyendo a quien no "
                        "contrató nada pero queda 'expuesto' a una relación de "
                        "consumo ajena (ej. un peatón lesionado por un cartel "
                        "publicitario mal instalado, o el chofer de un diario "
                        "golpeado por un proyectil en un estadio, como en el "
                        "caso 'Mosca' de la CSJN). Es un punto de fuerte "
                        "debate doctrinario sobre sus límites."
                    ),
                    "clave": True,
                    "tags": ["bystander", "consumidor expuesto"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Vulnerabilidad estructural e hipervulnerabilidad",
                    "resumen": (
                        "Para la cátedra Weingarten/Ghersi, la asimetría entre "
                        "proveedor y consumidor no es una debilidad "
                        "circunstancial sino ESTRUCTURAL (técnica, económica, "
                        "biológica —consumo de supervivencia—, ambiental y "
                        "psicológica), y opera como presunción que no admite "
                        "prueba en contrario. Los 'consumidores "
                        "hipervulnerables' (niños, ancianos, personas con "
                        "discapacidad, sectores marginados) requieren tutela "
                        "reforzada."
                    ),
                    "clave": True,
                    "tags": ["vulnerabilidad estructural", "hipervulnerabilidad"],
                },
            ],
        },
        {
            "nombre": "Deberes del proveedor: seguridad, información y publicidad",
            "rango": "arts. 1100-1103 CCyC, arts. 4, 5, 8 y 8 bis LDC",
            "articulos": [
                {
                    "num": "art. 42 CN, arts. 5 y 40 LDC",
                    "titulo": "Obligación de seguridad",
                    "resumen": (
                        "Mandato tácito, principal e insoslayable de "
                        "RESULTADO, ínsito en todo contrato y relación de "
                        "consumo: preservar la indemnidad física y patrimonial "
                        "del consumidor. No puede eludirse con cláusulas "
                        "eximentes. La responsabilidad es objetiva y "
                        "solidaria por el riesgo o vicio de la cosa o "
                        "actividad (arts. 1757-1758 CCyC y art. 40 LDC): así "
                        "responde el hotel por daños al huésped o la "
                        "concesionaria vial por un animal suelto en la ruta."
                    ),
                    "clave": True,
                    "tags": ["obligación de seguridad"],
                },
                {
                    "num": "1100 / art. 4 LDC",
                    "titulo": "Deber de información",
                    "resumen": (
                        "El proveedor debe suministrar información cierta, "
                        "clara, detallada y gratuita sobre las características "
                        "esenciales del bien o servicio y sus riesgos, en "
                        "soporte accesible. Ataca directamente la "
                        "vulnerabilidad técnica del consumidor."
                    ),
                    "clave": True,
                    "tags": ["deber de información"],
                },
                {
                    "num": "1101-1103 / art. 8 LDC",
                    "titulo": "Publicidad: fuerza vinculante y prohibiciones",
                    "resumen": (
                        "Todas las precisiones de la publicidad (prospectos, "
                        "anuncios) integran el contrato y obligan al "
                        "proveedor (art. 1103, art. 8 LDC): la cátedra critica "
                        "aplicar el art. 973 (invitación a ofertar) a estas "
                        "relaciones, porque la publicidad masiva funciona "
                        "como oferta vinculante. Se prohíbe la publicidad "
                        "engañosa (induce a error sobre elementos esenciales), "
                        "la comparativa ilegítima (sin objetividad) y la "
                        "abusiva o discriminatoria (denigra la dignidad, "
                        "incita comportamientos peligrosos). Los "
                        "consumidores y el Estado pueden pedir el cese de la "
                        "publicidad ilícita y la contrapublicidad "
                        "rectificatoria (art. 1102)."
                    ),
                    "clave": True,
                    "tags": ["publicidad", "publicidad engañosa"],
                },
                {
                    "num": "1096-1099",
                    "titulo": "Prácticas comerciales abusivas: trato digno y no discriminación",
                    "resumen": (
                        "Trato digno (1097): prohíbe prácticas vejatorias o "
                        "intimidatorias (ej. cobranzas hostiles). Trato "
                        "equitativo y no discriminatorio (1098). Libertad de "
                        "contratar (1099): prohíbe las 'ventas atadas' "
                        "(subordinar la compra de un producto a la de otro no "
                        "requerido)."
                    ),
                    "tags": ["trato digno", "prácticas abusivas"],
                },
            ],
        },
        {
            "nombre": "Modalidades especiales: distancia, fuera del establecimiento y medios electrónicos",
            "rango": "arts. 1104-1117 CCyC",
            "articulos": [
                {
                    "num": "1104-1105",
                    "titulo": "Contratos a distancia y fuera del establecimiento comercial",
                    "resumen": (
                        "Atrapan las contrataciones celebradas fuera del local "
                        "comercial (domicilio, vía pública) o sin presencia "
                        "física simultánea (por correo, medios electrónicos, "
                        "catálogos). Buscan neutralizar el 'efecto sorpresa' y "
                        "la imposibilidad de examinar la cosa antes de "
                        "comprar."
                    ),
                    "tags": ["contratos a distancia"],
                },
                {
                    "num": "1109",
                    "titulo": "Lugar de cumplimiento (garantía de jurisdicción)",
                    "resumen": (
                        "Se considera lugar de cumplimiento aquel donde el "
                        "consumidor recibió o debió recibir la prestación, lo "
                        "que fija la jurisdicción judicial. Impide que el "
                        "proveedor imponga litigar lejos del domicilio del "
                        "consumidor."
                    ),
                    "tags": ["jurisdicción del consumidor"],
                },
                {
                    "num": "1110-1115",
                    "titulo": "Derecho de revocación (arrepentimiento)",
                    "resumen": (
                        "El consumidor puede revocar unilateral e "
                        "incausadamente el contrato dentro de los 10 días "
                        "corridos desde la recepción del bien (período de "
                        "'enfriamiento'). El proveedor debe informar este "
                        "derecho por escrito y en caracteres destacados. "
                        "Ejercida la revocación, las partes se restituyen lo "
                        "entregado, y TODOS los gastos y riesgos de la "
                        "devolución quedan a cargo del proveedor (si no fuera "
                        "así, el derecho sería ilusorio)."
                    ),
                    "clave": True,
                    "tags": ["derecho de revocación", "arrepentimiento"],
                },
                {
                    "num": "1116-1117",
                    "titulo": "Excepciones a la revocación y orden público",
                    "resumen": (
                        "No hay derecho de revocación, entre otros casos, "
                        "para: grabaciones o software desembalados, prensa "
                        "periódica, o confecciones a medida. Todo este "
                        "régimen es de orden público irrenunciable."
                    ),
                    "tags": ["derecho de revocación", "excepciones"],
                },
                {
                    "num": "1106-1108",
                    "titulo": "Medios electrónicos y contratos informáticos",
                    "resumen": (
                        "La forma escrita se tiene por satisfecha con soporte "
                        "electrónico accesible e inalterable (art. 1106). El "
                        "proveedor debe informar además la operatoria técnica "
                        "y los riesgos de seguridad informática (art. 1107): "
                        "los riesgos del ecosistema digital (phishing, "
                        "hackeo) son soportados objetivamente por quien "
                        "controla los servidores. Las ofertas online quedan "
                        "vigentes mientras sean accesibles (art. 1108). En los "
                        "'contratos informáticos' (hardware/software), la "
                        "cátedra sostiene que el deber de información se eleva "
                        "a un DEBER DE ASESORAMIENTO o consejo: el proveedor "
                        "experto debe diagnosticar la necesidad real del "
                        "cliente, no solo informar datos técnicos crudos; si "
                        "lo omite, el consentimiento del cliente adolece de "
                        "error sustancial."
                    ),
                    "clave": True,
                    "tags": ["medios electrónicos", "contratos informáticos"],
                },
            ],
        },
        {
            "nombre": "Cláusulas abusivas, integración e interpretación en el consumo",
            "rango": "arts. 1094-1095 y 1117-1122 CCyC",
            "articulos": [
                {
                    "num": "1094",
                    "titulo": "Prelación normativa: protección del consumidor y consumo sustentable",
                    "resumen": (
                        "Ante colisión de normas, prevalece la más favorable "
                        "al consumidor. Introduce además el principio de "
                        "acceso al consumo SUSTENTABLE: el afán de lucro cede "
                        "ante la sustentabilidad ambiental (art. 41 CN y art. "
                        "240 CCyC)."
                    ),
                    "clave": True,
                    "tags": ["prelación normativa", "consumo sustentable"],
                },
                {
                    "num": "1095",
                    "titulo": "In dubio pro consumidor",
                    "resumen": (
                        "Ante dudas sobre el alcance de la obligación, se "
                        "adopta la interpretación menos gravosa para el "
                        "consumidor. Se funda en la 'teoría del riesgo de la "
                        "redacción': quien monopoliza la técnica negocial debe "
                        "soportar el riesgo de su propia oscuridad o "
                        "ambigüedad."
                    ),
                    "clave": True,
                    "tags": ["in dubio pro consumidor"],
                },
                {
                    "num": "1119",
                    "titulo": "Cláusula abusiva (definición)",
                    "resumen": (
                        "Es abusiva la cláusula que, negociada o no, tiene por "
                        "objeto o efecto provocar un desequilibrio "
                        "significativo entre los derechos y obligaciones de "
                        "las partes, en perjuicio del consumidor."
                    ),
                    "clave": True,
                    "tags": ["cláusulas abusivas"],
                },
                {
                    "num": "1120",
                    "titulo": "Situación jurídica abusiva",
                    "resumen": (
                        "Permite detectar abusividad no en una cláusula "
                        "aislada, sino en la CONEXIDAD de varios actos "
                        "jurídicos que, tomados en red, acorralan al "
                        "adherente (ej. una compraventa atada a un seguro "
                        "obligatorio y a un mutuo usurario)."
                    ),
                    "clave": True,
                    "tags": ["situación jurídica abusiva"],
                },
                {
                    "num": "1122",
                    "titulo": "Control judicial aun con aprobación administrativa",
                    "resumen": (
                        "El control de abusividad corresponde al Poder "
                        "Judicial, incluso si el modelo de contrato fue "
                        "aprobado previamente por un organismo de control "
                        "(Superintendencia de Seguros, BCRA, IGJ): la "
                        "aprobación administrativa no inmuniza a la empresa "
                        "frente al control judicial posterior."
                    ),
                    "clave": True,
                    "tags": ["control judicial", "cláusulas abusivas"],
                },
                {
                    "num": "art. 52 bis LDC",
                    "titulo": "Daño punitivo (multa civil)",
                    "resumen": (
                        "Ante un incumplimiento con grave menosprecio de los "
                        "derechos del consumidor, el juez puede aplicar una "
                        "multa civil a favor del consumidor, con función "
                        "disuasiva: busca evitar que 'sea más barato "
                        "incumplir la ley que respetarla'."
                    ),
                    "clave": True,
                    "tags": ["daño punitivo"],
                },
            ],
        },
    ],
}

# ---------------------------------------------------------------------------
# TÍTULO IV - CONTRATOS EN PARTICULAR (arts. 1123 a 1881)
# ---------------------------------------------------------------------------
TITULO_IV_PARTICULARES = {
    "nombre": "Título IV – Contratos en particular",
    "rango": "arts. 1123 a 1881",
    "descripcion": (
        "Regula cada tipo contractual específico. Los 22 contratos de este "
        "título están desarrollados artículo por artículo, con base en "
        "fuentes oficiales (InfoLeg/SAIJ) y doctrina académica."
    ),
    "capitulos": [
        {
            "nombre": "Compraventa",
            "rango": "arts. 1123-1171",
            "articulos": [
                {
                    "num": "1123-1125",
                    "titulo": "Definición y aplicación supletoria",
                    "resumen": (
                        "Hay compraventa si una parte se obliga a transferir "
                        "la propiedad de una cosa y la otra a pagar un precio "
                        "en dinero. Es un contrato bilateral, oneroso, en "
                        "principio conmutativo (puede ser aleatorio, arts. "
                        "1130-1131), formal para inmuebles y nominado. Sus "
                        "normas se aplican supletoriamente a la transferencia "
                        "de otros derechos reales (condominio, usufructo, "
                        "superficie) y a la venta de títulos valores. Cuando "
                        "una parte se compromete a entregar cosas por un "
                        "precio, aunque deban ser manufacturadas, sigue siendo "
                        "compraventa si el comitente no provee una parte "
                        "sustancial de los materiales (si la provee, es "
                        "contrato de obra, art. 1125)."
                    ),
                    "clave": True,
                    "tags": ["compraventa", "definición"],
                },
                {
                    "num": "1128-1132",
                    "titulo": "La cosa vendida",
                    "resumen": (
                        "Nadie está obligado a vender, salvo necesidad "
                        "jurídica (art. 1128). Puede venderse toda cosa que "
                        "sea objeto de los contratos. Si la cosa CIERTA ya "
                        "había dejado de existir al perfeccionarse el "
                        "contrato, este no produce efecto (si dejó de existir "
                        "solo parcialmente, el comprador puede pedir la parte "
                        "existente con reducción de precio). La venta de "
                        "COSA FUTURA se entiende sujeta a la condición de que "
                        "llegue a existir. La venta de COSA AJENA es válida: "
                        "si el vendedor no garantizó el éxito de la promesa, "
                        "asume una obligación de medios; si lo garantizó, "
                        "asume una de resultado y responde por daños si la "
                        "cosa no se transmite."
                    ),
                    "clave": True,
                    "tags": ["compraventa", "cosa vendida", "cosa ajena"],
                },
                {
                    "num": "1137-1140",
                    "titulo": "Obligaciones del vendedor",
                    "resumen": (
                        "Transferir la propiedad de la cosa, poner a "
                        "disposición del comprador los instrumentos "
                        "requeridos por los usos y prestar toda la "
                        "cooperación exigible para concretar la transferencia "
                        "dominial. Los gastos de entrega están a su cargo "
                        "(y en inmuebles, también el estudio de título, la "
                        "mensura y los tributos que graven la venta), salvo "
                        "pacto en contrario. Debe entregar el inmueble "
                        "inmediatamente después de la escrituración, salvo "
                        "convención distinta."
                    ),
                    "clave": True,
                    "tags": ["compraventa", "obligaciones del vendedor"],
                },
                {
                    "num": "1141",
                    "titulo": "Obligaciones del comprador",
                    "resumen": (
                        "Pagar el precio en el lugar y tiempo convenidos, "
                        "recibir la cosa y los documentos vinculados, y pagar "
                        "los gastos de recibo (incluidos los de testimonio de "
                        "la escritura pública y los demás posteriores a la "
                        "venta)."
                    ),
                    "tags": ["compraventa", "obligaciones del comprador"],
                },
                {
                    "num": "1151-1153",
                    "titulo": "Riesgos, tiempo del pago y venta sobre muestras",
                    "resumen": (
                        "Los riesgos de daño o pérdida de la cosa están a "
                        "cargo del vendedor hasta ponerla a disposición del "
                        "comprador. El pago se hace contra la entrega, salvo "
                        "pacto en contrario, y el comprador no está obligado "
                        "a pagar mientras no pueda examinar la cosa. En la "
                        "venta sobre muestras, el comprador no puede rehusar "
                        "la recepción si la cosa coincide en calidad con la "
                        "muestra."
                    ),
                    "tags": ["compraventa", "riesgos", "pago"],
                },
                {
                    "num": "1160",
                    "titulo": "Cláusulas especiales: venta a satisfacción/ensayo",
                    "resumen": (
                        "La venta 'a satisfacción del comprador' o 'a prueba' "
                        "(ad gustum) se presume sujeta a una condición "
                        "suspensiva: la aceptación del comprador, quien tiene "
                        "un plazo (10 días, salvo usos o pacto distinto) para "
                        "probar la cosa."
                    ),
                    "tags": ["compraventa", "venta a satisfacción"],
                },
                {
                    "num": "1170-1171",
                    "titulo": "El boleto de compraventa inmobiliaria",
                    "resumen": (
                        "El boleto de compraventa de un inmueble, de fecha "
                        "cierta y a favor de un adquirente de buena fe, es "
                        "oponible a los acreedores del vendedor con embargo "
                        "posterior si el comprador abonó el 25% del precio "
                        "(art. 1170), y es oponible al CONCURSO O QUIEBRA del "
                        "vendedor bajo el mismo umbral del 25% (art. 1171): "
                        "en ese caso el juez debe ordenar que se otorgue la "
                        "escritura pública, y si el saldo de precio es a "
                        "plazo, se debe constituir hipoteca en primer grado "
                        "en garantía. Esto explica por qué, en la práctica, "
                        "el boleto suele tratarse como un contrato definitivo "
                        "y no como una simple promesa."
                    ),
                    "clave": True,
                    "tags": ["compraventa", "boleto de compraventa"],
                },
            ],
        },
        {
            "nombre": "Permuta",
            "rango": "arts. 1172-1175",
            "articulos": [
                {
                    "num": "1172-1173",
                    "titulo": "Definición y gastos",
                    "resumen": (
                        "Hay permuta si las partes se obligan recíprocamente "
                        "a transferirse el dominio de cosas que NO son "
                        "dinero (si una de las prestaciones fuera en parte "
                        "dinero, hay que analizar cuál es la prestación "
                        "principal para calificar el contrato como permuta o "
                        "compraventa). Salvo pacto en contrario, los gastos "
                        "se reparten por partes iguales entre los "
                        "permutantes, y se aplican supletoriamente las normas "
                        "de la compraventa (evicción, vicios redhibitorios, "
                        "etc.), adaptando la posición de 'vendedor' a cada "
                        "permutante respecto de lo que da."
                    ),
                    "clave": True,
                    "tags": ["permuta"],
                },
            ],
        },
        {
            "nombre": "Suministro",
            "rango": "arts. 1176-1186",
            "articulos": [
                {
                    "num": "1176",
                    "titulo": "Definición",
                    "resumen": (
                        "El suministrante se obliga a entregar bienes "
                        "—incluso servicios sin relación de dependencia— en "
                        "forma periódica o continuada, y el suministrado a "
                        "pagar un precio por cada entrega o grupo de ellas. "
                        "Es el contrato típico de abastecimiento continuado "
                        "entre empresas (ej. una fábrica que provee insumos "
                        "periódicamente a otra)."
                    ),
                    "clave": True,
                    "tags": ["suministro", "definición"],
                },
                {
                    "num": "1177",
                    "titulo": "Plazo máximo",
                    "resumen": (
                        "El contrato puede pactarse por un plazo máximo de "
                        "20 años si se trata de frutos o productos del suelo "
                        "o del subsuelo, y de 10 años en los demás casos."
                    ),
                    "tags": ["suministro", "plazo"],
                },
                {
                    "num": "1178",
                    "titulo": "Cantidades",
                    "resumen": (
                        "Si no se pactó la cantidad de cada entrega, el "
                        "contrato se entiende celebrado según las "
                        "necesidades normales del suministrado al momento de "
                        "contratar. Si solo se pactaron cantidades máximas y "
                        "mínimas, el suministrado puede determinar la "
                        "cantidad dentro de esos límites para cada período."
                    ),
                    "tags": ["suministro", "cantidades"],
                },
            ],
        },
        {
            "nombre": "Locación",
            "rango": "arts. 1187-1226",
            "articulos": [
                {
                    "num": "1187-1188",
                    "titulo": "Definición y forma",
                    "resumen": (
                        "Una parte se obliga a otorgar a otra el uso y goce "
                        "temporario de una cosa, a cambio del pago de un "
                        "precio en dinero. Se aplican supletoriamente las "
                        "normas de compraventa sobre consentimiento, precio y "
                        "objeto. La locación de inmuebles, muebles "
                        "registrables o de parte material de un inmueble debe "
                        "hacerse por ESCRITO (también sus prórrogas y "
                        "modificaciones)."
                    ),
                    "clave": True,
                    "tags": ["locación", "definición", "forma"],
                },
                {
                    "num": "1189-1190",
                    "titulo": "Transmisión por muerte, enajenación y continuador",
                    "resumen": (
                        "Salvo pacto en contrario, la locación se transmite "
                        "activa y pasivamente por causa de muerte, y subsiste "
                        "aunque la cosa locada sea vendida a un tercero. Si el "
                        "inmueble (o parte de él) está destinado a vivienda, "
                        "en caso de abandono o fallecimiento del locatario "
                        "puede 'continuar' la locación quien haya recibido "
                        "ostensible trato familiar (cónyuge, conviviente, "
                        "descendientes, ascendientes), preservando la "
                        "vivienda familiar."
                    ),
                    "tags": ["locación", "continuador"],
                },
                {
                    "num": "1196-1198",
                    "titulo": "Plazo mínimo y máximo",
                    "resumen": (
                        "El plazo NO puede exceder 20 años para destino "
                        "habitacional y 50 años para los demás destinos. Si "
                        "no se pactó plazo, se aplica un plazo mínimo legal "
                        "en beneficio del locatario. Este plazo mínimo es de "
                        "orden público para el LOCADOR (no puede exigir "
                        "menos), pero es renunciable por el locatario (nunca "
                        "de forma anticipada al firmar), en cuyo beneficio "
                        "está previsto."
                    ),
                    "clave": True,
                    "tags": ["locación", "plazo"],
                },
                {
                    "num": "1206-1208",
                    "titulo": "Obligaciones del locatario",
                    "resumen": (
                        "Debe mantener la cosa y conservarla en el estado en "
                        "que la recibió (responde por deterioros, incluso de "
                        "visitantes ocasionales, salvo los causados por el "
                        "locador o sus dependientes, y por la destrucción por "
                        "incendio no originado en caso fortuito). Si es mueble, "
                        "el gasto de conservación y las mejoras de mero "
                        "mantenimiento corren por su cuenta; si es inmueble, "
                        "solo las de mero mantenimiento. Debe pagar el canon "
                        "convenido, que incluye el precio y toda otra "
                        "prestación periódica pactada."
                    ),
                    "tags": ["locación", "obligaciones del locatario"],
                },
                {
                    "num": "1216",
                    "titulo": "Acciones directas (locador-sublocatario)",
                    "resumen": (
                        "El locador tiene acción directa contra el "
                        "sublocatario para cobrar el alquiler adeudado por el "
                        "locatario (hasta el límite de lo que el "
                        "sublocatario le deba a este) y para exigirle el "
                        "cumplimiento de las obligaciones de la sublocación. "
                        "Recíprocamente, el sublocatario tiene acción directa "
                        "contra el locador para exigir el cumplimiento de las "
                        "obligaciones del contrato principal."
                    ),
                    "clave": True,
                    "tags": ["locación", "acción directa", "sublocación"],
                },
                {
                    "num": "1217-1218",
                    "titulo": "Extinción y continuación tácita",
                    "resumen": (
                        "Modos especiales de extinción: cumplimiento del "
                        "plazo (con el requerimiento del art. 1218 si "
                        "corresponde) y resolución anticipada. Si vencido el "
                        "plazo el locatario continúa en la tenencia sin "
                        "oposición del locador, no hay tácita reconducción "
                        "(no nace un nuevo contrato), sino la continuación de "
                        "la locación en los mismos términos, hasta que "
                        "cualquiera de las partes le ponga fin."
                    ),
                    "tags": ["locación", "extinción"],
                },
                {
                    "num": "1219-1220",
                    "titulo": "Resolución por incumplimiento",
                    "resumen": (
                        "El LOCADOR puede resolver por: cambio de destino o "
                        "uso irregular de la cosa, falta de conservación o "
                        "abandono, o falta de pago del alquiler durante DOS "
                        "períodos consecutivos. El LOCATARIO puede resolver "
                        "si el locador incumple su obligación de conservar la "
                        "cosa apta para el uso convenido (salvo que el daño "
                        "lo haya causado el propio locatario), o la garantía "
                        "de evicción o de vicios redhibitorios."
                    ),
                    "clave": True,
                    "tags": ["locación", "resolución"],
                },
                {
                    "num": "1221",
                    "titulo": "Resolución anticipada por el locatario",
                    "resumen": (
                        "El locatario puede resolver anticipadamente en "
                        "cualquier momento, notificando fehacientemente al "
                        "locador y pagando una indemnización. El texto "
                        "vigente desde el DNU 70/2023 (que derogó la Ley de "
                        "Alquileres 27.551) fija esa indemnización en el 10% "
                        "del saldo del canon locativo futuro, calculado desde "
                        "la notificación hasta el fin del plazo pactado."
                    ),
                    "clave": True,
                    "tags": ["locación", "resolución anticipada", "DNU 70/2023"],
                },
                {
                    "num": "1225",
                    "titulo": "Caducidad de la fianza en la locación",
                    "resumen": (
                        "Las obligaciones del fiador CESAN automáticamente al "
                        "vencer el plazo de la locación (salvo la que derive "
                        "de la no restitución a tiempo del inmueble). Se "
                        "exige el consentimiento EXPRESO del fiador para que "
                        "su garantía se extienda a una renovación o prórroga: "
                        "es nula toda cláusula que extienda anticipadamente "
                        "la fianza a futuras renovaciones sin ese "
                        "consentimiento. Es la aplicación concreta, en "
                        "materia locativa, de la regla general del art. 1596 "
                        "inc. b) sobre extinción de la fianza por prórroga no "
                        "consentida."
                    ),
                    "clave": True,
                    "tags": ["locación", "fianza"],
                },
                {
                    "num": "cátedra",
                    "titulo": "El DNU 70/2023 y la derogación de la Ley de Alquileres",
                    "resumen": (
                        "El DNU 70/2023 derogó la Ley 27.551 (Ley de "
                        "Alquileres, de 2020), que había fijado plazos y "
                        "fórmulas de ajuste obligatorias. Los contratos de "
                        "locación volvieron al esquema más flexible del CCyC "
                        "original: las partes pueden pactar libremente la "
                        "moneda, la periodicidad de pago (nunca menor a un "
                        "mes) y el índice de ajuste del canon, y ya no existe "
                        "obligación de registrar el contrato ante la AFIP."
                    ),
                    "clave": True,
                    "tags": ["locación", "DNU 70/2023"],
                },
            ],
        },
        {
            "nombre": "Leasing",
            "rango": "arts. 1227-1250",
            "articulos": [
                {
                    "num": "1227",
                    "titulo": "Definición y naturaleza mixta",
                    "resumen": (
                        "El dador conviene transferir al tomador la tenencia "
                        "de un bien cierto para su uso y goce, contra el pago "
                        "de un canon, y le confiere una opción de compra por "
                        "un precio. No es una simple suma de locación + "
                        "compraventa, sino un negocio único con causa-fin de "
                        "FINANCIACIÓN: caracteres consensual, bilateral, "
                        "oneroso, conmutativo, formal y de tracto sucesivo."
                    ),
                    "clave": True,
                    "tags": ["leasing", "definición"],
                },
                {
                    "num": "1231",
                    "titulo": "Modalidades de adquisición del bien y traslación de riesgos",
                    "resumen": (
                        "Según cómo el dador adquiere el bien, cambia quién "
                        "asume los riesgos de vicios o falta de entrega: (a) "
                        "compra a proveedor indicado por el tomador o (b) "
                        "según sus especificaciones, o (c) sustitución en un "
                        "contrato ya celebrado por el tomador: en estos tres "
                        "casos el dador queda LIBERADO de responder por "
                        "evicción o vicios, subrogándose el tomador en las "
                        "acciones contra el proveedor (art. 1232); (d) el "
                        "bien ya era del dador (leasing operativo): el dador "
                        "responde PLENAMENTE; (e) retro-leasing o lease-back "
                        "(el tomador le vende el bien al dador y lo recibe de "
                        "vuelta en leasing): el dador queda liberado porque el "
                        "tomador ya conocía el estado del bien; (f) "
                        "sub-leasing: el dador solo tiene un derecho de uso "
                        "sobre el bien."
                    ),
                    "clave": True,
                    "tags": ["leasing", "riesgos"],
                },
                {
                    "num": "1234",
                    "titulo": "Inscripción registral y oponibilidad",
                    "resumen": (
                        "Debe instrumentarse por escritura pública (inmuebles, "
                        "buques, aeronaves) o instrumento público o privado "
                        "(el resto). Para que el contrato sea oponible a "
                        "terceros desde la ENTREGA del bien (efecto "
                        "retroactivo), la inscripción debe solicitarse dentro "
                        "de los 5 días hábiles de la entrega; si se hace "
                        "después, la oponibilidad corre solo desde la "
                        "inscripción. Vigencia de la inscripción: 20 años "
                        "(inmuebles/buques/aeronaves) o 10 años (el resto). "
                        "En la quiebra del dador, el leasing registrado es "
                        "oponible a sus acreedores; en la quiebra del "
                        "tomador, el síndico decide continuar o resolver el "
                        "contrato con autorización judicial."
                    ),
                    "tags": ["leasing", "registración"],
                },
                {
                    "num": "1243",
                    "titulo": "Responsabilidad objetiva frente a terceros: recae en el tomador",
                    "resumen": (
                        "A diferencia de la regla general de responsabilidad "
                        "concurrente entre dueño y guardián (art. 1758), en el "
                        "leasing la responsabilidad OBJETIVA por riesgo o "
                        "vicio de la cosa (art. 1757) recae exclusivamente "
                        "sobre el TOMADOR, porque es quien tiene la guarda "
                        "material e intelectual y el aprovechamiento "
                        "económico del bien, pese a que el dador conserva la "
                        "propiedad registral."
                    ),
                    "clave": True,
                    "tags": ["leasing", "responsabilidad objetiva"],
                },
                {
                    "num": "1230 y 1241",
                    "titulo": "Opción de compra y prórroga",
                    "resumen": (
                        "El tomador puede ejercer la opción de compra una vez "
                        "pagadas las 3/4 partes del canon total (salvo pacto "
                        "menor). El precio de la opción debe estar "
                        "determinado o ser determinable según pautas objetivas "
                        "pactadas: no se admite que el dador lo fije "
                        "unilateralmente al momento del ejercicio. Las partes "
                        "pueden prever la prórroga del plazo de uso a opción "
                        "del tomador."
                    ),
                    "tags": ["leasing", "opción de compra"],
                },
                {
                    "num": "1248-1249",
                    "titulo": "Incumplimiento: desalojo (inmuebles) y secuestro (muebles)",
                    "resumen": (
                        "Leasing INMOBILIARIO: el procedimiento de desalojo "
                        "por falta de pago varía según el porcentaje de "
                        "cánones pagados (menos de 25%: desalojo directo; "
                        "entre 25% y 75%: intimación y 60 días de gracia; más "
                        "de 75%: intimación y 90 días de gracia, pudiendo "
                        "pagar o ejercer la opción de compra). Leasing "
                        "MOBILIARIO: el dador puede optar por el secuestro "
                        "directo del bien (previa interpelación de al menos 5 "
                        "días hábiles), lo que resuelve el contrato de pleno "
                        "derecho, o accionar ejecutivamente por el cobro de "
                        "cánones, ya que el contrato inscripto es título "
                        "ejecutivo."
                    ),
                    "clave": True,
                    "tags": ["leasing", "incumplimiento"],
                },
            ],
        },
        {
            "nombre": "Obra y servicios",
            "rango": "arts. 1251-1279",
            "articulos": [
                {
                    "num": "1251",
                    "titulo": "Definición conjunta",
                    "resumen": (
                        "Hay contrato de obra o de servicios cuando una "
                        "persona (contratista o prestador de servicios), "
                        "actuando independientemente, se obliga a favor de "
                        "otra (comitente) a realizar una obra material o "
                        "intelectual, o a proveer un servicio, mediante una "
                        "retribución. El Código unificó ambas figuras (antes "
                        "asimiladas a la 'locación de cosas' del Código de "
                        "Vélez) pero las distingue funcionalmente."
                    ),
                    "clave": True,
                    "tags": ["obra y servicios", "definición"],
                },
                {
                    "num": "1252",
                    "titulo": "Distinción obra/servicio: el criterio del resultado",
                    "resumen": (
                        "Si hay duda sobre la calificación del contrato, se "
                        "entiende que es de OBRA cuando se promete un "
                        "resultado eficaz, reproducible o susceptible de "
                        "entrega (se asimila a la obligación de resultado del "
                        "art. 774 inc. c). Se entiende que es de SERVICIOS "
                        "cuando la obligación de hacer consiste en realizar "
                        "cierta actividad independiente de su eficacia "
                        "(obligación de medios, art. 774 inc. a)."
                    ),
                    "clave": True,
                    "tags": ["obra y servicios", "obligación de resultado"],
                },
                {
                    "num": "1253",
                    "titulo": "Libertad de medios de ejecución",
                    "resumen": (
                        "A falta de ajuste sobre el modo de hacer la obra o "
                        "prestar el servicio, el contratista o prestador "
                        "elige libremente los medios de ejecución del "
                        "contrato."
                    ),
                    "tags": ["obra y servicios", "medios de ejecución"],
                },
                {
                    "num": "1256-1257",
                    "titulo": "Obligaciones nucleares de las partes",
                    "resumen": (
                        "El contratista o prestador debe: ejecutar conforme a "
                        "las previsiones contractuales y con los "
                        "conocimientos razonablemente exigibles según el "
                        "arte, ciencia o técnica de la actividad; informar al "
                        "comitente sobre aspectos esenciales; y entregar la "
                        "obra en el plazo pactado. El comitente debe pagar la "
                        "retribución y prestar la colaboración necesaria."
                    ),
                    "tags": ["obra y servicios", "obligaciones"],
                },
                {
                    "num": "1273-1274",
                    "titulo": "Responsabilidad por ruina de obra en inmuebles",
                    "resumen": (
                        "El constructor de una obra en inmueble destinada por "
                        "su naturaleza a larga duración responde frente al "
                        "comitente y al adquirente por los daños que "
                        "comprometen su solidez y por los que la hacen "
                        "IMPROPIA para su destino (ruina propia o impropia). "
                        "Solo se libera probando una causa AJENA: no son "
                        "causa ajena el vicio del suelo (aunque el terreno "
                        "sea del comitente o de un tercero) ni el vicio de "
                        "los materiales (aunque no los haya provisto el "
                        "contratista). Esta responsabilidad de orden público "
                        "se extiende a los profesionales que intervinieron "
                        "en la obra según su grado de participación."
                    ),
                    "clave": True,
                    "tags": ["obra y servicios", "ruina de obra"],
                },
                {
                    "num": "1276",
                    "titulo": "Nulidad de la cláusula de exclusión de responsabilidad",
                    "resumen": (
                        "Toda cláusula que dispense o limite la "
                        "responsabilidad por ruina o por hacer la obra "
                        "impropia para su destino se tiene por NO ESCRITA: es "
                        "responsabilidad de orden público de protección "
                        "(análoga, en su lógica, a la nulidad de las "
                        "cláusulas abusivas del art. 37 LDC cuando el "
                        "comitente es un consumidor)."
                    ),
                    "clave": True,
                    "tags": ["obra y servicios", "cláusulas nulas"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Plazos de caducidad y prescripción por vicios de obra",
                    "resumen": (
                        "Si el vicio afecta un INMUEBLE, el comitente tiene "
                        "3 años desde la recepción para que el defecto se "
                        "manifieste (se hayan o no exteriorizado antes); en "
                        "MUEBLES, el plazo de caducidad es de 6 meses desde "
                        "la recepción. Manifestado el vicio, debe denunciarse "
                        "expresamente dentro de los 60 días de advertido, "
                        "bajo pena de caducidad de la acción. Denunciado en "
                        "término, el plazo de PRESCRIPCIÓN de la acción es de "
                        "1 año (o 3 años si es una relación de consumo)."
                    ),
                    "clave": True,
                    "tags": ["obra y servicios", "prescripción", "vicios"],
                },
                {
                    "num": "1278-1279",
                    "titulo": "Normas especiales para los servicios",
                    "resumen": (
                        "Al contrato de servicios se le aplican, en lo "
                        "pertinente, las normas del contrato de obra. Los "
                        "servicios CONTINUADOS (de tracto sucesivo) se "
                        "presumen contratados por tiempo indeterminado si no "
                        "se pactó un plazo."
                    ),
                    "tags": ["obra y servicios", "servicios continuados"],
                },
            ],
        },
        {
            "nombre": "Transporte",
            "rango": "arts. 1280-1318",
            "articulos": [
                {
                    "num": "1280",
                    "titulo": "Definición y ámbito de aplicación",
                    "resumen": (
                        "El transportista (porteador) se obliga a trasladar "
                        "de forma incólume personas o cosas de un lugar a "
                        "otro, y el pasajero o cargador se obliga a pagar un "
                        "flete. Rige para todo medio de transporte terrestre "
                        "(automotor, ferrocarril), sin perjuicio de leyes "
                        "especiales (Código Aeronáutico, Ley de Navegación)."
                    ),
                    "tags": ["transporte", "definición"],
                },
                {
                    "num": "1289-1290",
                    "titulo": "Obligaciones del porteador y del pasajero",
                    "resumen": (
                        "Porteador: proveer la plaza convenida, trasladar en "
                        "el plazo pactado y garantizar la SEGURIDAD del "
                        "pasajero (obligación de resultado). Pasajero: pagar "
                        "el pasaje, presentarse en término y acatar los "
                        "reglamentos de seguridad."
                    ),
                    "clave": True,
                    "tags": ["transporte", "obligaciones"],
                },
                {
                    "num": "1286-1289",
                    "titulo": "Obligación tácita de seguridad y responsabilidad objetiva",
                    "resumen": (
                        "La obligación de seguridad del transportista es de "
                        "RESULTADO: llevar al pasajero sano y salvo a "
                        "destino. La responsabilidad se rige por el factor "
                        "objetivo de riesgo creado (art. 1757), con inversión "
                        "de la carga de la prueba a favor del pasajero. Solo "
                        "se exime probando: hecho de la víctima, hecho de un "
                        "tercero extraño, o caso fortuito AJENO al riesgo de "
                        "la actividad (un choque, un reventón de neumático o "
                        "una falla de frenos NO son caso fortuito: son "
                        "riesgos internos de la actividad). Toda cláusula "
                        "que exonere de esta responsabilidad es nula de "
                        "nulidad absoluta (art. 1292)."
                    ),
                    "clave": True,
                    "tags": ["transporte", "responsabilidad objetiva"],
                },
                {
                    "num": "1293-1294",
                    "titulo": "Responsabilidad por equipaje",
                    "resumen": (
                        "El transportista responde objetivamente (como "
                        "depositario necesario) por el equipaje entregado "
                        "para la bodega. Por el equipaje de mano que el "
                        "pasajero conserva consigo, solo responde si se "
                        "prueba su culpa o dolo. Se libera de objetos de "
                        "valor extraordinario o joyas no declaradas "
                        "previamente."
                    ),
                    "tags": ["transporte", "equipaje"],
                },
                {
                    "num": "1296-1302",
                    "titulo": "Transporte de cosas: cargador, carta de porte y guía",
                    "resumen": (
                        "El cargador debe declarar con exactitud el "
                        "contenido, peso y naturaleza de la carga, embalarla "
                        "adecuadamente y aportar la documentación exigida. La "
                        "carta de porte documenta el contrato; su 'segundo "
                        "ejemplar' es un título de crédito que permite "
                        "transmitir la propiedad de la mercadería en tránsito "
                        "mediante endoso o tradición."
                    ),
                    "tags": ["transporte de cosas", "carta de porte"],
                },
                {
                    "num": "1306",
                    "titulo": "Responsabilidad del transportista de cosas",
                    "resumen": (
                        "Es un deudor de resultado: responde objetivamente "
                        "por la pérdida o avería de las cosas transportadas. "
                        "Se exime probando caso fortuito ajeno a la "
                        "actividad, vicio propio de la cosa (ej. fruta que "
                        "fermenta sin cadena de frío), o culpa exclusiva del "
                        "cargador o destinatario."
                    ),
                    "clave": True,
                    "tags": ["transporte de cosas", "responsabilidad objetiva"],
                },
            ],
        },
        {
            "nombre": "Mandato",
            "rango": "arts. 1319-1334",
            "articulos": [
                {
                    "num": "1319",
                    "titulo": "Definición y aceptación tácita",
                    "resumen": (
                        "Hay contrato de mandato cuando una parte se obliga a "
                        "realizar uno o más actos jurídicos en interés de "
                        "otra. Puede conferirse y aceptarse expresa o "
                        "TÁCITAMENTE: si alguien sabe que otra persona está "
                        "haciendo algo en su interés y no lo impide pudiendo "
                        "hacerlo, se entiende que confirió mandato tácito. La "
                        "sola ejecución del mandato por el mandatario implica "
                        "su aceptación, aun sin mediar declaración expresa."
                    ),
                    "clave": True,
                    "tags": ["mandato", "definición"],
                },
                {
                    "num": "1320-1321",
                    "titulo": "Mandato con y sin representación",
                    "resumen": (
                        "Si el mandante confiere poder de representación, se "
                        "aplican además las reglas generales de la "
                        "representación voluntaria (arts. 362 y ss.): el "
                        "mandatario actúa a nombre del mandante y los efectos "
                        "del acto recaen directamente sobre este. Si NO se "
                        "otorga poder de representación, el mandatario actúa "
                        "en nombre PROPIO pero en interés del mandante: este "
                        "no queda obligado directamente frente al tercero, ni "
                        "el tercero frente a él (es el mismo esquema que la "
                        "consignación, que es un mandato sin representación "
                        "especializado en la venta de muebles)."
                    ),
                    "clave": True,
                    "tags": ["mandato", "representación"],
                },
                {
                    "num": "1322",
                    "titulo": "Onerosidad (presunción)",
                    "resumen": (
                        "El mandato se presume ONEROSO. A falta de acuerdo "
                        "sobre la retribución, la remuneración es la que "
                        "establecen las disposiciones legales o "
                        "reglamentarias aplicables, o el uso, o en su defecto "
                        "la que fija el juez."
                    ),
                    "tags": ["mandato", "onerosidad"],
                },
                {
                    "num": "1324",
                    "titulo": "Obligaciones del mandatario",
                    "resumen": (
                        "Debe cumplir los actos comprendidos en el mandato "
                        "conforme a las instrucciones dadas, con el cuidado "
                        "que pondría en los negocios propios (o mayor, si es "
                        "remunerado); informar al mandante sobre las "
                        "circunstancias relevantes; mantenerlo informado y "
                        "guardar reserva; y rendir cuentas de su gestión."
                    ),
                    "clave": True,
                    "tags": ["mandato", "obligaciones del mandatario"],
                },
                {
                    "num": "1325",
                    "titulo": "Conflicto de intereses",
                    "resumen": (
                        "Si media conflicto de intereses entre mandante y "
                        "mandatario, este debe posponer los suyos propios en "
                        "la ejecución del mandato, o renunciar. Es una "
                        "aplicación concreta del deber de lealtad propio de "
                        "todo mandato."
                    ),
                    "tags": ["mandato", "conflicto de intereses"],
                },
                {
                    "num": "1328",
                    "titulo": "Obligaciones del mandante",
                    "resumen": (
                        "Debe suministrar al mandatario los medios necesarios "
                        "para el cumplimiento del mandato, indemnizarle los "
                        "daños que sufra por causas no imputables a él, "
                        "liberarlo de las obligaciones asumidas frente a "
                        "terceros, y pagar la retribución pactada."
                    ),
                    "tags": ["mandato", "obligaciones del mandante"],
                },
                {
                    "num": "1329-1333",
                    "titulo": "Extinción del mandato",
                    "resumen": (
                        "Se extingue por: cumplimiento del negocio, "
                        "transcurso del plazo, revocación por el mandante, "
                        "renuncia del mandatario, muerte o incapacidad de "
                        "cualquiera de las partes. El mandato puede pactarse "
                        "IRREVOCABLE en ciertos supuestos (por ejemplo, si es "
                        "condición de un contrato bilateral o el medio para "
                        "cumplir una obligación ya contraída), en cuyo caso "
                        "el mandante no puede revocarlo unilateralmente."
                    ),
                    "clave": True,
                    "tags": ["mandato", "extinción", "mandato irrevocable"],
                },
                {
                    "num": "1334",
                    "titulo": "Rendición de cuentas",
                    "resumen": (
                        "El mandatario debe rendir cuentas de su gestión, "
                        "acompañadas de toda la documentación relativa a "
                        "ella, en el domicilio del mandante, salvo "
                        "estipulación en contrario."
                    ),
                    "tags": ["mandato", "rendición de cuentas"],
                },
            ],
        },
        {
            "nombre": "Consignación",
            "rango": "arts. 1335-1344",
            "articulos": [
                {
                    "num": "1335",
                    "titulo": "Concepto: mandato sin representación",
                    "resumen": (
                        "Es una especie de mandato SIN representación cuyo "
                        "objeto exclusivo es la venta de cosas muebles: el "
                        "consignatario vende a nombre propio pero por cuenta y "
                        "en interés del consignante, quedando él mismo "
                        "obligado frente a los terceros compradores (opacidad "
                        "representativa)."
                    ),
                    "clave": True,
                    "tags": ["consignación"],
                },
                {
                    "num": "1336-1342",
                    "titulo": "Obligaciones e instrucciones",
                    "resumen": (
                        "La aceptación de una parte del encargo implica "
                        "aceptar todo (indivisibilidad). El consignatario debe "
                        "ajustarse a las instrucciones del consignante, "
                        "conservar los bienes con diligencia de buen "
                        "comerciante, no puede vender a plazo sin "
                        "autorización, no puede comprar para sí los efectos ni "
                        "vender bienes propios al consignante (conflicto de "
                        "interés prohibido), y debe informar sobre los "
                        "créditos otorgados a terceros."
                    ),
                    "tags": ["consignación", "obligaciones"],
                },
                {
                    "num": "1340 y 1343",
                    "titulo": "Comisión y cláusula del credere",
                    "resumen": (
                        "El consignatario cobra una comisión por las ventas "
                        "concluidas. Mediante la cláusula del credere puede "
                        "pactarse que asuma solidariamente el riesgo de "
                        "insolvencia de los terceros compradores, a cambio de "
                        "una comisión adicional de garantía."
                    ),
                    "tags": ["consignación", "cláusula del credere"],
                },
            ],
        },
        {
            "nombre": "Corretaje",
            "rango": "arts. 1345-1355",
            "articulos": [
                {
                    "num": "1345",
                    "titulo": "Concepto y matriculación",
                    "resumen": (
                        "El corredor se obliga a mediar en la negociación y "
                        "conclusión de un contrato, sin relación de "
                        "dependencia ni representación de ninguna parte. "
                        "Exige matriculación profesional (Ley 20.266): sin "
                        "ella no puede reclamar el cobro de comisiones."
                    ),
                    "clave": True,
                    "tags": ["corretaje"],
                },
                {
                    "num": "1347-1348",
                    "titulo": "Obligaciones y prohibiciones",
                    "resumen": (
                        "Debe verificar títulos y datos, proponer los "
                        "negocios con exactitud y neutralidad, y guardar "
                        "secreto. Le está vedado adquirir para sí los bienes "
                        "que media, o representar intereses contrapuestos sin "
                        "autorización."
                    ),
                    "tags": ["corretaje", "obligaciones"],
                },
                {
                    "num": "1350-1352",
                    "titulo": "Derecho a la comisión",
                    "resumen": (
                        "Nace cuando el negocio mediado se concluye "
                        "definitivamente. Se mantiene el derecho al cobro "
                        "aunque el negocio luego se resuelva por condición "
                        "resolutoria cumplida, se rescinda de mutuo acuerdo, o "
                        "se resuelva por culpa de una de las partes (el "
                        "corredor cobra a la parte incumplidora)."
                    ),
                    "tags": ["corretaje", "comisión"],
                },
            ],
        },
        {
            "nombre": "Depósito",
            "rango": "arts. 1356-1377",
            "articulos": [
                {
                    "num": "1356-1357",
                    "titulo": "Definición y presunción de onerosidad",
                    "resumen": (
                        "Hay contrato de depósito cuando una parte "
                        "(depositario) se obliga a recibir de otra "
                        "(depositante) una cosa, con la obligación de "
                        "custodiarla y restituirla con sus frutos, si los "
                        "hubiera. Se presume ONEROSO (a diferencia de otros "
                        "contratos de guarda gratuitos como el comodato)."
                    ),
                    "clave": True,
                    "tags": ["depósito", "definición"],
                },
                {
                    "num": "1358",
                    "titulo": "Obligación del depositario",
                    "resumen": (
                        "Debe poner en la custodia de la cosa la diligencia "
                        "que usa para sus propias cosas, o la que corresponda "
                        "a su profesión (si es un depósito profesional, como "
                        "el bancario o el de un garaje, el estándar es más "
                        "exigente)."
                    ),
                    "clave": True,
                    "tags": ["depósito", "obligaciones"],
                },
                {
                    "num": "1368-1374",
                    "titulo": "Depósito en hoteles y establecimientos asimilables",
                    "resumen": (
                        "El depósito de los efectos introducidos por los "
                        "viajeros en un hotel se rige por reglas especiales: "
                        "el hotelero responde por el daño o pérdida de esos "
                        "efectos, incluso si no medió una entrega expresa "
                        "para custodia, mientras se encuentren dentro del "
                        "establecimiento. Se libera si el daño proviene de "
                        "caso fortuito ajeno a la actividad hotelera, o del "
                        "propio viajero o sus acompañantes. Puede limitarse "
                        "la responsabilidad por objetos de valor si el "
                        "viajero fue informado de la existencia de una caja "
                        "de seguridad y no la usó. Las normas del depósito en "
                        "hoteles se aplican también a establecimientos "
                        "asimilables (garajes, playas de estacionamiento, "
                        "clínicas, colegios) en lo pertinente."
                    ),
                    "clave": True,
                    "tags": ["depósito", "hoteles", "establecimientos asimilables"],
                },
            ],
        },
        {
            "nombre": "Mutuo y comodato",
            "rango": "arts. 1525-1541",
            "articulos": [
                {
                    "num": "1525-1527",
                    "titulo": "Mutuo: definición y onerosidad",
                    "resumen": (
                        "Hay contrato de mutuo cuando el mutuante se "
                        "compromete a entregar en propiedad una cantidad de "
                        "cosas fungibles, y el mutuario se obliga a devolver "
                        "igual cantidad de cosas de la misma calidad y "
                        "especie. A diferencia del comodato, el mutuo se "
                        "presume ONEROSO (salvo pacto en contrario o que se "
                        "trate de mutuo entre personas de confianza sin fines "
                        "comerciales), lo que lo distingue como préstamo de "
                        "consumo con transferencia de propiedad (el "
                        "mutuario puede disponer libremente de las cosas "
                        "recibidas, porque se hace dueño de ellas)."
                    ),
                    "clave": True,
                    "tags": ["mutuo", "definición"],
                },
                {
                    "num": "1529-1530",
                    "titulo": "Incumplimiento y vicios de la cosa mutuada",
                    "resumen": (
                        "Si el mutuario no cumple la obligación de devolver, "
                        "debe los daños causados. Si la cosa entregada era de "
                        "mala calidad o tenía vicios que causaron daños al "
                        "mutuario, el mutuante responde si conocía o debía "
                        "conocer esos defectos y no advirtió al mutuario."
                    ),
                    "tags": ["mutuo", "vicios"],
                },
                {
                    "num": "1533",
                    "titulo": "Comodato: definición",
                    "resumen": (
                        "Hay comodato cuando una parte se obliga a entregar a "
                        "otra una cosa no fungible, mueble o inmueble, para "
                        "que se sirva GRATUITAMENTE de ella y restituya la "
                        "misma cosa recibida. Es, por definición, un contrato "
                        "GRATUITO: si se pactara un precio, el negocio pasa a "
                        "ser locación, no comodato."
                    ),
                    "clave": True,
                    "tags": ["comodato", "definición"],
                },
                {
                    "num": "1541",
                    "titulo": "Extinción del comodato",
                    "resumen": (
                        "El comodato se extingue, entre otras causas, por la "
                        "muerte del comodatario (salvo que se haya pactado "
                        "para determinada persona y sus herederos), por la "
                        "destrucción de la cosa, por vencimiento del plazo o "
                        "cumplimiento del uso para el que se prestó, o por "
                        "voluntad unilateral del comodante si necesita la "
                        "cosa de forma imprevista y urgente."
                    ),
                    "tags": ["comodato", "extinción"],
                },
            ],
        },
        {
            "nombre": "Donación",
            "rango": "arts. 1542-1573, reformados por Ley 27.587 (2020)",
            "articulos": [
                {
                    "num": "1542",
                    "titulo": "Definición y actos mixtos",
                    "resumen": (
                        "Hay donación cuando una parte se obliga a transferir "
                        "gratuitamente una cosa a otra, y esta lo acepta "
                        "(animus donandi). Cuando se pacta una "
                        "contraprestación sustancialmente inferior al valor "
                        "real ('acto mixto', art. 1544), el negocio se rige "
                        "por las reglas onerosas en la porción cubierta por "
                        "la contraprestación, y por las de la donación en el "
                        "saldo gratuito."
                    ),
                    "clave": True,
                    "tags": ["donación", "definición"],
                },
                {
                    "num": "1552",
                    "titulo": "Forma: escritura pública bajo pena de nulidad",
                    "resumen": (
                        "Exige escritura pública, bajo sanción de nulidad "
                        "absoluta, para donaciones de inmuebles, muebles "
                        "registrables o prestaciones periódicas o vitalicias: "
                        "la solemnidad fuerza al donante a ser asesorado "
                        "notarialmente y a deliberar sobre un acto que lo "
                        "empobrece sin contraprestación."
                    ),
                    "clave": True,
                    "tags": ["donación", "forma"],
                },
                {
                    "num": "1565 y 2456",
                    "titulo": "Donaciones inoficiosas",
                    "resumen": (
                        "Una donación es inoficiosa cuando su cuantía excede "
                        "la porción disponible del patrimonio del donante al "
                        "momento de su fallecimiento, afectando la legítima "
                        "de los herederos forzosos."
                    ),
                    "tags": ["donación", "legítima"],
                },
                {
                    "num": "2458-2459 (reforma Ley 27.587)",
                    "titulo": "El giro de la Ley 27.587: protección del tercero de buena fe",
                    "resumen": (
                        "Antes de 2020, la acción de reducción de una "
                        "donación inoficiosa tenía efecto REIPERSECUTORIO: el "
                        "heredero perjudicado podía reivindicar el inmueble "
                        "incluso de un tercer comprador de buena fe, lo que "
                        "generaba 'títulos observables' que paralizaban el "
                        "mercado inmobiliario (rechazo de créditos "
                        "hipotecarios, desconfianza notarial). La Ley 27.587 "
                        "cambió el paradigma: si el tercer adquirente de un "
                        "inmueble es de buena fe y a título ONEROSO, su "
                        "dominio es INATACABLE (art. 2458); la pretensión del "
                        "heredero muta de una acción real sobre la cosa a una "
                        "acción PERSONAL de daños contra el donatario "
                        "original. Además, la acción no procede contra quien "
                        "posee el bien hace 10 años, y el mero conocimiento "
                        "de que el inmueble provino de una donación YA NO "
                        "destruye la buena fe del comprador (art. 2459). Esto "
                        "saneó masivamente los títulos y reactivó el mercado."
                    ),
                    "clave": True,
                    "tags": ["donación", "Ley 27.587", "títulos observables"],
                },
                {
                    "num": "1566 y ss.",
                    "titulo": "Pacto de reversión",
                    "resumen": (
                        "Condición resolutoria expresa: el bien vuelve al "
                        "donante si el donatario fallece antes que él, "
                        "evitando que el bien termine en manos de herederos "
                        "del donatario en lugar de regresar al donante."
                    ),
                    "tags": ["donación", "pacto de reversión"],
                },
                {
                    "num": "1569-1573",
                    "titulo": "Revocación por ingratitud",
                    "resumen": (
                        "Pese a ser en principio irrevocable, la donación "
                        "puede revocarse si el donatario incurre en: "
                        "atentados graves contra la vida del donante, "
                        "injurias graves a su honor, privación injusta de sus "
                        "bienes, o negativa infundada a prestarle alimentos "
                        "cuando puede hacerlo. La jurisprudencia exige un dolo "
                        "manifiesto (no cualquier distanciamiento familiar). "
                        "La acción caduca al año de conocido el hecho de "
                        "ingratitud."
                    ),
                    "clave": True,
                    "tags": ["donación", "revocación por ingratitud"],
                },
            ],
        },
        {
            "nombre": "Fianza",
            "rango": "arts. 1574-1598",
            "articulos": [
                {
                    "num": "1574",
                    "titulo": "Definición y caracteres",
                    "resumen": (
                        "Una persona se obliga accesoriamente por otra a "
                        "satisfacer una prestación en caso de incumplimiento "
                        "del deudor principal. Es un contrato directo entre "
                        "el ACREEDOR y el FIADOR (el deudor principal es un "
                        "tercero ajeno a ese contrato). Caracteres: "
                        "accesoria (sigue la suerte de la obligación "
                        "principal), subsidiaria (el fiador responde tras el "
                        "incumplimiento del deudor), unilateral y, salvo "
                        "pacto en contrario, gratuita."
                    ),
                    "clave": True,
                    "tags": ["fianza", "definición"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Tres tipos de fianza",
                    "resumen": (
                        "(1) Fianza SIMPLE: el fiador goza de los beneficios "
                        "de excusión y división. (2) Fianza SOLIDARIA (art. "
                        "1590): pactada expresamente o por renuncia a la "
                        "excusión; pierde la subsidiariedad procesal pero "
                        "conserva la accesoriedad (el fiador puede oponer las "
                        "defensas del deudor). (3) Principal PAGADOR (art. "
                        "1591): aunque se lo llame 'fiador', es un deudor "
                        "solidario liso y llano, sin accesoriedad ni "
                        "subsidiariedad."
                    ),
                    "clave": True,
                    "tags": ["fianza", "principal pagador"],
                },
                {
                    "num": "1578 y 1580",
                    "titulo": "Extensión y fianza de obligaciones futuras",
                    "resumen": (
                        "La fianza no puede ser más gravosa que la obligación "
                        "principal; comprende sus accesorios (intereses, "
                        "costas) salvo pacto en contrario. Puede afianzarse "
                        "obligaciones futuras o indeterminadas, pero exige "
                        "fijar un MONTO MÁXIMO y no puede extenderse por más "
                        "de 5 AÑOS: vencido ese plazo, la fianza se extingue "
                        "para las deudas futuras que nazcan después."
                    ),
                    "clave": True,
                    "tags": ["fianza", "obligaciones futuras"],
                },
                {
                    "num": "1583-1584",
                    "titulo": "Beneficio de excusión y sus excepciones",
                    "resumen": (
                        "El fiador simple puede exigir que el acreedor "
                        "primero ejecute los bienes del deudor principal. "
                        "Pierde este beneficio si: el deudor está en concurso "
                        "o quiebra, no puede ser demandado en el país o "
                        "carece de bienes aquí, la fianza es judicial, o el "
                        "fiador renunció al beneficio (frecuente en bancos)."
                    ),
                    "tags": ["fianza", "beneficio de excusión"],
                },
                {
                    "num": "1592-1594",
                    "titulo": "Efectos entre fiador y deudor principal",
                    "resumen": (
                        "El fiador que paga se subroga en todos los derechos, "
                        "acciones y garantías del acreedor contra el deudor "
                        "(art. 1592). Debe avisar al deudor antes de pagar; si "
                        "no lo hace y el deudor paga de nuevo por falta de "
                        "aviso, el fiador solo puede repetir contra el "
                        "acreedor de mala fe. El fiador puede pedir ser "
                        "liberado o exigir contragarantías si el deudor "
                        "dilapida bienes o transcurrieron 5 años de fianza "
                        "indeterminada."
                    ),
                    "tags": ["fianza", "subrogación"],
                },
                {
                    "num": "1596",
                    "titulo": "Causales especiales de extinción",
                    "resumen": (
                        "El fiador se libera —aunque la deuda principal "
                        "subsista— si: el acreedor, por su hecho, impide la "
                        "subrogación del fiador en garantías reales; se "
                        "prorroga el plazo de la deuda sin su consentimiento; "
                        "pasan 5 años de fianza de obligaciones futuras no "
                        "nacidas; o el acreedor no demanda al deudor dentro de "
                        "los 60 días de ser requerido por el fiador."
                    ),
                    "clave": True,
                    "tags": ["fianza", "extinción"],
                },
            ],
        },
        {
            "nombre": "Renta vitalicia y contratos aleatorios",
            "rango": "arts. 1599-1608",
            "articulos": [
                {
                    "num": "1599",
                    "titulo": "Renta vitalicia: definición y solemnidad",
                    "resumen": (
                        "A cambio de un capital u otra prestación, el deudor "
                        "se obliga a pagar una renta periódica a una o más "
                        "personas durante la vida de una o más personas "
                        "designadas. Debe celebrarse OBLIGATORIAMENTE por "
                        "escritura pública bajo pena de nulidad (art. 1601). "
                        "La renta se paga siempre en dinero (art. 1602); si "
                        "hay varios beneficiarios simultáneos y no se pactó lo "
                        "contrario, no hay derecho de acrecer entre ellos."
                    ),
                    "clave": True,
                    "tags": ["renta vitalicia"],
                },
                {
                    "num": "1604",
                    "titulo": "Resolución por falta de pago",
                    "resumen": (
                        "Ante la falta de pago sistemática de la renta, el "
                        "constituyente o sus herederos pueden pedir la "
                        "resolución del contrato y la restitución del "
                        "capital entregado."
                    ),
                    "tags": ["renta vitalicia", "resolución"],
                },
            ],
        },
        {
            "nombre": "Juego y apuesta",
            "rango": "arts. 1609-1613",
            "articulos": [
                {
                    "num": "1609-1610",
                    "titulo": "Juegos de destreza",
                    "resumen": (
                        "Cuando predomina la destreza física o intelectual, "
                        "confieren acción civil para exigir el cumplimiento. "
                        "El juez puede reducir prudencialmente la deuda si es "
                        "desproporcionada respecto del patrimonio del deudor."
                    ),
                    "tags": ["juego", "apuesta"],
                },
                {
                    "num": "1611",
                    "titulo": "Juegos de puro azar no autorizados",
                    "resumen": (
                        "No confieren acción civil para exigir su "
                        "cumplimiento. Rige la irrepetibilidad: si el deudor "
                        "pagó voluntariamente, no puede pedir la devolución "
                        "(salvo que quien pagó fuera incapaz)."
                    ),
                    "tags": ["juego", "azar"],
                },
                {
                    "num": "1613",
                    "titulo": "Juegos regulados por el Estado",
                    "resumen": (
                        "Loterías, quinielas y casinos autorizados quedan "
                        "sustraídos del derecho común y se rigen por las "
                        "normas administrativas locales que autorizaron su "
                        "funcionamiento."
                    ),
                    "tags": ["juego", "regulación estatal"],
                },
            ],
        },
        {
            "nombre": "Cesión de derechos y de posición contractual",
            "rango": "arts. 1614-1640",
            "articulos": [
                {
                    "num": "1614",
                    "titulo": "Definición y tipificación supletoria",
                    "resumen": (
                        "Hay cesión cuando una parte (cedente) transfiere a "
                        "otra (cesionario) un derecho. Se rige por las reglas "
                        "de la compraventa si hubo precio en dinero, de la "
                        "permuta si se dio otro bien, o de la donación si fue "
                        "gratuita, sin perder su autonomía como tipo "
                        "contractual propio."
                    ),
                    "clave": True,
                    "tags": ["cesión de derechos"],
                },
                {
                    "num": "1616-1617",
                    "titulo": "Objeto: regla de cesibilidad amplia",
                    "resumen": (
                        "Se presume que todo derecho es cesible, salvo "
                        "prohibición legal, incompatibilidad con su "
                        "naturaleza, o pacto en contrario. Son incesibles los "
                        "derechos inherentes a la persona humana "
                        "(personalísimos), aunque sus derivaciones "
                        "patrimoniales ya devengadas sí pueden cederse."
                    ),
                    "tags": ["cesión de derechos", "objeto"],
                },
                {
                    "num": "1618",
                    "titulo": "Forma",
                    "resumen": (
                        "Rige la forma escrita en general, y la escritura "
                        "pública para: cesión de derechos hereditarios, "
                        "cesión de derechos litigiosos sobre inmuebles, y "
                        "cesión de derechos que emanan de un acto celebrado "
                        "por escritura pública."
                    ),
                    "tags": ["cesión de derechos", "forma"],
                },
                {
                    "num": "1620-1622",
                    "titulo": "Efecto traslativo y notificación al deudor cedido",
                    "resumen": (
                        "Entre cedente y cesionario, el derecho se transmite "
                        "por el solo consentimiento (efecto traslativo "
                        "inmediato). Pero para ser OPONIBLE al deudor cedido y "
                        "a terceros, debe NOTIFICÁRSELO fehacientemente "
                        "(instrumento público o privado con fecha cierta), en "
                        "su domicilio real (no el domicilio especial del "
                        "contrato base). Antes de la notificación, el deudor "
                        "que paga de buena fe al cedente queda liberado. En "
                        "cesiones sucesivas del mismo crédito, prevalece el "
                        "cesionario que notificó PRIMERO al deudor, no quien "
                        "contrató primero."
                    ),
                    "clave": True,
                    "tags": ["cesión de derechos", "notificación", "oponibilidad"],
                },
                {
                    "num": "1636-1640",
                    "titulo": "Cesión de posición contractual (remisión)",
                    "resumen": (
                        "Ver desarrollo completo en Título II, Capítulo 14: "
                        "a diferencia de la cesión de un crédito aislado, "
                        "aquí se transmite la 'calidad de parte' entera "
                        "(teoría unitaria), y requiere el consentimiento del "
                        "contratante cedido."
                    ),
                    "tags": ["cesión de posición contractual"],
                },
            ],
        },
        {
            "nombre": "Transacción",
            "rango": "arts. 1641-1648",
            "articulos": [
                {
                    "num": "1641",
                    "titulo": "Definición",
                    "resumen": (
                        "Las partes, haciéndose concesiones recíprocas, "
                        "extinguen obligaciones dudosas o litigiosas, para "
                        "evitar un litigio futuro o poner fin a uno ya "
                        "iniciado."
                    ),
                    "clave": True,
                    "tags": ["transacción"],
                },
                {
                    "num": "1642-1643",
                    "titulo": "Efecto de cosa juzgada y forma",
                    "resumen": (
                        "Tiene, entre las partes, los efectos de la cosa "
                        "juzgada sustancial, sin requerir homologación "
                        "judicial previa. Si versa sobre derechos ya "
                        "litigiosos, solo produce efectos procesales desde "
                        "que se presenta por escrito ante el juzgado. Es un "
                        "contrato FORMAL: requiere forma escrita."
                    ),
                    "clave": True,
                    "tags": ["transacción", "cosa juzgada"],
                },
                {
                    "num": "1645-1647",
                    "titulo": "Causales de nulidad",
                    "resumen": (
                        "Es nula si versa sobre una obligación originaria "
                        "sustancialmente nula (salvo que las partes hayan "
                        "transado expresamente sobre la nulidad misma), si "
                        "hay vicios del consentimiento (error, dolo, "
                        "violencia), o si recae sobre un litigio ya resuelto "
                        "por sentencia firme que la parte impugnante "
                        "ignoraba de buena fe."
                    ),
                    "tags": ["transacción", "nulidad"],
                },
            ],
        },
        {
            "nombre": "Arbitraje",
            "rango": "arts. 1649-1665",
            "articulos": [
                {
                    "num": "1649",
                    "titulo": "Definición y objeto",
                    "resumen": (
                        "Hay contrato de arbitraje cuando las partes deciden "
                        "someter a la decisión de uno o más árbitros todas o "
                        "algunas de las controversias que hayan surgido o "
                        "puedan surgir entre ellas respecto de una "
                        "determinada relación jurídica, contractual o no "
                        "contractual, de derecho privado, EN LA QUE NO SE "
                        "ENCUENTRE COMPROMETIDO EL ORDEN PÚBLICO. La doctrina "
                        "mayoritaria aclara que el límite no pasa por que la "
                        "materia esté regulada por normas de orden público "
                        "(eso no la vuelve, por sí solo, no arbitrable), sino "
                        "por la DISPONIBILIDAD de los derechos en juego: solo "
                        "son arbitrables los derechos patrimoniales de los "
                        "que las partes pueden disponer libremente."
                    ),
                    "clave": True,
                    "tags": ["arbitraje", "definición", "arbitrabilidad"],
                },
                {
                    "num": "1650-1651",
                    "titulo": "Forma escrita y controversias excluidas",
                    "resumen": (
                        "El acuerdo arbitral debe ser escrito (alcanza con un "
                        "principio de prueba escrita), pudiendo constar en "
                        "una cláusula compromisoria dentro de un contrato, en "
                        "un acuerdo independiente, o en un estatuto o "
                        "reglamento. Quedan EXCLUIDAS del arbitraje, entre "
                        "otras materias: las cuestiones de estado civil o "
                        "capacidad de las personas, las de familia, los "
                        "derechos de usuarios y consumidores, los contratos "
                        "por adhesión (cualquiera sea su objeto) y las "
                        "derivadas de relaciones laborales. Además, este "
                        "capítulo no se aplica a controversias en que sea "
                        "parte el Estado nacional o local."
                    ),
                    "clave": True,
                    "tags": ["arbitraje", "forma", "materias excluidas"],
                },
                {
                    "num": "1652",
                    "titulo": "Clases de arbitraje",
                    "resumen": (
                        "Arbitraje DE DERECHO: los árbitros deben resolver "
                        "aplicando el derecho vigente. Arbitraje DE EQUIDAD "
                        "(arbitradores o amigables componedores): los "
                        "árbitros resuelven según su leal saber y entender. "
                        "Si el convenio arbitral no aclara cuál de los dos "
                        "es, SE PRESUME que es de derecho."
                    ),
                    "tags": ["arbitraje", "arbitraje de derecho", "amigables componedores"],
                },
                {
                    "num": "1653-1654",
                    "titulo": "Autonomía del contrato de arbitraje y competencia-competencia",
                    "resumen": (
                        "El contrato de arbitraje es AUTÓNOMO respecto del "
                        "contrato principal en el que está inserto: la "
                        "nulidad de este último no arrastra la nulidad de la "
                        "cláusula arbitral, por lo que los árbitros conservan "
                        "competencia incluso para juzgar esa nulidad "
                        "('separabilidad'). Además, salvo pacto en contrario, "
                        "los propios árbitros tienen la atribución de decidir "
                        "sobre su propia competencia, incluso sobre las "
                        "excepciones relativas a la existencia o validez del "
                        "convenio arbitral (principio 'kompetenz-kompetenz')."
                    ),
                    "clave": True,
                    "tags": ["arbitraje", "autonomía", "competencia-competencia"],
                },
                {
                    "num": "1656",
                    "titulo": "Efectos: exclusión de la jurisdicción judicial",
                    "resumen": (
                        "El convenio arbitral obliga a las partes a cumplir "
                        "lo estipulado y EXCLUYE la competencia de los "
                        "tribunales judiciales sobre las controversias "
                        "sometidas a arbitraje (salvo que el tribunal "
                        "arbitral no esté aún interviniendo y el convenio "
                        "parezca manifiestamente nulo o inaplicable: en caso "
                        "de duda, se estará a la mayor eficacia del contrato "
                        "de arbitraje). Los laudos pueden revisarse "
                        "judicialmente solo por CAUSALES TAXATIVAS DE "
                        "NULIDAD (vicios graves del procedimiento o "
                        "violación del orden público), nunca por el fondo de "
                        "lo decidido (no se admite una revisión de "
                        "'errores in iudicando'): las partes no pueden "
                        "renunciar a esta impugnación por nulidad si el laudo "
                        "fuera contrario al ordenamiento jurídico."
                    ),
                    "clave": True,
                    "tags": ["arbitraje", "efectos", "revisión judicial del laudo"],
                },
                {
                    "num": "1657",
                    "titulo": "Arbitraje institucional",
                    "resumen": (
                        "Las partes pueden encomendar la administración del "
                        "arbitraje y la designación de árbitros a "
                        "asociaciones civiles u otras entidades (nacionales o "
                        "extranjeras) cuyos estatutos lo prevean (ej. la "
                        "Bolsa de Comercio de Buenos Aires, cámaras de "
                        "comercio, colegios profesionales). Los reglamentos "
                        "de esas entidades rigen todo el proceso e integran "
                        "el contrato de arbitraje."
                    ),
                    "tags": ["arbitraje", "arbitraje institucional"],
                },
                {
                    "num": "1665",
                    "titulo": "Extinción de la competencia de los árbitros",
                    "resumen": (
                        "La competencia de los árbitros se extingue con el "
                        "dictado del laudo definitivo, salvo para resolver "
                        "aclaratorias o complementarias según lo pactado por "
                        "las partes."
                    ),
                    "tags": ["arbitraje", "extinción de competencia"],
                },
            ],
        },
        {
            "nombre": "Fideicomiso",
            "rango": "arts. 1666-1707",
            "articulos": [
                {
                    "num": "1666",
                    "titulo": "Definición y los cuatro sujetos",
                    "resumen": (
                        "Hay contrato de fideicomiso cuando una parte "
                        "(FIDUCIANTE) transmite o se compromete a transmitir "
                        "la propiedad de bienes a otra (FIDUCIARIO), quien se "
                        "obliga a ejercerla en beneficio de otra "
                        "(BENEFICIARIO) —designada en el contrato— y a "
                        "transmitirla al cumplirse un plazo o condición al "
                        "FIDEICOMISARIO. Estos cuatro roles pueden recaer en "
                        "menos de cuatro personas (el fiduciante puede ser a "
                        "la vez beneficiario o fideicomisario), salvo que el "
                        "fiduciario sea también el único beneficiario."
                    ),
                    "clave": True,
                    "tags": ["fideicomiso", "definición"],
                },
                {
                    "num": "1667",
                    "titulo": "Contenido obligatorio del contrato",
                    "resumen": (
                        "Debe individualizar los bienes objeto (o, si no es "
                        "posible al momento de contratar, describir los "
                        "requisitos que deben reunir); determinar el modo de "
                        "incorporar otros bienes; fijar el plazo o condición "
                        "a que se sujeta la propiedad fiduciaria; establecer "
                        "los derechos y obligaciones del fiduciario y el modo "
                        "de sustituirlo; los derechos del beneficiario; y el "
                        "destino de los bienes al finalizar el fideicomiso, "
                        "con indicación del fideicomisario."
                    ),
                    "tags": ["fideicomiso", "contenido"],
                },
                {
                    "num": "1668",
                    "titulo": "Plazo máximo",
                    "resumen": (
                        "El fideicomiso NO puede durar más de 30 años desde "
                        "su celebración, salvo que el beneficiario sea "
                        "incapaz o con capacidad restringida, en cuyo caso "
                        "puede durar hasta que cese esa incapacidad o "
                        "restricción. Si se pacta un plazo mayor, se reduce "
                        "automáticamente al máximo legal. Cumplida la "
                        "condición o vencido el plazo, cesa el fideicomiso y "
                        "el fiduciario debe transmitir los bienes a quien se "
                        "designó (a falta de estipulación, al fiduciante o "
                        "sus herederos)."
                    ),
                    "clave": True,
                    "tags": ["fideicomiso", "plazo"],
                },
                {
                    "num": "1669-1670",
                    "titulo": "Forma y objeto",
                    "resumen": (
                        "Se instrumenta por escritura pública o instrumento "
                        "privado (salvo que la naturaleza de los bienes exija "
                        "escritura pública), y debe inscribirse en el "
                        "registro correspondiente. Pueden ser objeto todos "
                        "los bienes que están en el comercio, incluso "
                        "universalidades, PERO NO las herencias futuras."
                    ),
                    "tags": ["fideicomiso", "forma", "objeto"],
                },
                {
                    "num": "1671-1672",
                    "titulo": "Beneficiario y fideicomisario",
                    "resumen": (
                        "El beneficiario puede ser una persona que exista o "
                        "no al momento del contrato (en ese caso deben "
                        "constar los datos para su individualización futura), "
                        "y puede ser el propio fiduciante, el fiduciario o el "
                        "fideicomisario. Si ningún beneficiario acepta, "
                        "renuncia o llega a existir, se entiende que el "
                        "beneficiario es el fideicomisario. El fideicomisario "
                        "es quien recibe la propiedad al finalizar el "
                        "fideicomiso; también puede coincidir con el "
                        "fiduciante o el beneficiario."
                    ),
                    "tags": ["fideicomiso", "beneficiario", "fideicomisario"],
                },
                {
                    "num": "1680",
                    "titulo": "Fideicomiso en garantía",
                    "resumen": (
                        "Si el fideicomiso se constituye con fines de "
                        "garantía, el fiduciario puede aplicar las sumas de "
                        "dinero que ingresen (incluso por cobro judicial de "
                        "créditos fideicomitidos) al pago de los créditos "
                        "garantizados, y puede disponer de otros bienes según "
                        "lo pactado (o, en su defecto, en forma privada o "
                        "judicial), procurando el mayor valor posible para no "
                        "perjudicar al fiduciante."
                    ),
                    "clave": True,
                    "tags": ["fideicomiso", "fideicomiso en garantía"],
                },
                {
                    "num": "cátedra",
                    "titulo": "El patrimonio fiduciario como patrimonio separado",
                    "resumen": (
                        "Los bienes fideicomitidos constituyen un patrimonio "
                        "separado tanto del patrimonio del fiduciario como "
                        "del fiduciante: no responden por las deudas de "
                        "ninguno de ellos, salvo la propia obligación "
                        "contraída en la ejecución del fideicomiso. Esta "
                        "separación patrimonial es la base técnica que "
                        "explica su uso masivo en el financiamiento de "
                        "proyectos inmobiliarios ('fideicomisos al costo') y "
                        "como garantía de créditos (fideicomiso en garantía), "
                        "porque aísla el activo de los riesgos de insolvencia "
                        "de las partes."
                    ),
                    "clave": True,
                    "tags": ["fideicomiso", "patrimonio separado"],
                },
            ],
        },
        {
            "nombre": "Agencia, concesión y franquicia (contratos de distribución comercial)",
            "rango": "arts. 1479-1524",
            "articulos": [
                {
                    "num": "1479",
                    "titulo": "Agencia: definición",
                    "resumen": (
                        "Hay contrato de agencia cuando una parte (agente) "
                        "se obliga a promover negocios por cuenta de otra "
                        "(preponente o empresario), de manera ESTABLE, "
                        "CONTINUADA E INDEPENDIENTE, sin relación laboral, "
                        "mediante una retribución. El agente es un "
                        "intermediario independiente: no asume el riesgo de "
                        "las operaciones que promueve ni representa al "
                        "preponente (a diferencia del mandatario con "
                        "representación, el agente solo acerca el negocio; "
                        "la conclusión del contrato queda, en principio, en "
                        "manos del preponente). Debe instrumentarse por "
                        "escrito."
                    ),
                    "clave": True,
                    "tags": ["agencia", "definición"],
                },
                {
                    "num": "1480",
                    "titulo": "Exclusividad del agente",
                    "resumen": (
                        "El agente tiene derecho a la exclusividad en el "
                        "ramo de negocios, zona geográfica o grupo de "
                        "personas determinados en el contrato. La doctrina "
                        "discute si la exclusividad es un elemento "
                        "esencial o meramente natural del contrato de "
                        "agencia (el art. 1499 sugiere que no es esencial, "
                        "al hablar de 'si el contrato prevé la "
                        "exclusividad')."
                    ),
                    "tags": ["agencia", "exclusividad"],
                },
                {
                    "num": "1502",
                    "titulo": "Concesión: definición",
                    "resumen": (
                        "Hay contrato de concesión cuando el concesionario, "
                        "que actúa en NOMBRE Y POR CUENTA PROPIA frente a "
                        "terceros, se obliga mediante una retribución a "
                        "disponer de su organización empresaria para "
                        "comercializar mercaderías provistas por el "
                        "concedente, prestar los servicios y proveer los "
                        "repuestos y accesorios convenidos. A diferencia del "
                        "agente, el concesionario COMPRA los productos al "
                        "concedente y los revende por su cuenta y riesgo: su "
                        "ganancia surge del margen entre el precio de compra "
                        "y el de reventa (típico de las concesionarias de "
                        "automotores)."
                    ),
                    "clave": True,
                    "tags": ["concesión", "definición"],
                },
                {
                    "num": "1503",
                    "titulo": "Exclusividad en la concesión",
                    "resumen": (
                        "Salvo pacto en contrario: (a) la concesión es "
                        "EXCLUSIVA para ambas partes en el territorio o zona "
                        "de influencia determinados (el concedente no puede "
                        "autorizar otra concesión en la misma zona, y el "
                        "concesionario no puede actuar fuera de ella ni "
                        "vender productos competidores); (b) la concesión "
                        "comprende todas las mercaderías fabricadas o "
                        "provistas por el concedente, incluidos los nuevos "
                        "modelos."
                    ),
                    "clave": True,
                    "tags": ["concesión", "exclusividad"],
                },
                {
                    "num": "1506",
                    "titulo": "Plazo mínimo de la concesión",
                    "resumen": (
                        "El plazo NO puede ser inferior a 4 años (o 2 años si "
                        "es el propio concedente quien provee las "
                        "instalaciones al concesionario). Si se pacta un "
                        "plazo menor, o el contrato es de plazo "
                        "indeterminado, SE TIENE POR CONVENIDO el plazo "
                        "mínimo legal: es una norma de orden público que "
                        "presume que recién a partir de esos años se cumplió "
                        "mínimamente la finalidad económica del negocio "
                        "(amortizar la inversión en infraestructura, "
                        "capacitación, stock)."
                    ),
                    "clave": True,
                    "tags": ["concesión", "plazo mínimo"],
                },
                {
                    "num": "1492-1493",
                    "titulo": "Preaviso y sus consecuencias (aplicable a agencia y concesión)",
                    "resumen": (
                        "Vencido el plazo mínimo, la parte que desea "
                        "extinguir el contrato de duración indeterminada "
                        "debe dar un PREAVISO cuya extensión se calcula, como "
                        "pauta, en un mes por cada año de vigencia del "
                        "contrato (hasta un máximo). Si el preaviso omitido o "
                        "insuficiente, quien rescinde debe indemnizar los "
                        "daños causados por la omisión, incluyendo las "
                        "ganancias dejadas de percibir en el lapso que "
                        "hubiera durado un preaviso suficiente. Este régimen "
                        "consolidó una línea jurisprudencial previa al "
                        "Código en materia de concesiones y agencias "
                        "rescindidas intempestivamente."
                    ),
                    "clave": True,
                    "tags": ["agencia", "concesión", "preaviso", "rescisión"],
                },
                {
                    "num": "1511",
                    "titulo": "Distribución: remisión a las normas de la concesión",
                    "resumen": (
                        "El Código no le da un tratamiento autónomo al "
                        "contrato de distribución (otro contrato de "
                        "comercialización habitual en la práctica, sin la "
                        "exclusividad total de la concesión): se rige por "
                        "las normas de la concesión en cuanto sean "
                        "pertinentes."
                    ),
                    "tags": ["distribución", "concesión"],
                },
                {
                    "num": "1512",
                    "titulo": "Franquicia: definición",
                    "resumen": (
                        "Hay franquicia comercial cuando una parte "
                        "(franquiciante) otorga a otra (franquiciado) el "
                        "derecho a utilizar un SISTEMA PROBADO destinado a "
                        "comercializar bienes o servicios bajo el nombre "
                        "comercial, emblema o marca del franquiciante, quien "
                        "provee un conjunto de conocimientos técnicos "
                        "(know-how) y asistencia técnica o comercial "
                        "continua, a cambio de una prestación del "
                        "franquiciado. El franquiciante debe ser titular "
                        "exclusivo de los derechos intelectuales, marcas y "
                        "patentes del sistema, y no puede tener participación "
                        "accionaria de control en el negocio del "
                        "franquiciado (para preservar su independencia "
                        "jurídica y patrimonial)."
                    ),
                    "clave": True,
                    "tags": ["franquicia", "definición", "know-how"],
                },
                {
                    "num": "1514",
                    "titulo": "Obligaciones del franquiciante",
                    "resumen": (
                        "Debe proveer información económica y financiera "
                        "sobre la evolución del sistema (deber "
                        "PRECONTRACTUAL: el franquiciado debe poder evaluar "
                        "el éxito real de la red antes de contratar), y "
                        "brindar asistencia técnica y de mercado continua "
                        "durante la ejecución del contrato."
                    ),
                    "tags": ["franquicia", "obligaciones del franquiciante"],
                },
                {
                    "num": "1516",
                    "titulo": "Plazo de la franquicia",
                    "resumen": (
                        "Se aplica el mismo plazo mínimo de la concesión (4 "
                        "años), salvo situaciones especiales de duración "
                        "inferior por naturaleza (ferias, congresos, "
                        "emprendimientos temporales). Al vencer el plazo, el "
                        "contrato se prorroga TÁCITAMENTE por períodos "
                        "sucesivos de 1 año, salvo denuncia expresa de una "
                        "parte con 30 días de anticipación; a la SEGUNDA "
                        "renovación, el contrato se transforma en uno de "
                        "plazo indeterminado."
                    ),
                    "clave": True,
                    "tags": ["franquicia", "plazo"],
                },
                {
                    "num": "1517-1518",
                    "titulo": "Exclusividad y prohibición de ceder",
                    "resumen": (
                        "Las franquicias son exclusivas para AMBAS partes "
                        "(salvo que se limite o excluya expresamente): el "
                        "franquiciante no puede autorizar otra unidad en el "
                        "mismo territorio sin consentimiento del "
                        "franquiciado, y este no puede operar unidades o "
                        "actividades competitivas. Salvo pacto en contrario, "
                        "el franquiciado NO puede ceder su posición "
                        "contractual ni sus derechos (excepto los de "
                        "contenido dinerario) mientras el contrato esté "
                        "vigente — salvedad hecha de las franquicias "
                        "mayoristas destinadas a otorgar subfranquicias."
                    ),
                    "clave": True,
                    "tags": ["franquicia", "exclusividad", "cesión"],
                },
                {
                    "num": "1519",
                    "titulo": "Cláusulas nulas",
                    "resumen": (
                        "No son válidas las cláusulas que prohíban al "
                        "franquiciado cuestionar justificadamente los "
                        "derechos del franquiciante sobre el sistema, la "
                        "marca o el know-how: es una protección análoga, en "
                        "su lógica, al control de cláusulas abusivas de los "
                        "contratos de adhesión."
                    ),
                    "clave": True,
                    "tags": ["franquicia", "cláusulas nulas"],
                },
                {
                    "num": "1520-1521",
                    "titulo": "Independencia de las partes y responsabilidad por defectos del sistema",
                    "resumen": (
                        "Las partes del contrato de franquicia son jurídica "
                        "y económicamente INDEPENDIENTES: no existe relación "
                        "laboral, de representación ni de sociedad entre "
                        "ellas (por eso, en principio, el franquiciante no "
                        "responde por las deudas del franquiciado frente a "
                        "terceros). Sin embargo, el franquiciante SÍ "
                        "responde frente al franquiciado por los defectos de "
                        "diseño del sistema que le fue transmitido, no "
                        "atribuibles a la gestión de este último."
                    ),
                    "clave": True,
                    "tags": ["franquicia", "responsabilidad"],
                },
                {
                    "num": "1523",
                    "titulo": "Derecho de la competencia",
                    "resumen": (
                        "El contrato de franquicia, por sí mismo, NO debe "
                        "considerarse un pacto que limite, restrinja o "
                        "distorsione la competencia: las cláusulas de "
                        "exclusividad territorial son inherentes a su "
                        "funcionamiento y no se presumen anticompetitivas."
                    ),
                    "tags": ["franquicia", "derecho de la competencia"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Los contratos de distribución comercial como red conexa",
                    "resumen": (
                        "Agencia, concesión, distribución y franquicia "
                        "comparten una lógica común: permiten a una empresa "
                        "(el preponente/concedente/franquiciante) extender "
                        "su llegada al mercado sin asumir directamente los "
                        "costos y riesgos de una red propia de sucursales, "
                        "trasladando parte de esa carga a un tercero "
                        "jurídicamente independiente pero económicamente "
                        "subordinado. Esta asimetría explica por qué el "
                        "Código consagra reglas protectorias específicas "
                        "(plazo mínimo, preaviso indemnizable, cláusulas "
                        "nulas en la franquicia) análogas, en su función, a "
                        "las que protegen al adherente en los contratos por "
                        "adhesión — y por qué, frecuentemente, se los "
                        "analiza en conexidad con otros contratos del mismo "
                        "sistema (financiamiento, seguros, planes de ahorro)."
                    ),
                    "clave": True,
                    "tags": ["agencia", "concesión", "franquicia", "conexidad"],
                },
            ],
        },
        {
            "nombre": "Contratos bancarios (parte general y específicos)",
            "rango": "arts. 1378-1428",
            "articulos": [
                {
                    "num": "1378",
                    "titulo": "Doble estándar: corporativo vs. consumidor",
                    "resumen": (
                        "Rige cuando los contratos son celebrados por "
                        "entidades financieras autorizadas por el BCRA. En "
                        "operaciones CORPORATIVAS prima la autonomía de la "
                        "voluntad. En operaciones con CONSUMIDORES (art. 1092 "
                        "CCyC y LDC), se integra con el microsistema de "
                        "consumo, de orden público."
                    ),
                    "clave": True,
                    "tags": ["contratos bancarios"],
                },
                {
                    "num": "1379-1381",
                    "titulo": "Transparencia: publicidad, contenido mínimo y nulidad de remisiones",
                    "resumen": (
                        "La publicidad de créditos debe informar de forma "
                        "clara el Costo Financiero Total (CFT), la TNA y la "
                        "TEA. El contrato debe detallar por escrito tasas "
                        "compensatorias y moratorias, comisiones y gastos. "
                        "Son NULAS las cláusulas que remitan de forma vaga a "
                        "'saldos' o reglamentos internos no incorporados "
                        "expresamente al contrato."
                    ),
                    "clave": True,
                    "tags": ["contratos bancarios", "transparencia"],
                },
                {
                    "num": "1386",
                    "titulo": "Forma escrita obligatoria",
                    "resumen": (
                        "Los contratos bancarios de consumo deben "
                        "instrumentarse por escrito (papel o soporte digital "
                        "con firma electrónica, garantizando legibilidad e "
                        "inmutabilidad). Su omisión es imputable al banco y "
                        "acarrea la nulidad del contrato."
                    ),
                    "tags": ["contratos bancarios", "forma"],
                },
                {
                    "num": "1389",
                    "titulo": "Rescisión unilateral en contratos de plazo indeterminado",
                    "resumen": (
                        "El cliente puede rescindir en cualquier momento, "
                        "gratis y sin causa. El banco puede rescindir, pero "
                        "debe dar un preaviso razonable (no menor a 30 días) "
                        "y no puede hacerlo de forma abusiva o discriminatoria."
                    ),
                    "tags": ["contratos bancarios", "rescisión"],
                },
                {
                    "num": "1390 y 1408",
                    "titulo": "Depósito bancario y mutuo bancario",
                    "resumen": (
                        "Depósito: el cliente transfiere la propiedad del "
                        "dinero al banco, que se obliga a restituirlo a la "
                        "vista o al vencimiento pactado, pudiendo disponer "
                        "libremente de los fondos mientras tanto. Mutuo: el "
                        "banco entrega dinero en propiedad al cliente, quien "
                        "debe restituir una cantidad equivalente con los "
                        "intereses pactados."
                    ),
                    "tags": ["depósito bancario", "mutuo bancario"],
                },
                {
                    "num": "1413-1417",
                    "titulo": "Caja de seguridad: responsabilidad objetiva y límites a las cláusulas",
                    "resumen": (
                        "El banco responde objetivamente (obligación de "
                        "resultado) por la idoneidad de la custodia. El robo "
                        "o hurto de la entidad NO es caso fortuito: es un "
                        "riesgo propio y previsible de la actividad bancaria. "
                        "Son nulas las cláusulas de exoneración total; los "
                        "topes de indemnización solo son válidos si se "
                        "informaron claramente antes de contratar y no "
                        "desnaturalizan la obligación de custodia. Dado el "
                        "secreto del contenido, la jurisprudencia admite "
                        "prueba por presunciones (nivel de ingresos, "
                        "extracciones previas, testigos)."
                    ),
                    "clave": True,
                    "tags": ["caja de seguridad", "responsabilidad objetiva"],
                },
                {
                    "num": "Ley 25.065",
                    "titulo": "Tarjeta de crédito: impugnación y reforma del DNU 70/2023",
                    "resumen": (
                        "Sistema en red de contratos conexos (emisor, titular, "
                        "comercios adheridos). El titular tiene 30 días para "
                        "impugnar su resumen; mientras se tramita, no se "
                        "pueden cobrar los montos cuestionados ni "
                        "inhabilitar la tarjeta si se paga el resto. El DNU "
                        "70/2023 desreguló fuertemente el sistema: habilitó "
                        "emisores no bancarios (fintechs), equiparó tarjetas "
                        "físicas y virtuales, eliminó el control estatal "
                        "previo de los contratos tipo, liberó las tasas de "
                        "interés (manteniendo la prohibición de capitalizar "
                        "punitorios) y habilitó cargos fijos por mora antes "
                        "prohibidos. La contracara es un mayor control "
                        "judicial ex post por abuso del derecho (art. 10) y "
                        "usura (art. 771)."
                    ),
                    "clave": True,
                    "tags": ["tarjeta de crédito", "DNU 70/2023"],
                },
                {
                    "num": "cátedra",
                    "titulo": "Phishing bancario: responsabilidad concurrente",
                    "resumen": (
                        "La jurisprudencia comercial reciente, ante estafas de "
                        "phishing o vishing (ingeniería social telefónica), "
                        "tiende a distribuir la responsabilidad entre el "
                        "banco (por fallas en sus sistemas de alerta y "
                        "seguridad informática) y el cliente (si facilitó "
                        "voluntariamente claves o instaló software de acceso "
                        "remoto a pedido de un desconocido), aplicando la "
                        "doctrina de la causalidad concurrente para morigerar "
                        "la condena, sin eximir totalmente al banco de su "
                        "deber de seguridad informática."
                    ),
                    "clave": True,
                    "tags": ["phishing", "responsabilidad bancaria"],
                },
            ],
        },
    ],
}

TITULOS = {
    "obligaciones": TITULO_I_OBLIGACIONES,
    "contratos_general": TITULO_II_CONTRATOS_GENERAL,
    "contratos_consumo": TITULO_III_CONSUMO,
    "contratos_particular": TITULO_IV_PARTICULARES,
}


def _articulos_de_titulo(titulo_dict):
    """Aplana los artículos (si existen) de todos los capítulos de un título."""
    articulos = []
    for capitulo in titulo_dict["capitulos"]:
        for art in capitulo.get("articulos", []):
            articulos.append({
                **art,
                "capitulo": capitulo["nombre"],
                "titulo_libro": titulo_dict["nombre"],
            })
    return articulos


def obtener_todos_los_articulos():
    """Aplana los artículos de TODOS los títulos que tienen detalle
    artículo por artículo, para alimentar el buscador."""
    articulos = []
    for titulo_dict in TITULOS.values():
        articulos.extend(_articulos_de_titulo(titulo_dict))
    return articulos
