# Actividad 5 — Ciencia de Datos

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio
**Ponderación:** 6%
**Temas relacionados:** T13, T14, T15 (Regresión lineal múltiple en Python - Partes 1, 2 y 3)

---

## Descripción

Dividida en dos partes, la actividad te guiará a través del proceso de aplicación de técnicas avanzadas de ciencia de datos para resolver problemas reales, enfocándose en dos estudios de caso: predicción de ventas según el precio y el kilometraje de los vehículos y análisis de factores de sobrevivencia en el Titanic.

---

## Objetivo

Reforzar los conocimientos sobre regresión lineal múltiple y regresión logística binaria para analizar datos y generar predicciones útiles en contextos de toma de decisiones.

---

## Instrucciones

### Parte 1: Predicción de ventas usando regresión lineal múltiple

En esta sección de la actividad, crearás y evaluarás un modelo de regresión lineal múltiple para predecir las ventas de los vehículos de acuerdo con el precio de venta establecido y el kilometraje de los mismos.

1. **Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data/download?datasetVersionNumber=1

2. **Análisis exploratorio:** Realiza una gráfica de dispersión para verificar la relación que existe entre el precio, el kilometraje y las ventas. Para esto, utiliza pairplot de la biblioteca Seaborn, la cual te permitirá visualizar las relaciones entre estas variables.

3. **Identificación de variables:** Determina cuáles son las variables independientes y cuál es la dependiente.

4. **División de datos:** Crea los grupos de entrenamiento y de prueba para tus variables. Esta división es esencial para entrenar tu modelo con un conjunto de datos y evaluar su rendimiento con otro, asegurando así que el modelo sea capaz de generalizar a nuevos datos.

5. **Modelado:** Aplica el modelo de regresión lineal múltiple.

6. **Evaluación del modelo:** Puedes utilizar métricas como el R² (coeficiente de determinación) para entender qué tan bien el modelo se ajusta a los datos.

7. **Predicción:** Con el modelo ya entrenado y evaluado, procede a realizar las predicciones.

8. **Error cuadrático medio:** Este paso te ayudará a entender la magnitud de los errores cometidos por el modelo en sus predicciones.

9. **Conclusión:** Finalmente, elabora una conclusión con base en los resultados obtenidos. Reflexiona sobre la eficacia del modelo de regresión lineal múltiple para predecir las ventas de vehículos. Considera posibles mejoras o ajustes para futuros modelos.

---

### Parte 2: Análisis de sobrevivencia en el Titanic con regresión logística binaria

Esta sección de la actividad se enfoca en la creación y evaluación de un modelo de regresión logística binaria. El objetivo principal será determinar las variables más significativas para predecir la sobrevivencia de los pasajeros del Titanic.

1. **Preparación de los datos:** Guarda la base de datos en una variable. Los datos los obtendrás de la siguiente liga: https://www.openml.org/data/get_csv/16826755/phpMYEkMl.

2. **Limpieza de datos:** Examina las columnas disponibles en tu conjunto de datos y decide cuáles no son necesarias para tu análisis, elimina las que no consideres necesarias. Además, identifica los datos nulos que tengas y elimínalos.

3. **Conversión de variables a su formato correcto:** Dependiendo de las variables en tu conjunto de datos, es posible que necesites convertir algunas de ellas a un tipo de dato más apropiado, como convertir variables categóricas a tipo 'category' o ajustar las fechas a un formato de fecha y hora.

4. **Visualización de datos:** Analiza los datos de forma gráfica para verificar que existe una relación entre la variable dependiente y la independiente.

5. **Prueba t-test:** Esta puede ayudarte a entender si las diferencias en las medias de dos grupos son estadísticamente significativas.

6. **División de datos:** Divide los datos en variables de prueba y de entrenamiento. Esto es crucial para entrenar el modelo y luego evaluar su capacidad para generalizar a nuevos datos.

7. **Creación del modelo:** Utiliza las clases vistas en la explicación de los temas para que puedas crear tu modelo.

8. **Estimación de los coeficientes y los odds ratio:** Una vez que entrenaste el modelo, el siguiente paso es interpretar los resultados. Esto se hace mediante la estimación de los coeficientes, los cuales te indicarán la fuerza y dirección de la relación entre cada variable independiente y la variable dependiente.

9. **Conclusión de tus resultados:** Formula una conclusión sobre tus hallazgos. Considera cuáles variables tienen mayor impacto en la probabilidad de sobrevivencia en el Titanic y la efectividad general de tu modelo para predecir la sobrevivencia. Reflexiona sobre posibles mejoras o ajustes para el modelo.

---

## Entregable(s)

> **⚠️ IMPORTANTE: La entrega se realiza a través del repositorio de GitHub**
>
> No se aceptan documentos en Word o PDF. Todo el trabajo debe estar subido a tu repositorio de GitHub.

### Estructura de entrega en GitHub:

```
Semana6/
├── Consolidado/
│   └── Semana6_Consolidado.md    # Documento consolidado semanal
├── Actividad5/
│   ├── RegresionLineal.py        # Código de regresión múltiple
│   ├── RegresionLogistica.py      # Código de regresión logística
│   ├── Datos/                     # Datasets utilizados
│   └── Visualizaciones/           # Gráficas generadas
└── commits documentados
```

### Componentes de evaluación:

| Componente | Ponderación | Descripción |
|------------|-------------|-------------|
| **Actividad Evaluable** | **70% (4.2%)** | Modelos de regresión múltiple y diagnóstico |
| **Ejercicios Complementarios** | **10% (1.7%)** | Álgebra matricial, multicolinealidad, regularización |
| **Actividades Prácticas Extra** | **10% (1.7%)** | Actividades 6.1 - 6.4 completadas |
| **Documentación Elaborada** | **10% (1.7%)** | Consolidado semanal organizado |

---

## Rúbrica de Evaluación

### 1. Actividad Evaluable (70% - 4.2%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| **Parte 1: Regresión Múltiple** | | |
| Preparación de datos | Dataset cargado y limpio | 0-0.3% |
| Análisis exploratorio | Pairplot con Seaborn | 0-0.3% |
| Identificación de variables | Variables correctamente definidas | 0-0.2% |
| División de datos | Train/test split apropiado | 0-0.2% |
| Modelado | Regresión múltiple implementada | 0-0.3% |
| Evaluación del modelo | R² y R² ajustado calculados | 0-0.3% |
| Predicciones | Predicciones realizadas | 0-0.2% |
| **Parte 2: Diagnóstico** | | |
| Supuestos de regresión | Verificación de linealidad, homocedasticidad | 0-0.5% |
| Normalidad de residuos | Q-Q plot y pruebas | 0-0.3% |
| Multicolinealidad | VIF calculado e interpretado | 0-0.4% |
| Conclusión | Reflexión sobre resultados | 0-0.3% |

### 2. Ejercicios Complementarios (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Álgebra Matricial | Resueltos correctamente | 0-0.4% |
| Regresión Múltiple | Resueltos correctamente | 0-0.45% |
| Multicolinealidad | Resueltos correctamente | 0-0.45% |
| Regularización | Resueltos correctamente | 0-0.4% |

### 3. Actividades Prácticas Extra (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Regresión Múltiple Básica | Completado | 0-0.4% |
| Supuestos de Regresión | Completado | 0-0.45% |
| Selección de Variables | Completado | 0-0.45% |
| Regularización | Completado | 0-0.4% |

### 4. Documentación Elaborada (10% - 1.7%)

| Criterio | Descripción | Puntuación |
|----------|-------------|------------|
| Estructura | Sigue la estructura propuesta | 0-0.4% |
| Completitud | Incluye todas las secciones | 0-0.45% |
| Calidad de contenido | Ejercicios bien resueltos | 0-0.45% |
| Reflexión | Reflexiones profundas | 0-0.4% |

---

## Calendario

- **Semana:** 6
- **Fecha de entrega:** Según calendario del curso
- **Fecha límite:** Domingo de la semana indicada

---

## Recursos

- [Tema 13: Regresión lineal múltiple - parte 1](Tema13.md)
- [Tema 14: Regresión lineal múltiple - parte 2](Tema14.md)
- [Tema 15: Regresión lineal múltiple - parte 3](Tema15.md)
- [Ejercicios Complementarios Semana 6](Actividad%20Semana%206/Ejercicios%20Complementarios.md)
- [Actividades Prácticas Semana 6](Actividad%20Semana%206/Propuesta%20Actividades.md)
