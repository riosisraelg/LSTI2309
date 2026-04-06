# Ejercicios Complementarios - Semana 7

## Temas Cubiertos
- **T16**: Regresión logística binaria - parte 1
- **T17**: Regresión logística binaria - parte 2
- **T18**: Estrategias de comunicación de datos en Python

## Prerrequisitos Recomendados
- **Matemáticas**: Funciones exponenciales, logaritmos, función sigmoide, probabilidades
- **Estadística**: Odds, Odds Ratio, probabilidad condicional, matriz de confusión, precisión, recall, F1-Score, AUC-ROC
- **Programación**: Funciones sigmoidales, métricas de clasificación, curvas ROC

---

## Ejercicios de Funciones Matemáticas

### Ejercicio 1: Función Exponencial
```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.exp(x)  # e^x

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('e^x')
plt.title('Función Exponencial')
plt.grid(True)
plt.show()

# Propiedades:
# e^0 = 1
# e^1 ≈ 2.718
# e^-∞ = 0
```

### Ejercicio 2: Función Logaritmo
```python
x = np.linspace(0.01, 10, 100)  # No puede ser 0
y = np.log(x)  # Logaritmo natural

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('log(x)')
plt.title('Función Logaritmo Natural')
plt.grid(True)
plt.show()

# Propiedades:
# log(1) = 0
# log(e) = 1
# log(a*b) = log(a) + log(b)
# log(a/b) = log(a) - log(b)
```

### Ejercicio 3: Función Sigmoide
La función sigmoide es:

```
σ(z) = 1 / (1 + e^(-z))
```

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

# Propiedades:
# σ(-∞) = 0
# σ(0) = 0.5
# σ(∞) = 1
# Es S-shaped (sigmoide)
```

---

## Ejercicios de Probabilidad y Odds

### Ejercicio 4: Conversión entre Probabilidad y Odds
```python
# Probabilidad a Odds
# Odds = p / (1 - p)

p = 0.75  # 75% de probabilidad de ganar
odds = p / (1 - p)
print(f"Probabilidad: {p}, Odds: {odds}")
# Significa: 3 a 1 (3 wins per 1 loss)

# Odds a Probabilidad
# p = odds / (1 + odds)

odds = 3  # 3 a 1
p = odds / (1 + odds)
print(f"Odds: {odds}, Probabilidad: {p}")

# Ejercicios:
# 1. Convertir p=0.2 a odds
# 2. Convertir odds=1 a probabilidad
# 3. Convertir p=0.9 a odds
```

### Ejercicio 5: Odds Ratio
```python
# Odds Ratio = Odds_grupo1 / Odds_grupo2

# Ejemplo:
# Grupo 1 (tratamiento): 80% recuperado (p=0.8)
# Grupo 2 (control): 60% recuperado (p=0.6)

odds_tratamiento = 0.8 / 0.2  # 4
odds_control = 0.6 / 0.4      # 1.5

odds_ratio = odds_tratamiento / odds_control
print(f"Odds Ratio: {odds_ratio:.2f}")
# Significa: El tratamiento tiene 2.67x más odds de recuperación
```

---

## Ejercicios de Regresión Logística

### Ejercicio 6: Regresión Logística con sklearn
```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Dataset de ejemplo: Predecir si un cliente comprará
data = {
    'edad': [25, 30, 35, 40, 45, 50, 22, 28, 33, 38],
    'ingreso': [30000, 40000, 50000, 60000, 70000, 80000, 25000, 35000, 45000, 55000],
    'compro': [0, 0, 1, 1, 1, 1, 0, 0, 0, 1]  # 0=No, 1=Sí
}

df = pd.DataFrame(data)

X = df[['edad', 'ingreso']]
y = df['compro']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear y entrenar modelo
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Accuracy
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")
```

### Ejercicio 7: Predicción de Probabilidades
```python
# Obtener probabilidades
probs = modelo.predict_proba(X_test)
print("Probabilidades (clase 0, clase 1):")
print(probs)

# Predicción manual
# Si probabilidad clase 1 > 0.5 → predecir 1
for i, prob in enumerate(probs):
    pred = 1 if prob[1] > 0.5 else 0
    print(f"Observación {i+1}: P(clase=1)={prob[1]:.3f}, Predicción={pred}")
```

---

## Ejercicios de Matriz de Confusión

### Ejercicio 8: Crear e Interpretar Matriz de Confusión
```python
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Valores reales vs predichos
y_real = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 1, 0, 0, 1, 1, 0, 1, 0]

# Matriz de confusión
cm = confusion_matrix(y_real, y_pred)
print("Matriz de Confusión:")
print(cm)

# Verdaderos Positivos (TP), Verdaderos Negativos (TN)
# Falsos Positivos (FP), Falsos Negativos (FN)
tn, fp, fn, tp = cm.ravel()
print(f"\nTN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")

# Visualizar
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['No', 'Sí'])
disp.plot()
```

### Ejercicio 9: Métricas de Clasificación
```python
from sklearn.metrics import precision_score, recall_score, f1_score, accuracy_score

# Calcular métricas
accuracy = accuracy_score(y_real, y_pred)
precision = precision_score(y_real, y_pred)
recall = recall_score(y_real, y_pred)
f1 = f1_score(y_real, y_pred)

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")

# Fórmulas:
# Accuracy = (TP + TN) / Total
# Precision = TP / (TP + FP)
# Recall = TP / (TP + FN)
# F1 = 2 * (Precision * Recall) / (Precision + Recall)
```

---

## Ejercicios de Curva ROC y AUC

### Ejercicio 10: Curva ROC
```python
from sklearn.metrics import roc_curve, roc_auc_score
import matplotlib.pyplot as plt

# Probabilidades predichas
y_real = [0, 0, 0, 0, 1, 1, 1, 1]
y_probs = [0.1, 0.3, 0.4, 0.6, 0.55, 0.7, 0.8, 0.9]

# Calcular ROC
fpr, tpr, thresholds = roc_curve(y_real, y_probs)
auc = roc_auc_score(y_real, y_probs)

# Graficar
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, label=f'ROC curve (AUC = {auc:.2f})')
plt.plot([0, 1], [0, 1], 'k--', label='Random classifier')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC')
plt.legend()
plt.grid(True)
plt.show()

print(f"AUC: {auc:.2f}")
```

### Ejercicio 11: Elegir Umbral
```python
# Relación entre umbral, precision y recall
from sklearn.metrics import precision_recall_curve

precision, recall, thresholds = precision_recall_curve(y_real, y_probs)

plt.figure(figsize=(10, 5))
plt.plot(thresholds, precision[:-1], label='Precision')
plt.plot(thresholds, recall[:-1], label='Recall')
plt.xlabel('Umbral')
plt.ylabel('Score')
plt.title('Precision vs Recall para diferentes umbrales')
plt.legend()
plt.grid(True)
plt.show()

# Trade-off: 
# - Alto umbral → Alta precisión, bajo recall
# - Bajo umbral → Baja precisión, alto recall
```

---

## Ejercicios de Visualización de Datos

### Ejercicio 12: Visualizaciones Efectivas
```python
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Crear dataset
df = pd.DataFrame({
    'categoria': ['A', 'B', 'C', 'D', 'E'],
    'ventas': [100, 200, 150, 300, 250],
    'profit': [20, 50, 30, 80, 60]
})

# 1. Gráfico de barras
plt.figure(figsize=(10, 5))
plt.bar(df['categoria'], df['ventas'])
plt.title('Ventas por Categoría')
plt.xlabel('Categoría')
plt.ylabel('Ventas')
plt.show()

# 2. Scatter plot
plt.figure(figsize=(10, 5))
plt.scatter(df['ventas'], df['profit'])
plt.title('Ventas vs Profit')
plt.xlabel('Ventas')
plt.ylabel('Profit')
for i, txt in enumerate(df['categoria']):
    plt.annotate(txt, (df['ventas'][i], df['profit'][i]))
plt.show()

# 3. Gráfico circular (usar con precaución)
plt.figure(figsize=(8, 8))
plt.pie(df['ventas'], labels=df['categoria'], autopct='%1.1f%%')
plt.title('Distribución de Ventas')
plt.show()
```

---

## Ejercicios de Comunicación de Datos

### Ejercicio 13: Principios de Storytelling
Investigar y practicar:
1. ¿Qué es elstory arc en la comunicación de datos?
2. ¿Cómo estructurar un narrativa con datos?
3. ¿Qué hace a una visualización efectiva?

### Ejercicio 14: Dashboard Design
Investigar:
1. ¿Qué es un dashboard efectivo?
2. ¿Cuáles son los principios de diseño de dashboards?
3. Ejemplos de dashboards famous

---

## Ejercicios de Investigación

### Ejercicio 15: Aplicaciones de Regresión Logística
Investigar:
1. ¿Qué es la regresión multinomial?
2. ¿Qué es la regresión ordinal?
3. Ejemplos de uso en medicina, finanzas, marketing

### Ejercicio 16: Métricas Avanzadas
Investigar:
1. ¿Qué es specificity?
2. ¿Qué es sensitivity?
3. ¿Qué es la curva Precision-Recall y cuándo usarla?
4. ¿Qué es el coeficiente de correlación de Matthews (MCC)?

---

## Recursos Adicionales

### Documentación
- Scikit-learn - Logistic Regression
- Statsmodels - Logistic Regression
- matplotlib - Visualization

### Videos
- StatQuest - Logistic Regression
- Data School - Classification metrics

---

## Nota Final
¡Felicidades! Has completado todos los temas del curso de Ciencia de Datos. Ahora estás preparado para:
- Analizar datos con Python
- Construir modelos de regresión (lineal y logística)
- Comunicar resultados efectivamente
- Aplicar principios éticos en el manejo de datos
