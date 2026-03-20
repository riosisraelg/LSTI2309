# Actividad 1 — Ciencia de Datos

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Ponderación:** 6%

---

## Descripción

La actividad consiste en la elaboración de un **reporte** basado en el análisis de un caso práctico, en el cual se aplicarán los conceptos de ciencia de datos, Big Data, arquitecturas de almacenamiento de datos y bases de datos NoSQL.

---

## Objetivo

Aplicar los conocimientos y habilidades adquiridas para resolver problemas reales con un enfoque práctico y eficiente.

---

## Instrucciones

### Caso: DeportivaMX

DeportivaMX, una tienda en línea de artículos deportivos en México, se encuentra en una situación de crecimiento acelerado en sus registros de ventas en línea. Actualmente, la empresa no cuenta con el personal ni la infraestructura adecuada para gestionar este crecimiento, lo que está generando desafíos en la gestión de sus datos.

Ante este escenario, DeportivaMX recurre a ti como científico de datos para desarrollar una solución que optimice el almacenamiento y futuro tratamiento de datos. El objetivo principal es optimizar la experiencia de sus clientes a corto y mediano plazo.

Algunas actividades que se han planteado y que te ayudarán a generar el reporte son las siguientes:

La empresa contratará un equipo de profesionales altamente capacitados, que posean competencias específicas en ciencia de datos. Estos especialistas serán responsables de interpretar y emplear los datos de manera efectiva, contribuyendo así a la toma de decisiones basada en información precisa.
Se recolectarán datos de diversas fuentes, incluyendo registros de ventas, información relacionada con los clientes y características específicas de los productos. Posteriormente, estos datos se limpiarán y organizarán para facilitar su análisis y asegurar calidad y relevancia.
Se usarán herramientas de visualización para explorar los datos y obtener insights sobre el comportamiento de los clientes, las tendencias del mercado y el performance de la tienda.
Se analizarán los datos para identificar áreas de mejora en la gestión de datos, como la eficiencia del almacenamiento y la precisión de la información.
Finalmente, se tiene como objetivo implementar arquitecturas de datos escalables y seguras, capaces de almacenar y procesar grandes volúmenes de datos de manera eficiente.

### 1. Perfiles de ciencia de datos

Para atender el caso de la tienda que desea tomar decisiones basadas en datos, se recomienda conformar un equipo balanceado con los siguientes perfiles, mapeando claramente qué aporta cada uno a las actividades descritas.

**Data Scientist**  
En este contexto, los Data Scientists se encargan de transformar los datos recopilados (ventas, clientes, productos) en conocimiento accionable. A partir de los datos ya limpios y organizados, realizan análisis exploratorios, prueban hipótesis sobre el comportamiento de los clientes, construyen modelos de segmentación, predicción de demanda o recomendación de productos, y colaboran con el equipo de negocio para traducir estos modelos en decisiones concretas (promociones, cambios en el catálogo, optimización de precios). Su rol es clave para que los datos no se queden solo en reportes descriptivos, sino que generen ventajas competitivas mediante modelos de inteligencia artificial y machine learning.

**Data Engineer**  
Los Data Engineers son responsables de la infraestructura que permite recolectar, mover y transformar los datos desde las distintas fuentes: sistemas de ventas, CRM de clientes, catálogos de productos, etc. En el caso de la tienda, diseñan y construyen el data pipeline que puede incluir ingestión batch (cargas diarias de ventas históricas) y, si se requiere, ingestión en streaming (transacciones casi en tiempo real). También se encargan de integrar datos heterogéneos en un data lake o data warehouse, garantizando calidad, consistencia y disponibilidad para que Data Scientists y Data Analysts puedan trabajar sin preocuparse por la parte técnica de integración.

**Machine Learning (ML) Engineer / AI & ML Specialist**  
Una vez que los Data Scientists han definido y validado modelos útiles (por ejemplo, un modelo que predice probabilidad de compra o abandono), los ML Engineers se encargan de llevar esos modelos a producción. En el caso de la tienda, diseñan la arquitectura para que los modelos se integren con el sistema de ventas, el sitio web o el CRM, de modo que las recomendaciones o predicciones se puedan usar en tiempo real o de forma automatizada. También monitorizan el desempeño de los modelos, gestionan versiones, ajustan recursos de cómputo y se aseguran de que las soluciones de IA/ML sean escalables, seguras y eficientes en costos.

**Data Analyst**  
El Data Analyst se enfoca en explotar los datos para responder preguntas específicas del negocio mediante consultas (SQL u otras herramientas), dashboards y reportes. Para esta empresa, se encargaría de crear reportes sobre ventas por producto, tienda o canal, análisis de comportamiento de clientes (frecuencia de compra, ticket promedio, categorías más consumidas), así como indicadores de desempeño clave (KPIs) de la tienda. Además, colabora en el uso de herramientas de visualización para explorar los datos y obtener insights rápidos sobre tendencias del mercado y rendimiento de campañas, apoyando la identificación de áreas de mejora en la gestión de datos y en la operación diaria.

**Business Analyst**  
El Business Analyst actúa como puente entre el negocio y el equipo técnico. En el escenario planteado, se encarga de recopilar las necesidades de los directivos y áreas comerciales (por ejemplo, entender por qué ciertas líneas de producto no se venden, o cómo mejorar la retención de clientes), traducir esas necesidades en requerimientos de datos y analítica, y priorizar las iniciativas. Trabaja con Data Analysts y Data Scientists para definir qué indicadores y modelos son más relevantes, y con ML Engineers y Data Engineers para asegurar que las soluciones desarrolladas realmente se integren en los procesos de la tienda. De esta manera, garantiza que las decisiones estén alineadas con la estrategia y se basen en información precisa.

**ETL Developer / Data Developer**  
Este perfil se especializa en la creación y mantenimiento de los procesos ETL/ELT que extraen datos de las fuentes operacionales, los transforman (limpieza, normalización, enriquecimiento) y los cargan en repositorios centrales. En el caso de la tienda, el ETL Developer diseña los flujos que toman los registros de ventas, la información de clientes y las características de productos, los validan, corrigen inconsistencias y los organizan en modelos de datos adecuados para análisis (por ejemplo, modelos estrella/dimensionales en un data warehouse). Su trabajo es crítico para asegurar que “los datos se limpiarán y organizarán para facilitar su análisis y asegurar calidad y relevancia”.

**Big Data Architect / IT Architect**  
Finalmente, el Big Data Architect diseña la arquitectura global de datos que soportará todos los casos de uso presentes y futuros. Para esta empresa, define qué tecnologías utilizar (por ejemplo, servicios en la nube para almacenamiento masivo, procesamiento distribuido y seguridad), cómo se integran los componentes (data lake, data warehouse, herramientas de visualización, plataformas de ML) y qué patrones de arquitectura se emplean para garantizar que el sistema sea escalable, seguro y eficiente. También define las políticas de gobernanza y buenas prácticas para que la organización pueda almacenar y procesar grandes volúmenes de datos de forma confiable, alineándose con el objetivo de implementar arquitecturas de datos escalables y seguras.

En conjunto, estos siete perfiles cubren todo el ciclo de vida de los datos para la tienda: desde la recolección y organización de la información, pasando por la creación de modelos avanzados y visualizaciones, hasta la definición de arquitecturas robustas y la traducción de resultados en decisiones de negocio concretas.

### 2. Las 5 V del Big Data

Manejar datos, desarrollar la arquitectura y ejecutar workloads y pipelines para la toma informada de decisiones requiere orden y claridad. Las cinco V nos permiten **mapear y entender** mejor las características de nuestros datos y cómo impactan el diseño de la solución para la tienda.

Aunque en la documentación de AWS solo se mencionan explícitamente **Volume, Velocity y Variety**, los conceptos de **Veracity** y **Value** también están presentes, pero con otros nombres (data quality, data governance, actionable insights, business value). A continuación se justifica cada V aplicada al caso planteado.

- **2.2 Velocity (Velocidad)**olumen de datos crece constantemente a partir de:

- Registros de ventas históricos (día a día, mes a mes, año tras año).  
- Información de clientes (datos de contacto, historial de compras, preferencias).  
- Catálogo y características de productos (categorías, precios, inventario, descripciones).

Aunque la empresa quizás no esté aún en “petabytes”, la arquitectura debe estar preparada para escalar conforme aumentan las transacciones y se integran nuevas fuentes (por ejemplo, ventas en línea, campañas digitales, redes sociales). Esto justifica la necesidad de **arquitecturas de datos escalables** (data lakes, data warehouses en la nube) y de un diseño que soporte el crecimiento sin perder rendimiento.

- **2.3 Variety (Variedad)**on **qué tan rápido se generan y necesitan los datos**:

- Las ventas se producen en tiempo casi real; cada ticket de compra genera un nuevo registro.  
- Las métricas de desempeño (ventas por día, producto más vendido, stock crítico) se deben actualizar con la frecuencia suficiente para tomar decisiones oportunas (reposición, promociones, ajustes de precios).  
- En un escenario más avanzado, podrían analizarse flujos de datos en streaming (por ejemplo, eventos en un e‑commerce o interacciones de clientes en tiempo real).

Esto implica diseñar procesos de ingestión **batch** (cargas periódicas de datos históricos) y, si el negocio lo requiere, **streaming** (actualizaciones casi inmediatas) para que los dashboards y modelos reflejen la realidad con la rapidez necesaria.

- **2.4 Veracity (Veracidad: Calidad, Integridad y Confiabilidad)**os que maneja la tienda:

- Datos estructurados: registros de ventas en el sistema de punto de venta (POS), tablas de clientes y productos en bases de datos relacionales.  
- Datos semiestructurados: archivos CSV/JSON exportados del CRM, de la plataforma de e‑commerce o de pasarelas de pago.  
- Datos no estructurados (potenciales): reseñas de clientes, correos de soporte, mensajes en redes sociales, imágenes de productos, etc.

Esta variedad obliga a diseñar una arquitectura que pueda integrar datos con diferentes esquemas y niveles de estructura (por ejemplo, usando un data lake en la nube), y a definir procesos de transformación que los unifiquen en modelos analíticos coherentes.

- **2.5 Value (Valor: Resultados de Negocio e Insights Accionables)**de AWS, pero sí a través de conceptos como **data quality** y **data governance**. En el caso de la tienda, la veracidad es crítica porque:

- Los datos de ventas pueden contener errores (tickets duplicados, devoluciones mal registradas, productos asignados a categorías incorrectas).  
- La información de clientes puede tener registros incompletos o duplicados (mismo cliente con varios IDs).  
- Diferentes sistemas pueden manejar formatos o reglas distintas (por ejemplo, monedas, impuestos, zonas horarias).

Durante la fase de **Transform** en los procesos ETL/ELT se aplican tareas de limpieza y estandarización: eliminación de duplicados, corrección de tipos de datos, normalización de catálogos, validación de reglas de negocio, etc. Además, las políticas de gobierno de datos (quién puede modificar qué, controles de acceso, trazabilidad) ayudan a garantizar que la información sea **íntegra y confiable**, de modo que las decisiones se basen en datos que realmente reflejan la realidad del negocio.

Finalmente, el valor responde a la pregunta: **¿para qué estamos recopilando y procesando todos estos datos?**. En la documentación de AWS este concepto aparece como *actionable insights* y *business value*. En la tienda, el valor se materializa cuando:

- Los análisis permiten identificar patrones de compra para diseñar promociones más efectivas.  
- Los modelos predictivos ayudan a anticipar la demanda y optimizar inventarios, reduciendo quiebres de stock y sobreinventario.  
- Los dashboards muestran KPIs clave (ventas, margen, rotación, fidelidad de clientes), permitiendo decisiones más rápidas y fundamentadas.  
- Se descubren nuevas oportunidades de negocio (nuevas líneas de producto, segmentación por tipo de cliente, canales con mayor potencial).

En otras palabras, los datos dejan de ser solo un “registro histórico” y se convierten en una herramienta para **mejorar la operación, incrementar ingresos, reducir costos y tomar decisiones estratégicas** antes que la competencia.

En conjunto, las cinco V —Volumen, Velocidad, Variedad, Veracidad y Valor— permiten justificar por qué la empresa necesita una arquitectura moderna de datos, procesos de calidad y un equipo especializado para transformar los datos de ventas, clientes y productos en ventajas reales para la tienda.

3. **Arquitectura de almacenamiento** — Realiza un análisis y define qué tipo de arquitectura/arquitecturas de almacenamiento de datos es óptima o adecuada para la empresa. Deberás justificar el porqué de la selección, además de plantar y sustentar qué tipo de base de datos NoSQL es la más factible de usar en la empresa.



4. **Diseño de colecciones en JSON** — Genera el análisis y plasma las estructuras de las posibles colecciones en formato JSON que deberá tener la base de datos NoSQL para el almacenamiento de datos no estructurados en **MongoDB** a través de su interfaz gráfica.

```json
{
  "cliente_id": "C123",
  "nombre": "Juan Pérez",
  "correo": "juan@example.com",
  "telefono": "555-123-4567",
  "direccion": {
    "calle": "Av. Principal 123",
    "ciudad": "Ciudad de México",
    "estado": "CDMX",
    "cp": "01234"
  },
  "fecha_registro": "2024-01-15T10:30:00Z",
  "preferencias": ["fútbol", "correr"],
  "metodos_pago": [
    {
      "tipo": "tarjeta",
      "ultimos4": "1234"
    }
  ]
}
```

```json
{
  "producto_id": "P567",
  "nombre": "Tenis para correr",
  "categoria": "Calzado",
  "marca": "MarcaX",
  "precio": 1299.99,
  "stock": 50,
  "tallas_disponibles": [24, 25, 26, 27],
  "colores": ["negro", "azul"],
  "caracteristicas": {
    "material": "malla",
    "genero": "unisex"
  }
}
```

```json
{
  "venta_id": "V890",
  "fecha": "2024-03-19T15:20:00Z",
  "cliente_id": "C123",
  "items": [
    {
      "producto_id": "P567",
      "cantidad": 2,
      "precio_unitario": 1299.99
    }
  ],
  "total": 2599.98,
  "metodo_pago": "tarjeta",
  "estatus": "completada",
  "canal": "web"
}
```

```json
{
   resena"review_id": "R001",
   "cliente_id": "C123",
   "nombre": "Juan Pérez",
   "calificacion": 4.5,
   "comentarios": "",
   "media": [
      "mediaObject_id" : "mediaObject/attachtments"
   ],
   "timestamp": "02302026-113050"
}

---

## Entregable(s)

> **⚠️ IMPORTANTE: La entrega se realiza a través del repositorio de GitHub**
>
> No se aceptan documentos en Word o PDF. Todo el trabajo debe estar subido a tu repositorio de GitHub.

### Estructura de entrega en GitHub:

```
Semana1/
├── Consolidado/
│   └── Semana1_Consolidado.md    # Documento consolidado semanal
├── Actividad1/
│   ├── Reporte.md                 # Reporte de la actividad
│   └── colecciones.json           # Colecciones JSON para MongoDB
└── commits documentados
```

### Componentes de evaluación:

| Componente | Ponderación | Descripción |
|------------|-------------|-------------|
| **Actividad Evaluable** | **70% (4.2%)** | Reporte completo con los 4 puntos solicitados |
| **Ejercicios Complementarios** | **10% (0.6%)** | Ejercicios de la semana 1 completados |
| **Actividades Prácticas Extra** | **10% (0.6%)** | Actividades 1.0 - 1.4 completadas |
| **Documentación Elaborada** | **10% (0.6%)** | Consolidado semanal organizado |

---

## Rúbrica de Evaluación

### 1. Actividad Evaluable (70% - 4.2%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| **Perfiles de ciencia de datos** | Menciona al menos 3 perfiles con argumentación clara del porqué | 0-1.05% |
| **Las 5 V del Big Data** | Explica las 5 V con ejemplos relacionados al caso | 0-1.05% |
| **Arquitectura de almacenamiento** | Justifica la selección de arquitectura y tipo de base de datos NoSQL | 0-1.05% |
| **Colecciones en JSON** | Crea al menos 3 colecciones con estructura válida en JSON | 0-1.05% |

### 2. Ejercicios Complementarios (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Ejercicios de Álgebra | Resueltos correctamente | 0-0.2% |
| Ejercicios de Lógica Computacional | Resueltos correctamente | 0-0.2% |
| Ejercicios de Escalas Big Data | Resueltos correctamente | 0-0.2% |

### 3. Actividades Prácticas Extra (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Configuración de Git y Repositorio | Completado | 0-0.15% |
| Conceptos Fundamentales | Completado | 0-0.15% |
| Casos de Uso | Completado | 0-0.15% |
| Entorno de Trabajo | Completado | 0-0.15% |

### 4. Documentación Elaborada (10% - 0.6%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Estructura | Sigue la estructura propuesta | 0-0.15% |
| Completitud | Incluye todas las secciones | 0-0.15% |
| Calidad de contenido | Ejercicios bien resueltos | 0-0.15% |
| Reflexión | Reflexiones profundas | 0-0.15% |

---

## Calendario

- **Semana:** 1
- **Fecha de entrega:** Según calendario del curso
- **Fecha límite:** Domingo de la semana indicada
