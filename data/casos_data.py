"""
Casos prácticos guiados. Cada caso tiene una secuencia de pasos con una
pregunta de análisis y luego una explicación (feedback) que enseña el
razonamiento jurídico esperado, citando los artículos relevantes.
"""

CASOS = [
    {
        "id": "caso1",
        "titulo": "El comprador arrepentido",
        "nivel": "Básico",
        "enunciado": (
            "Marta ve en la vidriera de un local un cartel: 'Bicicletas "
            "usadas, todos los modelos, $80.000'. Entra, elige una "
            "bicicleta puntual y le dice al vendedor 'me la llevo'. El "
            "vendedor se la envuelve y ella entrega $20.000 como seña, "
            "acordando pagar el resto en 3 días al retirarla. Al día "
            "siguiente, Marta se arrepiente y quiere que le devuelvan la "
            "seña completa."
        ),
        "pasos": [
            {
                "pregunta": "¿El cartel de la vidriera fue una 'oferta' en sentido técnico o una invitación a ofertar?",
                "opciones": [
                    "Fue una oferta vinculante, porque tenía precio",
                    "Fue una invitación a ofertar (art. 973), porque se dirige a personas indeterminadas",
                ],
                "correcta": 1,
                "explicacion": (
                    "Correcto: el cartel, al dirigirse al público en general, es en "
                    "principio invitación a ofertar (art. 973). La oferta concreta "
                    "la hizo Marta cuando eligió la bicicleta y dijo 'me la llevo', "
                    "y el contrato se perfeccionó cuando el vendedor la aceptó "
                    "(entre presentes, art. 980 inc. a)."
                ),
            },
            {
                "pregunta": "¿Ya existe un contrato de compraventa perfeccionado entre Marta y el vendedor?",
                "opciones": [
                    "No, falta que se pague el precio completo",
                    "Sí: hubo oferta de Marta y aceptación del vendedor entre presentes (art. 980 inc. a)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Sí. El contrato ya se perfeccionó con el acuerdo sobre la cosa y "
                    "el precio (elementos esenciales de la compraventa). El pago total "
                    "pendiente y la entrega diferida son solo modalidades de "
                    "cumplimiento, no condicionan la existencia del contrato."
                ),
            },
            {
                "pregunta": "Como no se pactó nada sobre el carácter de la seña, ¿es confirmatoria o penitencial?",
                "opciones": [
                    "Penitencial, porque las señas son siempre penitenciales",
                    "Confirmatoria (art. 1059): es la regla general si las partes no dijeron lo contrario",
                ],
                "correcta": 1,
                "explicacion": (
                    "Es confirmatoria (art. 1059). El CCyC invirtió la regla del "
                    "Código de Vélez: hoy, salvo pacto expreso en contrario, la seña "
                    "REFUERZA el contrato en lugar de habilitar el arrepentimiento."
                ),
            },
            {
                "pregunta": "¿Puede Marta arrepentirse y exigir la devolución simple de los $20.000?",
                "opciones": [
                    "Sí, siempre puede arrepentirse dentro de las 48 horas",
                    "No: al ser la seña confirmatoria, el contrato la obliga (art. 959) y si no cumple, incurre en incumplimiento contractual",
                ],
                "correcta": 1,
                "explicacion": (
                    "No puede simplemente 'arrepentirse'. Como la seña es "
                    "confirmatoria y el contrato es obligatorio (art. 959, fuerza "
                    "vinculante), si Marta no paga el saldo y retira la bicicleta, "
                    "está incumpliendo el contrato: el vendedor podría exigirle el "
                    "cumplimiento o resolver el contrato y reclamar los daños que el "
                    "incumplimiento le cause (más allá de la seña entregada)."
                ),
            },
        ],
        "conclusion": (
            "Este caso combina tres institutos centrales del Título II: la "
            "distinción entre oferta e invitación a ofertar (art. 973), el "
            "momento de perfeccionamiento del consentimiento entre presentes "
            "(art. 980), y el nuevo régimen de la seña confirmatoria (art. "
            "1059), que cambió sustancialmente respecto del Código derogado."
        ),
    },
    {
        "id": "caso2",
        "titulo": "La cláusula abusiva en el gimnasio",
        "nivel": "Intermedio",
        "enunciado": (
            "Juan se inscribe en un gimnasio firmando un contrato de "
            "adhesión ya impreso, con letra chica, que entre sus 40 "
            "cláusulas incluye una que dice: 'El gimnasio no asume "
            "ninguna responsabilidad por lesiones sufridas por el socio "
            "dentro del establecimiento, cualquiera sea la causa'. Juan "
            "sufre una lesión por una máquina en mal estado, y el "
            "gimnasio invoca esa cláusula para no responder."
        ),
        "pasos": [
            {
                "pregunta": "¿Qué tipo de contrato es este, según su forma de celebración?",
                "opciones": [
                    "Un contrato paritario, negociado punto por punto",
                    "Un contrato por adhesión a cláusulas predispuestas (arts. 984-989), y también de consumo",
                ],
                "correcta": 1,
                "explicacion": (
                    "Es un contrato por adhesión: el gimnasio redactó unilateralmente "
                    "todas las cláusulas y Juan solo pudo aceptarlas o no contratar. "
                    "Además, al ser Juan un consumidor final del servicio, se aplican "
                    "también las reglas de contratos de consumo (Título III)."
                ),
            },
            {
                "pregunta": "¿La cláusula que exime totalmente de responsabilidad al gimnasio 'cualquiera sea la causa' es válida?",
                "opciones": [
                    "Sí, porque Juan la firmó y aceptó libremente",
                    "No: es una cláusula abusiva porque desnaturaliza las obligaciones del predisponente (arts. 988 y 1117-1119)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Es abusiva. El art. 988 inc. a) considera abusivas, en los "
                    "contratos por adhesión, las cláusulas que desnaturalizan las "
                    "obligaciones del predisponente. Eximirse de TODA "
                    "responsabilidad, incluso por su propia negligencia (máquina en "
                    "mal estado), vacía de contenido su deber de seguridad. En "
                    "materia de consumo, el art. 1117 remite a este mismo régimen."
                ),
            },
            {
                "pregunta": "¿Qué consecuencia tiene declarar abusiva esa cláusula?",
                "opciones": [
                    "Se anula todo el contrato de inscripción al gimnasio",
                    "Se tiene por no escrita esa cláusula, pero el resto del contrato subsiste (art. 989)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Art. 989: la aprobación administrativa de las cláusulas "
                    "generales, o su inclusión en el contrato, no obsta a su "
                    "control judicial; cuando el juez declara la nulidad parcial "
                    "del contrato, simultáneamente lo debe integrar, si no puede "
                    "subsistir sin comprometer su finalidad. La sanción es la "
                    "nulidad de la cláusula, no de todo el contrato: el gimnasio "
                    "sigue obligado por el resto, y responde por la lesión conforme "
                    "a las reglas generales de responsabilidad civil."
                ),
            },
        ],
        "conclusion": (
            "Este caso muestra cómo el control de cláusulas abusivas (arts. "
            "988-989, y su espejo en el Título III de consumo, arts. "
            "1117-1119) protege a la parte débil en contratos predispuestos, "
            "y cómo la nulidad parcial preserva el contrato en lugar de "
            "destruirlo por completo."
        ),
    },
    {
        "id": "caso3",
        "titulo": "El contrato de exportación que se volvió inviable",
        "nivel": "Avanzado",
        "enunciado": (
            "Una empresa argentina firma en enero un contrato de "
            "suministro a 2 años con un importador extranjero, fijando el "
            "precio en pesos argentinos. Seis meses después, una crisis "
            "macroeconómica excepcional dispara una devaluación del 300% "
            "y una inflación descontrolada no prevista por ningún analista "
            "al momento de contratar, lo que hace que seguir vendiendo al "
            "precio pactado le genere pérdidas ruinosas a la empresa "
            "argentina."
        ),
        "pasos": [
            {
                "pregunta": "¿Qué instituto del Título II podría aplicar la empresa argentina para no seguir perdiendo con cada entrega?",
                "opciones": [
                    "La resolución por incumplimiento (art. 1084), porque el importador incumplió",
                    "La imprevisión o excesiva onerosidad sobreviniente (art. 1091)",
                ],
                "correcta": 1,
                "explicacion": (
                    "El art. 1091 es la figura correcta: el importador no incumplió "
                    "nada, pero un hecho extraordinario y ajeno a las partes "
                    "(crisis macroeconómica excepcional) volvió la prestación de la "
                    "empresa argentina excesivamente onerosa. No hay incumplimiento "
                    "de nadie, sino un desequilibrio sobrevenido."
                ),
            },
            {
                "pregunta": "¿Alcanza con probar que el contrato se volvió 'menos conveniente' para invocar el art. 1091?",
                "opciones": [
                    "Sí, cualquier pérdida de rentabilidad habilita la imprevisión",
                    "No: se exige una alteración EXTRAORDINARIA e imprevisible que exceda el riesgo propio del negocio",
                ],
                "correcta": 1,
                "explicacion": (
                    "No alcanza. El estándar es exigente: debe tratarse de un cambio "
                    "extraordinario e imprevisible al momento de contratar (no una "
                    "fluctuación normal del mercado o del tipo de cambio, que es un "
                    "riesgo propio de todo contrato en moneda local a largo plazo), y "
                    "debe superar el riesgo que razonablemente asumió esa parte."
                ),
            },
            {
                "pregunta": "Si se dan los requisitos, ¿qué puede pedir la empresa argentina: solo la resolución total?",
                "opciones": [
                    "Solo puede pedir la resolución total del contrato",
                    "Puede pedir la resolución total o parcial, o plantear un reajuste equitativo (adecuación) del contrato",
                ],
                "correcta": 1,
                "explicacion": (
                    "El art. 1091 da dos caminos: resolver (total o parcialmente) o "
                    "pedir la adecuación/renegociación equitativa del contrato, "
                    "manteniendo el vínculo pero reequilibrando las prestaciones. "
                    "En la práctica, muchas veces conviene negociar la adecuación "
                    "para no perder una relación comercial de largo plazo."
                ),
            },
        ],
        "conclusion": (
            "La imprevisión (art. 1091) es una herramienta pensada para "
            "contratos de ejecución diferida o continuada frente a sucesos "
            "verdaderamente extraordinarios, no para cualquier variación "
            "normal del mercado. Distinguirla de la frustración de la "
            "finalidad (art. 1090) y del incumplimiento (arts. 1084-1088) es "
            "clave en un examen de contratos."
        ),
    },
    {
        "id": "caso4",
        "titulo": "El leasing del tractor y el accidente",
        "nivel": "Intermedio",
        "enunciado": (
            "Una empresa agropecuaria toma un tractor en leasing operativo "
            "(el dador ya era dueno del bien antes de contratar). Mientras "
            "el tomador lo usa en el campo, el tractor atropella y lesiona "
            "a un peon rural por una falla de frenos. El peon demanda al "
            "dador (dueno registral) y al tomador (quien usaba el tractor)."
        ),
        "pasos": [
            {
                "pregunta": "Segun el art. 1243 CCyC, quien responde objetivamente frente al peon lesionado por el riesgo de la cosa?",
                "opciones": [
                    "El dador, por ser el propietario registral del tractor",
                    "El tomador, porque tiene la guarda material e intelectual y el aprovechamiento economico del bien",
                ],
                "correcta": 1,
                "explicacion": (
                    "El art. 1243 CCyC excluye al dador de la "
                    "responsabilidad objetiva del art. 1757: aunque "
                    "conserve la propiedad, transfirio la guarda completa "
                    "al tomador, que es quien debe responder frente al "
                    "peon lesionado."
                ),
            },
            {
                "pregunta": "Si en cambio la modalidad hubiera sido que el dador compro el tractor a pedido y segun especificaciones del tomador (art. 1231 inc. b), quien responderia por un vicio de fabrica del tractor frente al TOMADOR (no frente al peon)?",
                "opciones": [
                    "El dador, que debe responder plenamente por saneamiento",
                    "El proveedor/fabricante original: el tomador se subroga en las acciones de saneamiento y el dador queda liberado (art. 1232)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Cuando el dador actua como mero intermediario "
                    "financiero (comprando segun las especificaciones o "
                    "indicaciones del tomador), el art. 1232 lo libera de "
                    "responder por vicios o falta de idoneidad del bien: "
                    "esas acciones se dirigen contra el proveedor original, "
                    "en las que el tomador se subroga."
                ),
            },
        ],
        "conclusion": (
            "El leasing combina dos planos de responsabilidad distintos: "
            "frente a TERCEROS por el riesgo de la cosa en uso (art. 1243, "
            "siempre el tomador), y frente al TOMADOR por vicios del bien "
            "(art. 1231/1232, depende de la modalidad de adquisicion). No "
            "confundir ambos planos es clave para resolver bien un caso de "
            "leasing."
        ),
    },
    {
        "id": "caso5",
        "titulo": "El fiador del alquiler y la prorroga sorpresa",
        "nivel": "Intermedio",
        "enunciado": (
            "Julian firma como fiador simple de un contrato de locacion de "
            "un ano a favor de su amigo Tomas, inquilino. Al vencer el ano, "
            "el locador y Tomas acuerdan prorrogar el contrato por dos anos "
            "mas, sin avisarle nada a Julian. A los seis meses de la "
            "prorroga, Tomas deja de pagar el alquiler y el locador quiere "
            "cobrarle la deuda a Julian como fiador."
        ),
        "pasos": [
            {
                "pregunta": "Como fiador SIMPLE (no solidario), que beneficio procesal tiene Julian antes de que le exijan pagar?",
                "opciones": [
                    "Ninguno: el fiador simple responde igual que uno solidario",
                    "El beneficio de excusion (art. 1583): puede exigir que primero se ejecuten los bienes del deudor principal",
                ],
                "correcta": 1,
                "explicacion": (
                    "El fiador simple goza del beneficio de excusion: el "
                    "acreedor debe dirigirse primero contra los bienes del "
                    "deudor principal (Tomas) antes de poder cobrarle a "
                    "Julian."
                ),
            },
            {
                "pregunta": "La prorroga del contrato de locacion sin el consentimiento de Julian, afecta su fianza para ese periodo prorrogado?",
                "opciones": [
                    "No, la fianza sigue vigente automaticamente durante toda prorroga",
                    "Si: el art. 1596 inc. b) CCyC extingue la fianza si se prorroga el plazo de la obligacion garantizada sin el consentimiento del fiador",
                ],
                "correcta": 1,
                "explicacion": (
                    "El art. 1596 inc. b) es claro: la fianza se extingue "
                    "si se prorroga el plazo de cumplimiento sin el "
                    "consentimiento del fiador. Julian solo garantizo el "
                    "primer ano; la deuda generada durante la prorroga no "
                    "pactada con el no lo alcanza."
                ),
            },
            {
                "pregunta": "Entonces, puede el locador cobrarle a Julian la deuda generada en el septimo mes (dentro de la prorroga)?",
                "opciones": [
                    "Si, porque la fianza es accesoria y sigue a la deuda principal siempre",
                    "No, porque esa deuda nacio durante un periodo no cubierto por la fianza extinguida (art. 1596 inc. b)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Al extinguirse la fianza para el periodo prorrogado, "
                    "Julian no responde por deudas generadas durante esa "
                    "prorroga que el nunca consintio. El locador debera "
                    "reclamarle exclusivamente a Tomas."
                ),
            },
        ],
        "conclusion": (
            "Este caso ilustra una de las causales especiales de extincion "
            "de la fianza (art. 1596) que suele pasarse por alto: el "
            "fiador no queda ligado indefinidamente a cualquier "
            "modificacion posterior del contrato principal que no consintio "
            "expresamente."
        ),
    },
    {
        "id": "caso6",
        "titulo": "El phishing bancario y la responsabilidad concurrente",
        "nivel": "Avanzado",
        "enunciado": (
            "A Elena la llama alguien que dice ser del banco y le pide "
            "instalar una aplicacion de asistencia remota para 'verificar "
            "una operacion sospechosa'. Elena la instala, y los "
            "estafadores acceden a su home banking, registran diez nuevos "
            "destinatarios y hacen ocho transferencias en menos de una "
            "hora, vaciando su cuenta. El banco no genero alertas hasta "
            "varias horas despues. Elena reclama al banco la restitucion "
            "integra del dinero."
        ),
        "pasos": [
            {
                "pregunta": "El banco, al ofrecer servicios de banca digital, asume una obligacion de seguridad informatica. Que tipo de obligacion es?",
                "opciones": [
                    "Una obligacion de medios: alcanza con que tenga 'algun' sistema de seguridad",
                    "Un estandar reforzado que exige detectar patrones de uso anomalos y alertar preventivamente",
                ],
                "correcta": 1,
                "explicacion": (
                    "El deber de seguridad informatica del banco lo obliga "
                    "a disenar barreras de control aptas para contrarrestar "
                    "fraudes, incluyendo la deteccion de patrones "
                    "transaccionales inusuales (diez destinatarios nuevos y "
                    "ocho transferencias en una hora es, precisamente, un "
                    "patron atipico que deberia disparar alertas "
                    "tempranas)."
                ),
            },
            {
                "pregunta": "El hecho de que Elena haya instalado voluntariamente el software de acceso remoto a pedido de un desconocido, la deja sin ningun reclamo posible?",
                "opciones": [
                    "Si, su propia negligencia grave libera totalmente al banco",
                    "No necesariamente: la jurisprudencia reciente aplica un criterio de responsabilidad CONCURRENTE, distribuyendo el dano entre banco y clienta",
                ],
                "correcta": 1,
                "explicacion": (
                    "Los tribunales comerciales, ante fallas del sistema de "
                    "seguridad del banco combinadas con un descuido grave "
                    "del cliente, no eximen totalmente al banco (que sigue "
                    "teniendo un deber de seguridad objetivo) ni cargan "
                    "todo el dano sobre la clienta: aplican la doctrina de "
                    "la causalidad concurrente, morigerando la "
                    "indemnizacion en lugar de negarla o concederla en su "
                    "totalidad."
                ),
            },
            {
                "pregunta": "Si se prueba que el banco envio la alerta de las transferencias varias horas despues de consumado el vaciamiento, que efecto tiene eso en el reparto de responsabilidad?",
                "opciones": [
                    "Ninguno, porque la clienta ya habia cometido el error inicial",
                    "Agrava la responsabilidad del banco, porque incumplio su propio estandar de deteccion temprana de patrones anomalos",
                ],
                "correcta": 1,
                "explicacion": (
                    "La demora en alertar sobre un patron transaccional "
                    "flagrantemente inusual es, en si misma, una falla "
                    "atribuible al banco, que agrava su cuota de "
                    "responsabilidad dentro del esquema de causalidad "
                    "concurrente, aunque no elimine la incidencia causal de "
                    "la conducta descuidada de la clienta."
                ),
            },
        ],
        "conclusion": (
            "El deber de seguridad bancaria en entornos digitales se "
            "mantiene como un nucleo duro de responsabilidad objetiva, pero "
            "la jurisprudencia comercial reciente no otorga una cobertura "
            "ciega: pondera tambien la conducta del cliente, buscando un "
            "equilibrio entre exigir barreras tecnologicas robustas al "
            "banco y un minimo resguardo razonable de las propias "
            "credenciales por parte del usuario."
        ),
    },
    {
        "id": "caso7",
        "titulo": "La concesionaria rescindida sin aviso",
        "nivel": "Avanzado",
        "enunciado": (
            "Una automotriz (concedente) le otorga a Ruedas SA una "
            "concesion de plazo indeterminado hace 8 anos. Sin previo "
            "aviso, la automotriz le comunica de un dia para otro que da "
            "por terminada la relacion, alegando que puede rescindir "
            "'cuando quiera' por ser un contrato de plazo indeterminado. "
            "Ruedas SA, que invirtio fuerte en instalaciones y personal "
            "capacitado, reclama una indemnizacion."
        ),
        "pasos": [
            {
                "pregunta": "Es correcto que la automotriz pueda rescindir 'cuando quiera' sin ningun recaudo, por tratarse de un contrato de plazo indeterminado?",
                "opciones": [
                    "Si, el plazo indeterminado permite la rescision unilateral incausada e inmediata",
                    "No: debe otorgar un preaviso razonable antes de rescindir (arts. 1492-1493 CCyC)",
                ],
                "correcta": 1,
                "explicacion": (
                    "Aunque el contrato sea de plazo indeterminado, la "
                    "parte que quiere rescindirlo debe dar un preaviso "
                    "razonable, calculado como pauta en un mes por cada "
                    "ano de vigencia del contrato. Rescindir sin preaviso "
                    "es rescindir de forma intempestiva."
                ),
            },
            {
                "pregunta": "Que puede reclamar Ruedas SA por la falta de preaviso?",
                "opciones": [
                    "Nada, porque el contrato de plazo indeterminado no genera derecho a indemnizacion",
                    "Los danos causados por la omision del preaviso, incluyendo las ganancias dejadas de percibir durante el plazo que hubiera durado un preaviso suficiente",
                ],
                "correcta": 1,
                "explicacion": (
                    "El regimen protectorio de la distribucion comercial "
                    "(aplicable a agencia y concesion) impone indemnizar "
                    "el dano derivado de la falta de preaviso, incluyendo "
                    "el lucro cesante correspondiente al periodo de "
                    "preaviso omitido."
                ),
            },
            {
                "pregunta": "El hecho de que Ruedas SA haya invertido fuertemente en instalaciones y personal, tiene alguna relevancia juridica adicional?",
                "opciones": [
                    "No, esos gastos son un riesgo propio del negocio que Ruedas SA debe asumir sin mas",
                    "Si: la falta de amortizacion de inversiones especificas por la ruptura intempestiva integra el calculo del dano resarcible",
                ],
                "correcta": 1,
                "explicacion": (
                    "La doctrina y la jurisprudencia consolidada en esta "
                    "materia (receptada por el regimen de preaviso del "
                    "CCyC) reconocen que la falta de amortizacion de "
                    "inversiones especificas exigidas por el concedente "
                    "(instalaciones, capacitacion, stock) es un rubro "
                    "resarcible cuando la ruptura es intempestiva."
                ),
            },
        ],
        "conclusion": (
            "Este caso muestra como el regimen de preaviso de los arts. "
            "1492-1493 CCyC opera como una proteccion analoga a la de los "
            "contratos por adhesion: aunque formalmente las partes sean "
            "'independientes', la asimetria economica entre una gran "
            "concedente y un concesionario que invirtio en la red "
            "justifica limitar la libertad de rescision unilateral "
            "incausada."
        ),
    },
]
