# Proyecto Final - Análisis Predictivo del Mercado Inmobiliario

**Curso:** QR.LSTI2309TEO — Universidad Tecmilenio  
**Ponderación:** 35%  
**Temas:** T16, T17, T18

---

## 📋 Descripción del Proyecto

Este proyecto aplica técnicas avanzadas de ciencia de datos para desarrollar modelos predictivos basados en datos del mercado inmobiliario de Airbnb. Se utilizan técnicas de visualización avanzadas para comunicar insights de manera efectiva.

---

## 🎯 Objetivos

1. Aplicar técnicas de modelado predictivo para analizar el mercado inmobiliario
2. Comunicar los resultados de manera efectiva mediante visualizaciones
3. Desarrollar un modelo de regresión lineal múltiple para predecir precios

---

## 📁 Estructura del Proyecto

```
ProyectoFinal/
├── README.md                    # Este archivo
├── Datos/
│   └── train.csv               # Dataset de Airbnb
├── import.ipynb                # Análisis Exploratorio de Datos (Fase I)
├── Modelo.ipynb                # Modelo de Regresión Lineal Múltiple (Fase II)
├── Limpieza.py                 # Script de limpieza de datos
└── Visualizaciones/            # Gráficas generadas
```

---

## 📊 Fase I: Análisis Exploratorio (Semana 3)

### Avance del Proyecto

El análisis exploratorio inicial incluye:

- ✅ Carga y exploración del dataset (74,111 registros, 29 columnas)
- ✅ Análisis descriptivo de variables numéricas y categóricas
- ✅ Identificación de valores faltantes
- ✅ Detección de outliers (2.07% del dataset)
- ✅ Análisis de correlaciones (Pearson, Spearman, Kendall)
- ✅ Visualizaciones: histogramas, boxplots, scatter plots, mapas de calor

### Hallazgos Clave

**Variables más correlacionadas con el precio:**
1. `accommodates` (capacidad): 0.57
2. `bedrooms` (habitaciones): 0.47
3. `beds` (camas): 0.44
4. `bathrooms` (baños): 0.36

**Calidad de datos:**
- Variables con valores nulos: `host_response_rate` (24.69%), `review_scores_rating` (22.56%)
- Distribución de precios: asimetría 0.51, curtosis 0.66 (cercana a normal)

---

## 🔬 Fase II: Modelo Predictivo (Semana 7)

### Parte 1: Modelo de Regresión Lineal Múltiple

**Pasos implementados:**

1. **Limpieza de datos**
   - Eliminación/imputación de valores faltantes
   - Identificación y corrección de outliers

2. **Identificación de variables**
   - Variable dependiente: `log_price`
   - Variables independientes: `accommodates`, `bedrooms`, `beds`, `bathrooms`, etc.

3. **Selección de características**
   - Análisis de correlación
   - Evaluación de multicolinealidad (VIF)

4. **División de datos**
   - Train/test split (80/20)

5. **Construcción del modelo**
   - Regresión lineal múltiple con sklearn

6. **Evaluación**
   - R² y R² ajustado
   - MSE (Error Cuadrático Medio)
   - Análisis de residuos

7. **Predicciones**
   - Predicciones sobre conjunto de prueba
   - Comparación con valores reales

### Parte 2: Comunicación de Resultados

**Visualizaciones creadas:**
- Gráficos de predicciones vs valores reales
- Gráficos de importancia de características
- Análisis de residuos
- Distribución de errores

**Narrativa:**
- Explicación de resultados del análisis
- Interpretación de la precisión del modelo
- Análisis de cómo las características influyen en los precios

---

## 📈 Resultados del Modelo

### Métricas de Evaluación

| Métrica | Valor |
|---------|-------|
| R² | [Por completar] |
| R² Ajustado | [Por completar] |
| MSE | [Por completar] |
| RMSE | [Por completar] |

### Coeficientes del Modelo

| Variable | Coeficiente | Interpretación |
|----------|-------------|----------------|
| accommodates | [valor] | [interpretación] |
| bedrooms | [valor] | [interpretación] |
| beds | [valor] | [interpretación] |
| bathrooms | [valor] | [interpretación] |

---

## 🛠️ Tecnologías Utilizadas

- **Python 3.x**
- **Pandas**: Manipulación de datos
- **NumPy**: Operaciones numéricas
- **Matplotlib**: Visualizaciones
- **Seaborn**: Visualizaciones estadísticas
- **Scikit-learn**: Modelado predictivo
- **Scipy**: Análisis estadístico

---

## 📝 Instrucciones de Uso

### 1. Configurar el entorno

```bash
# Crear entorno virtual
python -m venv .venv

# Activar entorno
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate     # Windows

# Instalar dependencias
pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter
```

### 2. Ejecutar el análisis

```bash
# Abrir Jupyter
jupyter notebook

# Abrir los notebooks en orden:
# 1. import.ipynb (Análisis Exploratorio)
# 2. Modelo.ipynb (Modelo Predictivo)
```

---

## 📚 Referencias

- Dataset: [Airbnb Price Prediction - Kaggle](https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction)
- Scikit-learn Documentation: https://scikit-learn.org/
- Seaborn Gallery: https://seaborn.pydata.org/examples/index.html

---

## 👤 Autor

**Nombre:** [Tu nombre]  
**Matrícula:** [Tu matrícula]  
**Curso:** QR.LSTI2309TEO  
**Universidad:** Tecmilenio

---

## 📅 Historial de Versiones

| Versión | Fecha | Descripción |
|---------|-------|-------------|
| 1.0 | Semana 3 | Análisis Exploratorio de Datos |
| 2.0 | Semana 7 | Modelo Predictivo y Entrega Final |

---

## ✅ Checklist de Entrega

- [x] Limpieza de datos
- [x] Identificación de variables
- [x] Selección de características
- [x] Análisis de correlación
- [x] División train/test
- [ ] Construcción del modelo
- [ ] Evaluación del modelo (R², MSE)
- [ ] Manejo de multicolinealidad
- [ ] Predicciones sobre test set
- [ ] Visualizaciones de resultados
- [ ] Narrativa y comunicación
- [ ] Consolidado semanal
- [ ] Commits documentados en Git

---

## 📧 Contacto

Para dudas o comentarios sobre este proyecto, contactar a través de la plataforma del curso.
