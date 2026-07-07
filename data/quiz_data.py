"""
Banco de preguntas para el módulo de autoevaluación.
Cada pregunta referencia el/los artículos del CCyC en los que se basa,
para que el estudiante pueda ir a repasar la fuente.
"""

PREGUNTAS = [
    {
        "id": "q1",
        "tema": "Definición y elementos",
        "pregunta": "Según el art. 957 CCyC, el contrato requiere que las partes manifiesten su consentimiento para crear, regular, modificar, transferir o extinguir relaciones jurídicas:",
        "opciones": [
            "De cualquier naturaleza",
            "Patrimoniales",
            "Solo obligacionales de dar sumas de dinero",
            "Extrapatrimoniales",
        ],
        "correcta": 1,
        "explicacion": (
            "El objeto de la relación jurídica regulada por el contrato debe ser "
            "patrimonial (art. 957). Por eso actos como el matrimonio, que crean "
            "relaciones jurídicas de familia, no son 'contratos' en este sentido "
            "técnico, aunque compartan la estructura de acuerdo de voluntades."
        ),
    },
    {
        "id": "q2",
        "tema": "Formación del consentimiento",
        "pregunta": "Un cartel en una vidriera que dice 'Zapatillas $50.000' dirigido al público en general es, en principio, jurídicamente:",
        "opciones": [
            "Una oferta vinculante que cualquiera puede aceptar",
            "Una invitación a ofertar (art. 973)",
            "Un contrato ya perfeccionado",
            "Una promesa unilateral",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 973 establece que la oferta dirigida a personas indeterminadas "
            "se considera invitación a ofertar, salvo que de sus términos o "
            "circunstancias resulte la intención de contratar (por ejemplo, si se "
            "especifican cantidad y condiciones claras de venta directa)."
        ),
    },
    {
        "id": "q3",
        "tema": "Formación del consentimiento",
        "pregunta": "¿Qué teoría adopta el CCyC para determinar cuándo se perfecciona el contrato entre ausentes?",
        "opciones": [
            "Teoría de la declaración",
            "Teoría de la expedición",
            "Teoría de la recepción (art. 980)",
            "Teoría del conocimiento",
        ],
        "correcta": 2,
        "explicacion": (
            "El art. 980 adopta la teoría de la recepción: entre ausentes, el "
            "contrato se perfecciona cuando la aceptación es recibida por el "
            "proponente durante el plazo de vigencia de la oferta (no cuando el "
            "aceptante la envía, ni cuando el oferente efectivamente la lee)."
        ),
    },
    {
        "id": "q4",
        "tema": "Buena fe y responsabilidad precontractual",
        "pregunta": "Si una parte rompe intempestiva y arbitrariamente las tratativas precontractuales, generando gastos a la otra parte que confió en que el negocio se celebraría, ¿qué debe reparar?",
        "opciones": [
            "El interés positivo (como si el contrato se hubiera cumplido)",
            "El interés negativo o de confianza (los gastos y pérdidas por haber confiado)",
            "Nada, porque las tratativas no obligan",
            "El lucro cesante del contrato futuro",
        ],
        "correcta": 1,
        "explicacion": (
            "Arts. 990 y 991: las partes son libres de abandonar las tratativas, "
            "pero deben hacerlo de buena fe. Si las frustran arbitrariamente, "
            "responden por el 'interés negativo': lo que la otra parte gastó o "
            "perdió por haber confiado razonablemente en que el contrato se "
            "celebraría, no por las ganancias que hubiera tenido de cumplirse."
        ),
    },
    {
        "id": "q5",
        "tema": "Señal o arras",
        "pregunta": "En el CCyC actual (a diferencia del Código de Vélez), la señal o arras se presume, salvo pacto en contrario:",
        "opciones": [
            "Penitencial (permite arrepentirse)",
            "Confirmatoria (art. 1059)",
            "Nula de pleno derecho",
            "Solo válida en contratos formales",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1059 invierte la regla histórica: hoy la señal se presume "
            "confirmatoria (refuerza el vínculo) salvo que las partes pacten "
            "expresamente que es penitencial (que habilita el arrepentimiento con "
            "pérdida/devolución duplicada de la seña, art. 1060)."
        ),
    },
    {
        "id": "q6",
        "tema": "Efectos del contrato",
        "pregunta": "La regla del 'efecto relativo' de los contratos (art. 1021) significa que:",
        "opciones": [
            "El contrato produce efectos absolutos frente a todos",
            "El contrato solo tiene efecto entre las partes, salvo excepciones legales",
            "Los terceros pueden exigir su cumplimiento libremente",
            "Solo se aplica a contratos formales",
        ],
        "correcta": 1,
        "explicacion": (
            "Art. 1021: el contrato solo tiene efecto entre las partes contratantes; "
            "no lo tiene respecto de terceros, salvo excepciones legales como la "
            "estipulación a favor de tercero (art. 1027) o la extensión a "
            "sucesores universales (art. 1024)."
        ),
    },
    {
        "id": "q7",
        "tema": "Extinción del contrato",
        "pregunta": "Ante un incumplimiento esencial sin pacto comisorio expreso, para resolver el contrato la parte cumplidora debe, según el art. 1088:",
        "opciones": [
            "Resolver directamente sin ningún aviso previo",
            "Emplazar a la otra parte a cumplir en un plazo no menor a 15 días, bajo apercibimiento de resolución",
            "Iniciar juicio y esperar sentencia firme",
            "Solicitar autorización judicial previa siempre",
        ],
        "correcta": 1,
        "explicacion": (
            "Cuando el pacto comisorio es implícito, el art. 1088 exige un "
            "requerimiento previo: emplazar a la parte incumplidora a cumplir en "
            "un plazo no menor a 15 días (salvo que de los usos o la índole de la "
            "prestación resulte la procedencia de uno menor), bajo apercibimiento "
            "expreso de resolución."
        ),
    },
    {
        "id": "q8",
        "tema": "Imprevisión",
        "pregunta": "La teoría de la imprevisión (art. 1091) exige que la alteración de circunstancias sea:",
        "opciones": [
            "Ordinaria y previsible",
            "Extraordinaria, imprevisible y ajena a las partes",
            "Causada por culpa de la parte perjudicada",
            "Solo aplicable a contratos gratuitos",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1091 requiere una alteración EXTRAORDINARIA e imprevisible "
            "de las circunstancias existentes al contratar, ajena a las partes, "
            "que torne la prestación excesivamente onerosa y supere el riesgo "
            "propio del contrato (los riesgos normales del negocio no habilitan "
            "esta figura)."
        ),
    },
    {
        "id": "q9",
        "tema": "Clasificación de contratos",
        "pregunta": "Un contrato de seguro, donde la existencia y magnitud de las ventajas para las partes dependen de un acontecimiento incierto, se clasifica como:",
        "opciones": [
            "Oneroso conmutativo",
            "Oneroso aleatorio (art. 968)",
            "Gratuito",
            "Formal solemne absoluto",
        ],
        "correcta": 1,
        "explicacion": (
            "Art. 968: es aleatorio cuando las ventajas para todos los "
            "contratantes o para alguno de ellos dependen de un acontecimiento "
            "incierto. El seguro es el ejemplo típico de esta categoría."
        ),
    },
    {
        "id": "q10",
        "tema": "Contratos por adhesión",
        "pregunta": "En un contrato de adhesión a cláusulas predispuestas, una cláusula ambigua se interpreta:",
        "opciones": [
            "A favor del predisponente",
            "En contra del predisponente (contra proferentem)",
            "Se anula todo el contrato automáticamente",
            "Queda a criterio exclusivo del juez sin regla legal",
        ],
        "correcta": 1,
        "explicacion": (
            "Los arts. 987 y 1068/1069 consagran la regla 'contra proferentem': "
            "las cláusulas ambiguas predispuestas por una parte se interpretan en "
            "sentido contrario a esa parte, porque fue quien tuvo el poder de "
            "redactarlas con claridad."
        ),
    },
    {
        "id": "q11",
        "tema": "Obligaciones dinerarias",
        "pregunta": "Tras la reforma del DNU 70/2023 a los arts. 765 y 766 CCyC, si se pacto pagar en dolares, el deudor:",
        "opciones": [
            "Puede liberarse dando el equivalente en pesos al tipo de cambio que prefiera",
            "Solo se libera entregando la moneda exactamente pactada; los jueces no pueden modificarla",
        ],
        "correcta": 1,
        "explicacion": (
            "El DNU 70/2023 elimino la facultad de pagar en pesos que traia "
            "el texto original de 2015. Hoy el deudor solo se libera "
            "entregando la moneda pactada, y la norma prohibe expresamente "
            "que los jueces modifiquen la moneda o la forma de pago "
            "convenidas por las partes."
        ),
    },
    {
        "id": "q12",
        "tema": "Obligaciones de medios y de resultado",
        "pregunta": "Un cirujano estetico que promete un resultado especifico asume, segun el art. 774 CCyC, una obligacion de:",
        "opciones": [
            "Medios: solo debe poner diligencia, sin garantizar el resultado",
            "Resultado eficaz (de garantia): responde objetivamente si no logra el resultado prometido",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 774 inc. c) capta el supuesto de procurar el "
            "resultado eficaz prometido: la responsabilidad es objetiva, y "
            "el profesional solo se exime probando caso fortuito o culpa de "
            "la victima."
        ),
    },
    {
        "id": "q13",
        "tema": "Leasing",
        "pregunta": "En el leasing, la responsabilidad objetiva frente a terceros por el riesgo o vicio de la cosa (art. 1243 CCyC) recae sobre:",
        "opciones": [
            "El dador, porque conserva la propiedad registral del bien",
            "El tomador, porque tiene la guarda material e intelectual y el aprovechamiento economico del bien",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1243 excluye al dador de la responsabilidad objetiva "
            "del art. 1757, aunque sea el propietario, porque transfirio "
            "totalmente la guarda de la cosa al tomador."
        ),
    },
    {
        "id": "q14",
        "tema": "Fianza",
        "pregunta": "Si una persona se obliga como 'principal pagador' (art. 1591 CCyC), aunque se lo llame 'fiador', en realidad es:",
        "opciones": [
            "Un fiador simple con beneficio de excusion",
            "Un deudor solidario liso y llano, sin accesoriedad ni subsidiariedad",
        ],
        "correcta": 1,
        "explicacion": (
            "El 'principal pagador' pierde la accesoriedad y la "
            "subsidiariedad propias de la fianza: se rige directamente por "
            "las normas de las obligaciones solidarias pasivas."
        ),
    },
    {
        "id": "q15",
        "tema": "Transporte",
        "pregunta": "Si un colectivo sufre un reventon de neumatico y un pasajero se lesiona, el transportista:",
        "opciones": [
            "Se exime invocando caso fortuito, ya que es un hecho imprevisible",
            "No se exime: el reventon es un riesgo interno de la actividad, no caso fortuito ajeno a ella",
        ],
        "correcta": 1,
        "explicacion": (
            "Solo se exime con caso fortuito AJENO al riesgo de la "
            "actividad. Un reventon, una falla de frenos o un choque vial "
            "son riesgos internos del transporte y no eximen de "
            "responsabilidad."
        ),
    },
    {
        "id": "q16",
        "tema": "Donacion",
        "pregunta": "Con la Ley 27.587 (2020), si un heredero pretende reducir una donacion inoficiosa pero el inmueble ya fue vendido a un tercero de buena fe y a titulo oneroso, ese tercero:",
        "opciones": [
            "Puede perder el inmueble igual, porque la accion de reduccion es reipersecutoria",
            "Conserva el inmueble: el heredero solo tiene una accion personal de danos contra el donatario original",
        ],
        "correcta": 1,
        "explicacion": (
            "La Ley 27.587 protegio al tercer adquirente de buena fe y a "
            "titulo oneroso. La pretension del heredero muta de una accion "
            "real a una accion personal de danos contra el donatario "
            "original."
        ),
    },
    {
        "id": "q17",
        "tema": "Cesion de derechos",
        "pregunta": "Si un mismo credito es cedido a dos cesionarios distintos, a quien prefiere el sistema?",
        "opciones": [
            "Al cesionario que firmo el contrato de cesion primero en el tiempo",
            "Al cesionario que notifico primero al deudor cedido con instrumento de fecha cierta",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1622 CCyC premia la diligencia publicitaria: prevalece "
            "quien notifico primero al deudor cedido, no quien contrato "
            "primero."
        ),
    },
    {
        "id": "q18",
        "tema": "Vicios redhibitorios y consumo",
        "pregunta": "El CCyC no incluyo la accion estimatoria (quita proporcional del precio) entre las opciones del art. 1039. En consumo, que norma revive esa posibilidad?",
        "opciones": [
            "El art. 1091 CCyC (imprevision)",
            "El art. 17 de la Ley de Defensa del Consumidor (LDC)",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 17 LDC habilita al consumidor a pedir sustitucion, "
            "resolucion con restitucion, o una quita proporcional del "
            "precio: revive de facto la accion estimatoria."
        ),
    },
    {
        "id": "q19",
        "tema": "Arbitraje",
        "pregunta": "Si el contrato principal que contiene una clausula arbitral resulta nulo, que pasa con la competencia de los arbitros para juzgar esa nulidad?",
        "opciones": [
            "Los arbitros pierden competencia automaticamente, porque el contrato de arbitraje tambien cae",
            "Los arbitros conservan competencia: el contrato de arbitraje es autonomo del contrato principal (principio de separabilidad)",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1653 CCyC consagra la autonomia del contrato de "
            "arbitraje: la nulidad del contrato principal no acarrea la "
            "nulidad de la clausula arbitral, que sigue vigente para que "
            "los arbitros decidan incluso sobre esa nulidad."
        ),
    },
    {
        "id": "q20",
        "tema": "Arbitraje",
        "pregunta": "Puede revisarse judicialmente el fondo de lo decidido en un laudo arbitral (si los arbitros interpretaron mal el derecho)?",
        "opciones": [
            "Si, cualquier parte disconforme puede apelar el contenido del laudo ante la justicia",
            "No: el laudo solo puede impugnarse por causales taxativas de nulidad (vicios graves del procedimiento), nunca por errores de fondo",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1656 CCyC excluye la revision judicial del fondo de "
            "lo decidido por los arbitros. Solo procede la accion de "
            "nulidad por causales taxativas (por ejemplo, violacion del "
            "derecho de defensa o del orden publico), no una apelacion "
            "sobre el acierto de la decision."
        ),
    },
    {
        "id": "q21",
        "tema": "Concesión y franquicia",
        "pregunta": "Cual es el plazo minimo legal del contrato de concesion (y, por remision, de la franquicia), segun el art. 1506 CCyC?",
        "opciones": [
            "2 anos en todos los casos",
            "4 anos (o 2 si el concedente provee las instalaciones), y si se pacto menos, se tiene por convenido el minimo legal",
        ],
        "correcta": 1,
        "explicacion": (
            "El art. 1506 fija un piso de orden publico de 4 anos (2 si "
            "el concedente provee las instalaciones). Si las partes "
            "pactaron un plazo menor, o el contrato es de plazo "
            "indeterminado, igual se aplica el minimo legal."
        ),
    },
    {
        "id": "q22",
        "tema": "Agencia y concesion",
        "pregunta": "Que consecuencia tiene rescindir un contrato de agencia o concesion de plazo indeterminado sin dar el preaviso correspondiente?",
        "opciones": [
            "Ninguna, mientras se avise con algunos dias de anticipacion",
            "Quien rescinde debe indemnizar los danos, incluyendo las ganancias dejadas de percibir durante el plazo que hubiera durado un preaviso suficiente",
        ],
        "correcta": 1,
        "explicacion": (
            "El regimen de preaviso (arts. 1492-1493 CCyC) protege a la "
            "parte mas debil de la relacion de distribucion: si se omite "
            "o resulta insuficiente, la parte que rescinde debe indemnizar "
            "el dano, incluido el lucro cesante del periodo de preaviso "
            "faltante."
        ),
    },
]
