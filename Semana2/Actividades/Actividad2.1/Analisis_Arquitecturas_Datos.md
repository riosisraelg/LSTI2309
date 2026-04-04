# Actividad 2.1: Investigación de Arquitecturas de Datos 

## 📊 Matriz Comparativa Técnica

| Vector de Análisis | Data Warehouse (DW) | Data Lake | Data Mart |
| :--- | :--- | :--- | :--- |
| **Coste** | [Investigación en curso] | [Investigación en curso] | [Investigación en curso] |
| **Flexibilidad de Datos** | Permite guardar datos estructurados y semiestructurados. Por lo que es medianamente flexible, permitiendo bases de datos, archivos o bases de datos NoSQL. | Can store structured and unstructured data at any scale. It means can store SQL and NoSQL DB, JSONs, YAMLs, XML or media, either different file formats or custom semi-structured data. | Guarda información valiosa para un estudio particular. Se utilizan datos estructurados y semiestructurados. |
| **Perfil de Usuario** | Usuarios con datos semiestructurados o estructurados en medianas y grandes cantidades, como corporaciones y empresas de 25 a más empleados. | Cualquier empresa lo puede ocupar; es extremadamente útil específicamente por su alta flexibilidad para situaciones concretas. | Departamentos específicos de una empresa o procesos aparte de sus sistemas y medios tradicionales. |

---

## 🏗️ Análisis Detallado

### 1. Data Warehouse
Esta arquitectura permite la gestión de datos estructurados y semiestructurados con una flexibilidad media. Es la opción predilecta para corporaciones que manejan volúmenes considerables de información.

**Casos de uso recomendables:**
*   Making real-time decisions based on data-driven decisions.
*   Consolidating siloed data.
*   Enabling business reporting and ad hoc analysis.
*   Implementing machine learning and AI.

### 2. Data Lake
Su ventaja principal reside en la capacidad de almacenar datos de las tres categorías (estructurados, semiestructurados y no estructurados) a cualquier escala. 

**Ventajas core:**
*   Ingesta en tiempo real de datos de múltiples fuentes.
*   Catalogación, seguridad de los datos e implementación de Machine Learning.
*   Ideal para ecosistemas de IoT y arquitecturas adaptadas para *real-time data ingesting*.
*   A diferencia del Data Warehouse, es menos estricto y más flexible ante situaciones que no requieren datos puramente estructurados.

### 3. ¿Qué es un Data Mart?
Guarda información procesada para requerimientos específicos de estudio de un departamento. Almacena datos provenientes de múltiples fuentes manteniendo la calidad de los mismos. A diferencia de los Data Lakes, los Data Marts se enfocan en datos procesados para necesidades particulares de análisis.

---

## 🔗 Fuentes de Investigación

- [Google Cloud Architecture Framework: Data Warehousing](https://cloud.google.com/learn/what-is-a-data-warehouse?hl=es)
- [AWS: ¿Qué es un Data Lake?](https://aws.amazon.com/es/big-data/datalakes-and-analytics/what-is-a-data-lake/)
- [Microsoft Azure Data Architecture Guide](https://learn.microsoft.com/es-es/azure/architecture/data-guide/relational-data/data-warehousing)
- [AWS Reference: What is a Data Mart?](https://aws.amazon.com/what-is-a-data-mart/)
