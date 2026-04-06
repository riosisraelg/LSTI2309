# Ejercicios Complementarios - Semana 6

## Temas Cubiertos
- **T13**: Regresión lineal múltiple - parte 1
- **T14**: Regresión lineal múltiple - parte 2
- **T15**: Regresión lineal múltiple - parte 3

## Prerrequisitos Recomendados
- **Matemáticas**: Álgebra matricial, vectores, matrices, optimización, regularización
- **Estadística**: Extensión de regresión simple, multicolinealidad, R² ajustado, diagnóstico de residuos, validación cruzada
- **Programación**: Vectores y matrices, hyperparameter tuning

---

## Ejercicios de Álgebra Matricial

### Ejercicio 1: Operaciones con Matrices
```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Realizar:
# 1. Suma de matrices
# 2. Resta de matrices
# 3. Multiplicación escalar
# 4. Multiplicación de matrices (dot product)
# 5. Transpuesta
# 6. Inversa (si existe)
# 7. Determinante
```

### Ejercicio 2: Álgebra Matricial para Regresión
La ecuación normal de regresión:

```
β = (X^T * X)^-1 * X^T * y
```

```python
import numpy as np

# Datos: Y = salario, X1 = experiencia, X2 = educación
X = np.array([
    [1, 2, 12],   # (intercepto, años exp, años edu)
    [1, 3, 14],
    [1, 5, 16],
    [1, 8, 18],
    [1, 10, 20]
])
y = np.array([30000, 35000, 45000, 60000, 75000])

# Calcular coeficientes usando la fórmula
X_T = X.T
X_T_X = X_T @ X
X_T_X_inv = np.linalg.inv(X_T_X)
beta = X_T_X_inv @ X_T @ y

print(f"Coeficientes: {beta}")
```

---

## Ejercicios de Regresión Lineal Múltiple

### Ejercicio 3: Implementación con sklearn
```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Dataset de ejemplo (puedes usar cualquier dataset)
data = {
    'experiencia': [1, 2, 3, 5, 8, 10, 12, 15],
    'educacion': [12, 14, 16, 16, 18, 20, 22, 22],
    'edad': [22, 24, 26, 30, 35, 40, 45, 50],
    'salario': [30000, 35000, 42000, 55000, 70000, 85000, 100000, 120000]
}

df = pd.DataFrame(data)

X = df[['experiencia', 'educacion', 'edad']]
y = df['salario']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Crear y entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Predicciones
y_pred = modelo.predict(X_test)

# Métricas
print(f"R²: {r2_score(y_test, y_pred)}")
print(f"RMSE: {np.sqrt(mean_squared_error(y_test, y_pred))}")
print(f"Coeficientes: {modelo.coef_}")
print(f"Intercepto: {modelo.intercept_}")
```

### Ejercicio 4: R² Ajustado
El R² ajustado corrige por el número de predictores:

```
R²_adj = 1 - [(1-R²)(n-1) / (n-p-1)]
```

Dónde:
- n = número de observaciones
- p = número de predictores

```python
# Calcular R² ajustado manualmente
n = len(y)
p = X.shape[1]

r2 = modelo.score(X_test, y_test)
r2_adj = 1 - ((1-r2)*(n-1) / (n-p-1))

print(f"R²: {r2}")
print(f"R² ajustado: {r2_adj}")
```

---

## Ejercicios de Multicolinealidad

### Ejercicio 5: Factor de Inflación de Varianza (VIF)
```python
from statsmodels.stats.outliers_influence import variance_inflation_factor
import pandas as pd
import numpy as np

# Datos con posible multicolinealidad
df = pd.DataFrame({
    'X1': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'X2': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20],  # Alta correlación con X1
    'X3': [5, 3, 8, 2, 7, 1, 9, 4, 6, 10]
})

# Calcular VIF para cada variable
vif_data = pd.DataFrame()
vif_data["Variable"] = df.columns
vif_data["VIF"] = [variance_inflation_factor(df.values, i) for i in range(df.shape[1])]

print(vif_data)

# Interpretación:
# VIF > 10: Multicolinealidad problemática
# VIF > 5: Revisar multicolinealidad
```

---

## Ejercicios de Diagnóstico de Residuos

### Ejercicio 6: Pruebas de Heterocedasticidad
```python
import statsmodels.api as sm
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import het_breuschpagan, het_white

# Ajustar modelo OLS
X_with_const = sm.add_constant(X)
model = sm.OLS(y, X_with_const).fit()

# Residuos
residuos = model.resid
predichos = model.fittedvalues

# Prueba Breusch-Pagan
bp_test = het_breuschpagan(residuos, X_with_const)
print(f"Breusch-Pagan p-value: {bp_test[1]}")

# Prueba White
white_test = het_white(residuos, X_with_const)
print(f"White p-value: {white_test[1]}")

# Gráfico de residuos vs predichos
plt.scatter(predichos, residuos)
plt.axhline(y=0, color='r', linestyle='--')
plt.xlabel('Valores predichos')
plt.ylabel('Residuos')
plt.title('Residuos vs Predichos')
plt.show()
```

### Ejercicio 7: Normalidad de Residuos
```python
from scipy import stats

# Histograma
plt.hist(residuos, bins=10, density=True, alpha=0.6)
xmin, xmax = plt.xlim()
x = np.linspace(xmin, xmax, 100)
p = stats.norm.pdf(x, np.mean(residuos), np.std(residuos))
plt.plot(x, p, 'r', linewidth=2)
plt.show()

# Prueba Shapiro-Wilk
shapiro_stat, shapiro_p = stats.shapiro(residuos)
print(f"Shapiro-Wilk: stat={shapiro_stat}, p-value={shapiro_p}")

# Q-Q Plot
stats.probplot(residuos, dist="norm", plot=plt)
plt.show()
```

---

## Ejercicios de Regularización

### Ejercicio 8: Ridge Regression (L2)
```python
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler

# Escalar datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Ridge con diferentes alphas
alphas = [0.01, 0.1, 1, 10, 100]

for alpha in alphas:
    ridge = Ridge(alpha=alpha)
    ridge.fit(X_scaled, y)
    print(f"Alpha: {alpha}, Coef: {ridge.coef_}")
```

### Ejercicio 9: Lasso Regression (L1)
```python
from sklearn.linear_model import Lasso

# Lasso con diferentes alphas
for alpha in [0.01, 0.1, 1, 10]:
    lasso = Lasso(alpha=alpha)
    lasso.fit(X_scaled, y)
    print(f"Alpha: {alpha}, Coef: {lasso.coef_}")
    # Observar cómo algunos coeficientes se vuelven 0
```

### Ejercicio 10: Elastic Net
```python
from sklearn.linear_model import ElasticNet

# Elastic Net (combinación de Ridge y Lasso)
for l1_ratio in [0.1, 0.5, 0.9]:
    elastic = ElasticNet(alpha=1.0, l1_ratio=l1_ratio)
    elastic.fit(X_scaled, y)
    print(f"L1 ratio: {l1_ratio}, Coef: {elastic.coef_}")
```

---

## Ejercicios de Validación Cruzada

### Ejercicio 11: Cross-Validation
```python
from sklearn.model_selection import cross_val_score

# Regresión lineal simple
modelo = LinearRegression()
cv_scores = cross_val_score(modelo, X_scaled, y, cv=5, scoring='r2')

print(f"CV Scores: {cv_scores}")
print(f"Mean R²: {cv_scores.mean():.4f}")
print(f"Std R²: {cv_scores.std():.4f}")
```

### Ejercicio 12: Grid Search para Regularización
```python
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Ridge

# Grid search para Ridge
param_grid = {'alpha': [0.001, 0.01, 0.1, 1, 10, 100]}
ridge = Ridge()
grid_search = GridSearchCV(ridge, param_grid, cv=5, scoring='r2')
grid_search.fit(X_scaled, y)

print(f"Mejor alpha: {grid_search.best_params_}")
print(f"Mejor R²: {grid_search.best_score_}")
```

---

## Ejercicios de Investigación

### Ejercicio 13: Selección de Variables
Investigar:
1. ¿Qué es Forward Selection?
2. ¿Qué es Backward Elimination?
3. ¿Qué es Stepwise Regression?
4. ¿Cómo interpretar los coeficientes en presencia de multicolinealidad?

### Ejercicio 14: Aplicaciones Avanzadas
Investigar:
1. ¿Qué es Weighted Least Squares (WLS)?
2. ¿Qué es Generalized Least Squares (GLS)?
3. ¿Cuándo usar cada tipo de regresión?

---

## Recursos Adicionales

### Documentación
- Scikit-learn - Linear Models
- Statsmodels - Regression
- UCLA - Regression Diagnostics

### Videos
- StatQuest - Ridge & Lasso
- Josh Starmer - Multicollinearity

---

## Próxima Semana
En la Semana 7 cubriremos:
- **T16**: Regresión logística binaria - parte 1
- **T17**: Regresión logística binaria - parte 2
- **T18**: Estrategias de comunicación de datos en Python

**Prerrequisitos para próxima semana:**
- Funciones exponenciales, logaritmos, sigmoide
- Odds, Odds Ratio, probabilidad condicional
- Matriz de confusión, precisión, recall, F1-Score, AUC-ROC
