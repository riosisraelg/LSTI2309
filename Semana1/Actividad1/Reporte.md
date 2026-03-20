# Actividad 1 — Reporte: Caso DeportivaMX

| Campo | Detalle |
|-------|---------|
| Alumno | Israel Ríos G. |
| Curso | QR.LSTI2309TEO — Universidad Tecmilenio |
| Ponderación | 6% |

---

## 1. Perfiles de Ciencia de Datos

Para atender el caso de DeportivaMX se recomienda un equipo con los siguientes perfiles:

- **Data Scientist**: análisis exploratorio, modelos de segmentación, predicción de demanda y recomendación de productos. Transforma datos en conocimiento accionable.
- **Data Engineer**: diseña y construye pipelines de datos (batch y streaming). Integra datos heterogéneos en data lake o data warehouse.
- **ML Engineer**: lleva modelos a producción, integra con el sistema de ventas y sitio web, monitoriza desempeño.
- **Data Analyst**: reportes, dashboards, KPIs, consultas SQL. Insights rápidos sobre tendencias y rendimiento.
- **Business Analyst**: puente entre negocio y equipo técnico. Traduce necesidades en requerimientos de datos.
- **ETL Developer**: procesos ETL/ELT de limpieza, normalización y carga de datos en repositorios centrales.
- **Big Data Architect**: diseña la arquitectura global, define tecnologías, patrones de integración y políticas de gobernanza.

## 2. Las 5 V del Big Data aplicadas a DeportivaMX

- **Volumen**: registros de ventas, clientes y productos que crecen constantemente. Requiere arquitectura escalable.
- **Velocidad**: ventas en tiempo casi real, métricas que deben actualizarse oportunamente. Ingestión batch y streaming.
- **Variedad**: datos estructurados (POS, tablas SQL), semiestructurados (CSV/JSON) y no estructurados (reseñas, imágenes).
- **Veracidad**: posibles errores, duplicados e inconsistencias entre sistemas. Requiere procesos ETL de limpieza y gobernanza.
- **Valor**: insights accionables para promociones, predicción de demanda, optimización de inventarios y decisiones estratégicas.

## 3. Arquitectura de Almacenamiento

Se recomienda una arquitectura Data Lakehouse que combina Data Lake (almacenamiento flexible) con Data Warehouse (consultas estructuradas, ACID). MongoDB como base de datos NoSQL documental por su modelo de documentos JSON, esquemas flexibles, consultas ricas y escalabilidad horizontal mediante sharding.

## 4. Diseño de Colecciones en JSON

Ver archivo adjunto: `colecciones.json`

Colecciones diseñadas: clientes, productos, ventas, resenas.
