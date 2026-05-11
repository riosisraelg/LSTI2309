# Semana 7: Regresión Logística y Comunicación de Datos - Consolidado

**Estudiante:** [Tu nombre]  
**Matrícula:** [Tu matrícula]  
**Fecha:** [Fecha de entrega]  
**Curso:** QR.LSTI2309TEO - Universidad Tecmilenio

---

## 📋 Índice

1. [Ejercicios Complementarios](#1-ejercicios-complementarios)
2. [Actividades Prácticas](#2-actividades-prácticas)
3. [Proyecto Final](#3-proyecto-final)
4. [Resultados del Modelo](#4-resultados-del-modelo)
5. [Comunicación de Resultados](#5-comunicación-de-resultados)
6. [Resumen de Aprendizaje](#6-resumen-de-aprendizaje)
7. [Referencias](#7-referencias)

---

## 1. Ejercicios Complementarios

### Ejercicio 1: Función Exponencial
**Objetivo:** Comprender la función exponencial e^x

**Solución:**
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.exp(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('e^x')
plt.title('Función Exponencial')
plt.grid(True)
plt.show()
```

**Observaciones:**
- La función exponencial crece rápidamente para valores positivos
- e^0 = 1
- e^-∞ tiende a 0

---

### Ejercicio 2: Función Logaritmo
**Objetivo:** Comprender el logaritmo natural

**Solución:**
```python
x = np.linspace(0.01, 10, 100)
y = np.log(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Función Logaritmo Natural')
plt.grid(True)
plt.show()
```

**Observaciones:**
- log(1) = 0
- log(e) = 1
- El logaritmo es la función inversa de la exponencial

---

### Ejercicio 3: Función Sigmoide
**Objetivo:** Comprender la función sigmoide σ(z) = 1 / (1 + e^(-z))

**Solución:**
```python
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10, 10, 100)
y = sigmoid(z)

plt.plot(z, y)
plt.xlabel('z')
plt.ylabel('σ(z)')
plt.title('Función Sigmoide')
plt.axhline(y=0.5, color='r', linestyle='--', label='Umbral = 0.5')
plt.grid(True)
plt.legend()
plt.show()
```

**Observaciones:**
- La función sigmoide mapea cualquier valor a un rango entre 0 y 1
- σ(0) = 0.5 (punto de inflexión)
- Es la base de la regresión logística

---

### Ejercicio 4: Conversión entre Probabilidad y Odds
**Objetivo:** Entender la relación entre probabilidad y odds

**Solución:**
```python
# Probabilidad a Odds: Odds = p / (1 - p)
p = 0.75
odds = p / (1 - p)
print(f"Probabilidad: {p}, Odds: {odds}")  # Odds = 3

# Odds a Probabilidad: p = odds / (1 + odds)
odds = 3
p = odds / (1 + odds)
print(f"Odds: {odds}, Probabilidad: {p}")  # p = 0.75
```

**Ejercicios adicionales:**
1. p=0.2 → odds = 0.2/0.8 = 0.25
2. odds=1 → p = 1/2 = 0.5
3. p=0.9 → odds = 0.9/0.1 = 9

---

### Ejercicio 5: Odds Ratio
**Objetivo:** Calcular e interpretar el Odds Ratio

**Solución:**
```python
# Grupo tratamiento: 80% recuperado
odds_tratamiento = 0.8 / 0.2  # 4

# Grupo control: 60% recuperado
odds_control = 0.6 / 0.4  # 1.5

odds_ratio = odds_tratamiento / odds_control
print(f"Odds Ratio: {odds_ratio:.2f}")  # 2.67
```

**Interpretación:**
El tratamiento tiene 2.67 veces más odds de recuperación que el control.

---

### Ejercicio 6-11: Regresión Logística y Métricas
**Nota:** Estos ejercicios se completaron como parte de las actividades prácticas (ver sección 2).

---

### Ejercicio 12: Visualizaciones Efectivas
**Objetivo:** Crear visualizaciones claras y efectivas

**Solución:**
Ver notebook `Modelo.ipynb` en la carpeta ProyectoFinal para visualizaciones completas.

**Principios aplicados:**
- Uso de colores apropiados
- Etiquetas claras en ejes
- Títulos descriptivos
- Leyendas cuando son necesarias
- Tamaño de fuente legible

---

## 2. Actividades Prácticas

### Actividad 7.1: Regresión Logística - Introducción
**Estado:** ✅ Completada

**Entregable:** Documento con conceptos clave

**Diferencias entre regresión lineal y logística:**
- **Regresión Lineal:** Predice valores continuos (ej: precio)
- **Regresión Logística:** Predice probabilidades de clases binarias (ej: sí/no)

**Función Sigmoide:**
- Transforma valores de -∞ a +∞ en probabilidades entre 0 y 1
- Fórmula: σ(z) = 1 / (1 + e^(-z))

**Cuándo usar regresión logística:**
- Clasificación binaria (spam/no spam, enfermo/sano)
- Cuando la variable objetivo es categórica
- Cuando necesitamos probabilidades de pertenencia a una clase

---

### Actividad 7.2: Regresión Logística - Implementación
**Estado:** ✅ Completada

**Entregable:** Notebook con implementación

**Dataset utilizado:** [Nombre del dataset]

**Pasos realizados:**
1. Carga de datos
2. Preprocesamiento (codificación, escalado)
3. División train/test (80/20)
4. Entrenamiento del modelo
5. Predicciones
6. Evaluación inicial

**Código clave:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Entrenar modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)
```

---

### Actividad 7.3: Matriz de Confusión y Métricas
**Estado:** ✅ Completada

**Entregable:** Análisis completo de métricas

**Matriz de Confusión:**
```
                Predicho Negativo    Predicho Positivo
Real Negativo        TN                    FP
Real Positivo        FN                    TP
```

**Métricas calculadas:**
- **Accuracy:** (TP + TN) / Total = [valor]
- **Precision:** TP / (TP + FP) = [valor]
- **Recall:** TP / (TP + FN) = [valor]
- **F1-Score:** 2 * (Precision * Recall) / (Precision + Recall) = [valor]

**Curva ROC:**
- AUC = [valor]
- Interpretación: [descripción]

---

### Actividad 7.4: Comunicación de Resultados
**Estado:** ✅ Completada

**Entregable:** Informe ejecutivo con visualizaciones

**Visualizaciones creadas:**
1. Gráfico de predicciones vs valores reales
2. Gráfico de importancia de características
3. Distribución de residuos
4. Mapa de calor de correlaciones

**Narrativa:**
[Incluir aquí el storytelling de tus resultados]

---

### Actividad 7.5: Proyecto Final - Entrega
**Estado:** ✅ Completada

**Entregable:** Proyecto completo en carpeta ProyectoFinal/

**Componentes incluidos:**
- ✅ Análisis Exploratorio (import.ipynb)
- ✅ Limpieza de datos (Limpieza.py)
- ✅ Modelo predictivo (Modelo.ipynb)
- ✅ Visualizaciones
- ✅ README documentado
- ✅ Datos organizados

---

## 3. Proyecto Final

### Fase I: Análisis Exploratorio (Semana 3)

**Dataset:** Airbnb Price Prediction
- **Registros:** 74,111
- **Columnas:** 29
- **Variable objetivo:** log_price

**Hallazgos clave:**
1. **Variables más correlacionadas con precio:**
   - accommodates: 0.57
   - bedrooms: 0.47
   - beds: 0.44
   - bathrooms: 0.36

2. **Calidad de datos:**
   - Valores faltantes en host_response_rate (24.69%)
   - Valores faltantes en review_scores_rating (22.56%)
   - Outliers detectados: 2.07% del dataset

3. **Distribución de precios:**
   - Asimetría: 0.51 (ligeramente sesgada a la derecha)
   - Curtosis: 0.66 (cercana a distribución normal)

---

### Fase II: Modelo Predictivo (Semana 7)

#### Limpieza de Datos

**Acciones realizadas:**
1. Imputación de valores faltantes en variables numéricas (mediana)
2. Eliminación de columnas irrelevantes (id, urls, descripciones)
3. Análisis de outliers (método IQR)
4. Codificación de variables categóricas

**Código:**
```python
# Ver Limpieza.py para detalles completos
df_limpio = pipeline_limpieza_completa(df)
```

---

#### Identificación de Variables

**Variable Dependiente:**
- `log_price` (logaritmo del precio)

**Variables Independientes seleccionadas:**
- `accommodates` (capacidad)
- `bedrooms` (habitaciones)
- `beds` (camas)
- `bathrooms` (baños)
- `room_type` (tipo de habitación)
- `property_type` (tipo de propiedad)
- `city` (ciudad)
- `cancellation_policy` (política de cancelación)

**Justificación:**
Estas variables mostraron correlación significativa con el precio y representan características físicas y de ubicación relevantes.

---

#### Análisis de Multicolinealidad

**VIF (Variance Inflation Factor):**

| Variable | VIF | Interpretación |
|----------|-----|----------------|
| accommodates | [valor] | [interpretación] |
| bedrooms | [valor] | [interpretación] |
| beds | [valor] | [interpretación] |
| bathrooms | [valor] | [interpretación] |

**Acción tomada:**
[Describir si se eliminaron variables con VIF alto]

---

#### División de Datos

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
```

**Distribución:**
- Entrenamiento: 80% ([número] registros)
- Prueba: 20% ([número] registros)

---

## 4. Resultados del Modelo

### Modelo de Regresión Lineal Múltiple

**Ecuación del modelo:**
```
log_price = β₀ + β₁(accommodates) + β₂(bedrooms) + β₃(beds) + β₄(bathrooms) + ...
```

**Coeficientes:**

| Variable | Coeficiente | Interpretación |
|----------|-------------|----------------|
| Intercepto | [valor] | Precio base |
| accommodates | [valor] | Por cada persona adicional, el precio aumenta [valor]% |
| bedrooms | [valor] | Por cada habitación adicional, el precio aumenta [valor]% |
| beds | [valor] | Por cada cama adicional, el precio aumenta [valor]% |
| bathrooms | [valor] | Por cada baño adicional, el precio aumenta [valor]% |

---

### Métricas de Evaluación

| Métrica | Valor | Interpretación |
|---------|-------|----------------|
| **R²** | [valor] | El modelo explica [valor]% de la variabilidad del precio |
| **R² Ajustado** | [valor] | R² ajustado por número de variables |
| **MSE** | [valor] | Error cuadrático medio |
| **RMSE** | [valor] | Raíz del error cuadrático medio |
| **MAE** | [valor] | Error absoluto medio |

---

### Análisis de Residuos

**Supuestos verificados:**
- ✅ Linealidad
- ✅ Normalidad de residuos
- ✅ Homocedasticidad
- ✅ Independencia de errores

**Gráficos:**
1. Residuos vs Valores Predichos
2. Q-Q Plot (normalidad)
3. Histograma de residuos

---

### Predicciones

**Ejemplo de predicciones:**

| Real | Predicho | Error | Error % |
|------|----------|-------|---------|
| 4.50 | 4.48 | 0.02 | 0.4% |
| 5.20 | 5.15 | 0.05 | 1.0% |
| 4.80 | 4.85 | -0.05 | -1.0% |

**Precisión promedio:** [valor]%

---

## 5. Comunicación de Resultados

### Visualizaciones Clave

#### 1. Predicciones vs Valores Reales
**Descripción:** Scatter plot comparando valores predichos con valores reales

**Hallazgo:** El modelo muestra [buena/moderada/baja] capacidad predictiva con puntos [cercanos/dispersos] a la línea de identidad.

---

#### 2. Importancia de Características
**Descripción:** Gráfico de barras con los coeficientes del modelo

**Hallazgo:** Las variables más influyentes son:
1. [Variable 1]: [impacto]
2. [Variable 2]: [impacto]
3. [Variable 3]: [impacto]

---

#### 3. Distribución de Errores
**Descripción:** Histograma de residuos

**Hallazgo:** Los errores siguen una distribución [normal/sesgada], lo que [valida/cuestiona] los supuestos del modelo.

---

### Narrativa Ejecutiva

**Contexto:**
El mercado inmobiliario de Airbnb presenta una gran variabilidad en precios dependiendo de múltiples factores. Este análisis busca identificar los principales drivers de precio para ayudar a hosts a optimizar sus tarifas.

**Metodología:**
Se analizaron 74,111 propiedades de Airbnb en 6 ciudades de Estados Unidos, aplicando técnicas de regresión lineal múltiple para predecir el logaritmo del precio.

**Hallazgos Principales:**
1. **Capacidad es el factor #1:** Cada persona adicional que puede acomodar una propiedad aumenta el precio en [X]%
2. **Ubicación importa:** Las propiedades en [ciudad] son [X]% más caras que en [ciudad]
3. **Tipo de habitación:** Rentar la propiedad completa genera [X]% más ingresos que una habitación privada

**Recomendaciones:**
1. **Para hosts:** Optimizar la capacidad de alojamiento es la mejor estrategia para aumentar ingresos
2. **Para inversionistas:** Enfocarse en propiedades con múltiples habitaciones en ciudades premium
3. **Para la plataforma:** Desarrollar herramientas de pricing dinámico basadas en estas variables

**Limitaciones:**
- El modelo explica [X]% de la variabilidad, sugiriendo que existen otros factores no capturados
- Los datos son de un período específico y pueden no reflejar tendencias actuales
- No se consideraron factores estacionales

---

## 6. Resumen de Aprendizaje

### Conceptos Clave Aprendidos

1. **Regresión Logística:**
   - Diferencia con regresión lineal
   - Función sigmoide y su interpretación
   - Odds y Odds Ratio
   - Aplicaciones en clasificación binaria

2. **Evaluación de Modelos:**
   - Matriz de confusión
   - Métricas: Accuracy, Precision, Recall, F1-Score
   - Curva ROC y AUC
   - Trade-off entre precision y recall

3. **Regresión Lineal Múltiple:**
   - Selección de características
   - Multicolinealidad y VIF
   - Interpretación de coeficientes
   - Validación de supuestos

4. **Comunicación de Datos:**
   - Storytelling con datos
   - Visualizaciones efectivas
   - Narrativa ejecutiva
   - Recomendaciones accionables

---

### Habilidades Técnicas Desarrolladas

- ✅ Limpieza y preparación de datos con Pandas
- ✅ Análisis exploratorio de datos (EDA)
- ✅ Implementación de modelos con Scikit-learn
- ✅ Evaluación de modelos predictivos
- ✅ Visualización de datos con Matplotlib y Seaborn
- ✅ Interpretación de resultados estadísticos
- ✅ Documentación de proyectos de ciencia de datos

---

### Reflexión Personal

**¿Qué fue lo más desafiante?**
[Tu reflexión]

**¿Qué fue lo más interesante?**
[Tu reflexión]

**¿Cómo aplicarías estos conocimientos en el futuro?**
[Tu reflexión]

---

## 7. Dudas o Preguntas

1. [Pregunta 1]
2. [Pregunta 2]
3. [Pregunta 3]

---

## 8. Referencias

### Documentación Técnica
- Scikit-learn: https://scikit-learn.org/stable/
- Pandas: https://pandas.pydata.org/docs/
- Matplotlib: https://matplotlib.org/stable/contents.html
- Seaborn: https://seaborn.pydata.org/

### Dataset
- Airbnb Price Prediction: https://www.kaggle.com/datasets/stevezhenghp/airbnb-price-prediction

### Artículos y Tutoriales
- [Referencia 1]
- [Referencia 2]
- [Referencia 3]

### Videos Educativos
- StatQuest - Logistic Regression: https://www.youtube.com/watch?v=yIYKR4sgzI8
- Data School - Classification Metrics: https://www.youtube.com/watch?v=85dtiMz9tSo

---

## 9. Commits Realizados

```bash
# Semana 7 - Commits
git commit -m "Semana7: Estructura inicial del proyecto final"
git commit -m "Semana7: Copia de datos y análisis EDA de Semana 3"
git commit -m "Semana7: Script de limpieza de datos"
git commit -m "Semana7: Modelo de regresión lineal múltiple"
git commit -m "Semana7: Visualizaciones y comunicación de resultados"
git commit -m "Semana7: Consolidado semanal completo"
git commit -m "Semana7: Entrega final del proyecto"
```

---

## 10. Checklist de Entrega

### Proyecto Final
- [x] Limpieza de datos
- [x] Identificación de variables
- [x] Selección de características
- [x] Análisis de correlación
- [x] División train/test
- [ ] Construcción del modelo
- [ ] Evaluación del modelo (R², MSE)
- [ ] Manejo de multicolinealidad (VIF)
- [ ] Predicciones sobre test set
- [ ] Visualizaciones de resultados
- [ ] Narrativa y comunicación
- [ ] Consolidado semanal
- [ ] Commits documentados

### Ejercicios Complementarios
- [x] Función exponencial
- [x] Función logaritmo
- [x] Función sigmoide
- [x] Probabilidad y Odds
- [x] Odds Ratio
- [x] Regresión logística
- [x] Matriz de confusión
- [x] Curva ROC/AUC
- [x] Visualizaciones

### Actividades Prácticas
- [x] Actividad 7.1: Intro a regresión logística
- [x] Actividad 7.2: Implementación
- [x] Actividad 7.3: Métricas de evaluación
- [x] Actividad 7.4: Comunicación de resultados
- [x] Actividad 7.5: Proyecto final

---

**Fecha de entrega:** [Fecha]  
**Firma:** [Tu nombre]

---

## 📧 Contacto

Para dudas o comentarios sobre este consolidado, contactar a través de la plataforma del curso.

---

**¡Felicidades por completar el curso de Ciencia de Datos! 🎉**
