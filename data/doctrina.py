"""
Perspectiva crítica de cátedra (síntesis pedagógica, en lenguaje propio,
de la línea doctrinaria asociada a Weingarten/Ghersi sobre el derecho de
los contratos). No reemplaza al CCyC: es una lente de lectura adicional,
muy útil para exámenes que piden "análisis crítico" y no solo la letra
de la ley.
"""

EJES_DOCTRINARIOS = [
    {
        "titulo": "El contrato como fenómeno económico y social",
        "resumen": (
            "El contrato no es una abstracción aislada: es la forma jurídica "
            "que toma la circulación de bienes y servicios en un sistema "
            "económico determinado. La cátedra sostiene que el modelo de "
            "'contrato paritario' (dos partes iguales que negocian cada "
            "cláusula) describía la economía artesanal previa a la "
            "industrialización, pero hoy es una porción minoritaria del "
            "tráfico real: la gran mayoría de los contratos que se celebran "
            "en la sociedad son de adhesión, de consumo, o forman parte de "
            "redes de contratos conexos."
        ),
    },
    {
        "titulo": "Consentimiento vs. asentimiento",
        "resumen": (
            "El consentimiento clásico presupone deliberación, igualdad de "
            "condiciones y posibilidad real de modificar las cláusulas. En "
            "los contratos de adhesión y de consumo, sostiene la cátedra, no "
            "hay consentimiento en ese sentido, sino un mero ASENTIMIENTO: "
            "el adherente se somete a un esquema normativo y económico ya "
            "diseñado por el predisponente, con una alternativa binaria "
            "('tomar o dejar'). Esta distinción no es solo terminológica: "
            "justifica la intervención judicial correctora (control de "
            "cláusulas abusivas) que sería impensable frente a un "
            "consentimiento plenamente negociado."
        ),
    },
    {
        "titulo": "Vulnerabilidad estructural (no una debilidad circunstancial)",
        "resumen": (
            "La asimetría entre proveedor y consumidor no es un accidente "
            "del mercado ni depende del caso concreto: es ESTRUCTURAL, y "
            "según esta doctrina, opera como una presunción que no admite "
            "prueba en contrario. Se manifiesta en cinco planos: técnico "
            "(desconocimiento del producto), económico-político (asimetría "
            "de poder de negociación), biológico (el 'consumo de "
            "supervivencia': alimentos, salud, vivienda no son electivos), "
            "ambiental y psicológico (marketing y neuromarketing que "
            "inducen necesidades). Los 'consumidores hipervulnerables' "
            "(niños, ancianos, personas con discapacidad) suman factores "
            "adicionales de fragilidad."
        ),
    },
    {
        "titulo": "Las tres funciones del orden público",
        "resumen": (
            "Coordinación (liberal clásica: solo prohíbe pactos ilícitos "
            "entre partes presuntamente iguales), Dirección (el Estado "
            "orienta la macroeconomía: tarifas, control de cambios, "
            "retenciones) y Protección (pilar del derecho del consumo: "
            "tutela imperativa e irrenunciable de la parte débil). La "
            "evolución del derecho contractual argentino, para la cátedra, "
            "es la evolución desde el primero hacia el tercero."
        ),
    },
    {
        "titulo": "Interés positivo vs. interés negativo",
        "resumen": (
            "La diferencia entre rescindir, revocar y resolver no es solo "
            "de nomenclatura: determina CUÁNTO se indemniza. Si el contrato "
            "se declara NULO (vicio de origen, como en la lesión), solo se "
            "indemniza el interés NEGATIVO o 'de confianza': se retrotrae el "
            "patrimonio de la víctima a como estaba antes de contratar "
            "(gastos y daño emergente), pero nunca las ganancias que hubiera "
            "tenido el contrato. Si el contrato se RESUELVE por "
            "incumplimiento imputable a la otra parte, se indemniza el "
            "interés POSITIVO o 'de cumplimiento': se coloca a la víctima "
            "como si el contrato se hubiera cumplido en su totalidad "
            "(incluyendo el lucro cesante esperado del negocio)."
        ),
    },
    {
        "titulo": "La crítica a la 'oferta al público' en el consumo (art. 973)",
        "resumen": (
            "El art. 973 CCyC —pensado para el contrato paritario— dice que "
            "la oferta a personas indeterminadas es solo una invitación a "
            "ofertar. La cátedra sostiene que aplicar esta regla a las "
            "relaciones de consumo invierte el sentido protectorio: en el "
            "consumo, la publicidad masiva de un producto con precisiones "
            "concretas SÍ es una oferta vinculante para el proveedor (art. 7 "
            "y 8 LDC, art. 1103 CCyC), precisamente porque la empresa "
            "invirtió en construir esa expectativa en el público."
        ),
    },
    {
        "titulo": "Contratos conexos y la crisis del efecto relativo",
        "resumen": (
            "Cuando varios contratos autónomos (compraventa + financiación + "
            "seguro, por ejemplo) están unidos por una finalidad económica "
            "supracontractual común, la doctrina y el art. 1075 CCyC admiten "
            "que los efectos, incumplimientos y nulidades de uno de ellos se "
            "propaguen a los demás. Esto rompe el dogma clásico del efecto "
            "relativo (res inter alios acta) para impedir que las empresas "
            "'atomicen' artificialmente su responsabilidad frente al "
            "consumidor mediante estructuras societarias o contractuales "
            "separadas."
        ),
    },
    {
        "titulo": "El 'deber de asesoramiento' en contratos informáticos",
        "resumen": (
            "En contratación de tecnología, la brecha no es económica sino "
            "COGNITIVA (el cliente no entiende el lenguaje técnico). Por "
            "eso, sostiene la cátedra, el genérico 'deber de información' se "
            "eleva a un DEBER DE ASESORAMIENTO: el proveedor experto debe "
            "diagnosticar la necesidad real del cliente y hasta disuadirlo "
            "de compras sobredimensionadas o ineficientes. Si lo omite, el "
            "consentimiento del cliente puede considerarse viciado por error "
            "sustancial."
        ),
    },
]

CASO_JURISPRUDENCIAL_DESTACADO = {
    "titulo": "CSJN, 'Mosca, Hugo Arnaldo c/ Provincia de Buenos Aires y otros' (2007)",
    "resumen": (
        "Un chofer de un diario fue lesionado por un objeto arrojado desde "
        "la tribuna durante un partido de fútbol, mientras esperaba en la "
        "vía pública (no había comprado entrada). La Corte extendió la "
        "obligación de seguridad —de naturaleza objetiva y de resultado— al "
        "'tercero expuesto' o bystander, condenando al club organizador "
        "(que genera el riesgo y se beneficia económicamente del evento), "
        "pero rechazó la responsabilidad de la Provincia de Buenos Aires, "
        "por entender que la actuación policial se ajustó al estándar de "
        "diligencia exigible (no hubo 'falta de servicio'). El fallo es la "
        "referencia clásica para explicar el alcance —y los límites— del "
        "concepto de consumidor expuesto."
    ),
}
