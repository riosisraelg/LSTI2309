# 📋 Instrucciones para Completar el Proyecto Final - Semana 7

**Curso:** QR.LSTI2309TEO - Universidad Tecmilenio  
**Ponderación:** 35%  
**Fecha:** Mayo 2026

---

## ✅ Lo que YA está hecho

He preparado todo el material base para tu proyecto final:

### 1. **Datos del Proyecto** ✅
- ✅ Dataset de Airbnb copiado desde Semana 3 (`train.csv` - 74,111 registros)
- ✅ Ubicado en: `Semana7/ProyectoFinal/Datos/train.csv`

### 2. **Análisis Exploratorio (Fase I)** ✅
- ✅ Notebook completo de EDA: `Semana7/ProyectoFinal/import.ipynb`
- ✅ Incluye:
  - Carga de datos
  - Estadísticas descriptivas
  - Análisis de correlaciones (Pearson, Spearman, Kendall)
  - Detección de outliers
  - Visualizaciones (histogramas, boxplots, scatter plots, mapas de calor)
  - Identificación de variables clave

### 3. **Script de Limpieza** ✅
- ✅ Archivo: `Semana7/ProyectoFinal/Limpieza.py`
- ✅ Funciones incluidas:
  - Carga de datos
  - Análisis de valores faltantes
  - Imputación de valores numéricos
  - Eliminación de columnas irrelevantes
  - Detección de outliers (método IQR)
  - Codificación de variables categóricas
  - Normalización de datos
  - Pipeline completo de limpieza

### 4. **Documentación** ✅
- ✅ README del proyecto: `Semana7/ProyectoFinal/README.md`
- ✅ Consolidado semanal (plantilla): `Semana7/Consolidado/Semana7_Consolidado.md`
- ✅ Estructura de carpetas creada

---

## 🚀 Lo que DEBES hacer ahora

### Paso 1: Crear el Notebook del Modelo (PRIORITARIO)

Crea un nuevo notebook llamado `Modelo.ipynb` en `Semana7/ProyectoFinal/` con el siguiente contenido:

```python
# ============================================
# PROYECTO FINAL - MODELO DE REGRESIÓN LINEAL MÚLTIPLE
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from statsmodels.stats.outliers_influence import variance_inflation_factor
import warnings
warnings.filterwarnings('ignore')

# ============================================
# 1. CARGAR Y LIMPIAR DATOS
# ============================================

# Importar funciones de limpieza
import sys
sys.path.append('.')
from Limpieza import cargar_datos, pipeline_limpieza_completa

# Cargar datos
df = cargar_datos('Datos/train.csv')

# Aplicar limpieza
df_limpio = pipeline_limpieza_completa(df)

# ============================================
# 2. PREPARACIÓN DE VARIABLES
# ============================================

# Seleccionar variables numéricas para el modelo
variables_numericas = ['accommodates', 'bedrooms', 'beds', 'bathrooms']

# Variable objetivo
y = df_limpio['log_price']

# Variables independientes (solo numéricas por ahora)
X = df_limpio[variables_numericas]

# Eliminar filas con valores nulos
X = X.dropna()
y = y[X.index]

print(f"Dimensiones finales: X={X.shape}, y={y.shape}")

# ============================================
# 3. ANÁLISIS DE CORRELACIÓN
# ============================================

# Crear dataframe con todas las variables
df_modelo = X.copy()
df_modelo['log_price'] = y

# Matriz de correlación
plt.figure(figsize=(10, 8))
sns.heatmap(df_modelo.corr(), annot=True, fmt='.2f', cmap='RdBu_r', center=0)
plt.title('Matriz de Correlación - Variables del Modelo')
plt.tight_layout()
plt.savefig('Visualizaciones/correlacion_modelo.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# 4. ANÁLISIS DE MULTICOLINEALIDAD (VIF)
# ============================================

# Calcular VIF para cada variable
vif_data = pd.DataFrame()
vif_data["Variable"] = X.columns
vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(len(X.columns))]

print("\n📊 Análisis de Multicolinealidad (VIF):")
print(vif_data)
print("\nInterpretación:")
print("- VIF < 5: No hay multicolinealidad")
print("- VIF 5-10: Multicolinealidad moderada")
print("- VIF > 10: Multicolinealidad alta (considerar eliminar variable)")

# ============================================
# 5. DIVISIÓN DE DATOS
# ============================================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\n📊 División de datos:")
print(f"Entrenamiento: {X_train.shape[0]} registros ({X_train.shape[0]/len(X)*100:.1f}%)")
print(f"Prueba: {X_test.shape[0]} registros ({X_test.shape[0]/len(X)*100:.1f}%)")

# ============================================
# 6. CONSTRUCCIÓN Y ENTRENAMIENTO DEL MODELO
# ============================================

# Crear modelo
modelo = LinearRegression()

# Entrenar modelo
modelo.fit(X_train, y_train)

print("\n✅ Modelo entrenado exitosamente!")

# Mostrar coeficientes
coeficientes = pd.DataFrame({
    'Variable': X.columns,
    'Coeficiente': modelo.coef_
}).sort_values('Coeficiente', ascending=False)

print("\n📊 Coeficientes del Modelo:")
print(coeficientes)
print(f"\nIntercepto: {modelo.intercept_:.4f}")

# ============================================
# 7. PREDICCIONES
# ============================================

# Predicciones en conjunto de entrenamiento
y_train_pred = modelo.predict(X_train)

# Predicciones en conjunto de prueba
y_test_pred = modelo.predict(X_test)

print("\n✅ Predicciones realizadas!")

# ============================================
# 8. EVALUACIÓN DEL MODELO
# ============================================

# Métricas en conjunto de entrenamiento
r2_train = r2_score(y_train, y_train_pred)
mse_train = mean_squared_error(y_train, y_train_pred)
rmse_train = np.sqrt(mse_train)
mae_train = mean_absolute_error(y_train, y_train_pred)

# Métricas en conjunto de prueba
r2_test = r2_score(y_test, y_test_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = np.sqrt(mse_test)
mae_test = mean_absolute_error(y_test, y_test_pred)

# R² ajustado
n = X_test.shape[0]
p = X_test.shape[1]
r2_adj_test = 1 - (1 - r2_test) * (n - 1) / (n - p - 1)

print("\n📊 MÉTRICAS DE EVALUACIÓN:")
print("="*60)
print(f"{'Métrica':<20} {'Entrenamiento':<20} {'Prueba':<20}")
print("="*60)
print(f"{'R²':<20} {r2_train:<20.4f} {r2_test:<20.4f}")
print(f"{'R² Ajustado':<20} {'-':<20} {r2_adj_test:<20.4f}")
print(f"{'MSE':<20} {mse_train:<20.4f} {mse_test:<20.4f}")
print(f"{'RMSE':<20} {rmse_train:<20.4f} {rmse_test:<20.4f}")
print(f"{'MAE':<20} {mae_train:<20.4f} {mae_test:<20.4f}")
print("="*60)

print("\n📝 Interpretación:")
print(f"- El modelo explica el {r2_test*100:.2f}% de la variabilidad del precio")
print(f"- Error promedio: {mae_test:.4f} unidades de log_price")
print(f"- RMSE: {rmse_test:.4f} (penaliza errores grandes)")

# ============================================
# 9. VISUALIZACIONES
# ============================================

# 9.1 Predicciones vs Valores Reales
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_test_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 'r--', lw=2)
plt.xlabel('Valores Reales (log_price)')
plt.ylabel('Valores Predichos (log_price)')
plt.title('Predicciones vs Valores Reales')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Visualizaciones/predicciones_vs_reales.png', dpi=300, bbox_inches='tight')
plt.show()

# 9.2 Importancia de Características (Coeficientes)
plt.figure(figsize=(10, 6))
coeficientes_sorted = coeficientes.sort_values('Coeficiente')
plt.barh(coeficientes_sorted['Variable'], coeficientes_sorted['Coeficiente'])
plt.xlabel('Coeficiente')
plt.title('Importancia de Características (Coeficientes del Modelo)')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.savefig('Visualizaciones/importancia_caracteristicas.png', dpi=300, bbox_inches='tight')
plt.show()

# 9.3 Distribución de Residuos
residuos = y_test - y_test_pred

fig, axes = plt.subplots(1, 2, figsize=(15, 5))

# Histograma de residuos
axes[0].hist(residuos, bins=50, edgecolor='black')
axes[0].set_xlabel('Residuos')
axes[0].set_ylabel('Frecuencia')
axes[0].set_title('Distribución de Residuos')
axes[0].axvline(x=0, color='r', linestyle='--', linewidth=2)
axes[0].grid(True, alpha=0.3)

# Residuos vs Predicciones
axes[1].scatter(y_test_pred, residuos, alpha=0.5)
axes[1].axhline(y=0, color='r', linestyle='--', linewidth=2)
axes[1].set_xlabel('Valores Predichos')
axes[1].set_ylabel('Residuos')
axes[1].set_title('Residuos vs Valores Predichos')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('Visualizaciones/analisis_residuos.png', dpi=300, bbox_inches='tight')
plt.show()

# 9.4 Q-Q Plot (Normalidad de Residuos)
from scipy import stats

plt.figure(figsize=(8, 6))
stats.probplot(residuos, dist="norm", plot=plt)
plt.title('Q-Q Plot - Normalidad de Residuos')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('Visualizaciones/qq_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================
# 10. TABLA DE PREDICCIONES (MUESTRA)
# ============================================

# Crear tabla con muestra de predicciones
muestra = pd.DataFrame({
    'Real': y_test[:10].values,
    'Predicho': y_test_pred[:10],
    'Error': (y_test[:10].values - y_test_pred[:10]),
    'Error_Abs': np.abs(y_test[:10].values - y_test_pred[:10]),
    'Error_%': (np.abs(y_test[:10].values - y_test_pred[:10]) / y_test[:10].values * 100)
})

print("\n📊 MUESTRA DE PREDICCIONES (primeras 10):")
print(muestra.to_string(index=False))

# ============================================
# 11. CONCLUSIONES
# ============================================

print("\n" + "="*60)
print("📝 CONCLUSIONES DEL MODELO")
print("="*60)
print(f"""
1. RENDIMIENTO DEL MODELO:
   - R² = {r2_test:.4f}: El modelo explica el {r2_test*100:.2f}% de la variabilidad
   - RMSE = {rmse_test:.4f}: Error promedio en escala logarítmica
   
2. VARIABLES MÁS IMPORTANTES:
   {coeficientes.to_string(index=False)}
   
3. CALIDAD DE PREDICCIONES:
   - Error absoluto medio: {mae_test:.4f}
   - El modelo {'tiene buen ajuste' if r2_test > 0.7 else 'tiene ajuste moderado' if r2_test > 0.5 else 'necesita mejoras'}
   
4. SUPUESTOS DEL MODELO:
   - Revisar Q-Q plot para normalidad de residuos
   - Revisar gráfico de residuos vs predicciones para homocedasticidad
   
5. RECOMENDACIONES:
   - {'Considerar agregar más variables' if r2_test < 0.7 else 'El modelo es adecuado'}
   - {'Revisar multicolinealidad (VIF alto)' if vif_data['VIF'].max() > 10 else 'No hay problemas de multicolinealidad'}
   - Considerar transformaciones no lineales si es necesario
""")

print("\n✅ Análisis completado exitosamente!")
print("📁 Visualizaciones guardadas en: Visualizaciones/")
```

---

### Paso 2: Ejecutar el Notebook

1. Abre Jupyter Notebook:
   ```bash
   cd Semana7/ProyectoFinal
   jupyter notebook
   ```

2. Ejecuta todas las celdas del notebook `Modelo.ipynb`

3. Revisa las visualizaciones generadas en `Visualizaciones/`

---

### Paso 3: Completar el Consolidado

Abre `Semana7/Consolidado/Semana7_Consolidado.md` y completa:

1. **Sección 4: Resultados del Modelo**
   - Copia los valores de R², MSE, RMSE del notebook
   - Copia la tabla de coeficientes
   - Interpreta los resultados

2. **Sección 5: Comunicación de Resultados**
   - Describe las visualizaciones
   - Escribe la narrativa ejecutiva
   - Incluye recomendaciones

3. **Sección 6: Resumen de Aprendizaje**
   - Reflexiona sobre lo aprendido
   - Identifica desafíos y logros

---

### Paso 4: Hacer Commits en Git

```bash
# Agregar todos los archivos
git add Semana7/

# Commit del proyecto completo
git commit -m "Semana7: Proyecto final completo - Modelo de regresión lineal múltiple"

# Subir a GitHub
git push origin semana7
```

---

## 📊 Estructura Final del Proyecto

```
Semana7/
├── Consolidado/
│   └── Semana7_Consolidado.md          ✅ Plantilla lista
├── ProyectoFinal/
│   ├── Datos/
│   │   └── train.csv                   ✅ Datos copiados
│   ├── Visualizaciones/
│   │   ├── correlacion_modelo.png      ⏳ Se generará
│   │   ├── predicciones_vs_reales.png  ⏳ Se generará
│   │   ├── importancia_caracteristicas.png ⏳ Se generará
│   │   ├── analisis_residuos.png       ⏳ Se generará
│   │   └── qq_plot.png                 ⏳ Se generará
│   ├── import.ipynb                    ✅ EDA completo
│   ├── Modelo.ipynb                    ⏳ CREAR ESTE
│   ├── Limpieza.py                     ✅ Script listo
│   └── README.md                       ✅ Documentación lista
├── Ejercicios Complementarios-6.md     ✅ Ejercicios disponibles
├── Index-7.md                          ✅ Índice de la semana
├── Propuesta Actividades-6.md          ✅ Actividades propuestas
└── Proyecto - Entrega final.md         ✅ Instrucciones oficiales
```

---

## ⚠️ Puntos Importantes

### 1. Interpretación de Resultados

**R² (Coeficiente de Determinación):**
- R² = 0.7 → El modelo explica el 70% de la variabilidad (BUENO)
- R² = 0.5 → El modelo explica el 50% de la variabilidad (MODERADO)
- R² < 0.3 → El modelo necesita mejoras (BAJO)

**MSE (Error Cuadrático Medio):**
- Mientras más bajo, mejor
- Penaliza errores grandes más que errores pequeños

**VIF (Factor de Inflación de Varianza):**
- VIF < 5: No hay multicolinealidad ✅
- VIF 5-10: Multicolinealidad moderada ⚠️
- VIF > 10: Multicolinealidad alta ❌ (eliminar variable)

---

### 2. Comunicación de Resultados

**Estructura de la narrativa:**
1. **Contexto:** ¿Por qué es importante este análisis?
2. **Metodología:** ¿Qué hiciste?
3. **Hallazgos:** ¿Qué descubriste?
4. **Recomendaciones:** ¿Qué acciones sugieres?
5. **Limitaciones:** ¿Qué no cubre el modelo?

---

### 3. Rúbrica de Evaluación (35%)

| Componente | Peso | Qué evalúa |
|------------|------|------------|
| **Actividad Evaluable** | 70% (24.5%) | Modelo predictivo y comunicación |
| **Ejercicios Complementarios** | 10% (1.7%) | Regresión logística, métricas |
| **Actividades Prácticas** | 10% (1.7%) | Actividades 7.1-7.5 |
| **Documentación** | 10% (1.7%) | Consolidado semanal |

**Desglose de Actividad Evaluable (24.5%):**
- Limpieza de datos: 3%
- Identificación de variables: 2%
- Selección de características: 3%
- Análisis de correlación: 2%
- División de datos: 2%
- Construcción del modelo: 3%
- Manejo de multicolinealidad: 2.5%
- Evaluación (R², R² ajustado): 2%
- Predicciones: 2%
- MSE: 3%
- Visualizaciones: 2%
- Importancia de características: 2%
- Narrativa: 2%
- Conclusiones: 2%

---

## 🎯 Checklist Final

Antes de entregar, verifica:

- [ ] Notebook `Modelo.ipynb` creado y ejecutado
- [ ] Todas las visualizaciones generadas
- [ ] Consolidado completado con tus resultados
- [ ] README actualizado con tus datos personales
- [ ] Commits realizados en Git
- [ ] Código comentado y documentado
- [ ] Interpretaciones escritas (no solo números)
- [ ] Narrativa ejecutiva completa
- [ ] Recomendaciones accionables incluidas

---

## 📚 Recursos Adicionales

### Videos Recomendados
- StatQuest - Linear Regression: https://www.youtube.com/watch?v=nk2CQITm_eo
- StatQuest - R-squared: https://www.youtube.com/watch?v=2AQKmw14mHM

### Documentación
- Scikit-learn Linear Regression: https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html
- Statsmodels VIF: https://www.statsmodels.org/stable/generated/statsmodels.stats.outliers_influence.variance_inflation_factor.html

---

## ❓ Preguntas Frecuentes

**P: ¿Debo eliminar los outliers?**
R: Depende. Si son errores de datos, sí. Si son valores legítimos (propiedades premium), considera mantenerlos o crear una variable categórica.

**P: ¿Qué hago si mi R² es bajo (<0.5)?**
R: Considera agregar más variables, transformaciones no lineales, o interacciones entre variables.

**P: ¿Debo usar todas las variables?**
R: No. Usa solo las que tienen sentido teórico y estadístico. Evita multicolinealidad.

**P: ¿Cómo interpreto un coeficiente negativo?**
R: Significa que cuando esa variable aumenta, el precio disminuye (relación inversa).

---

## 🎉 ¡Éxito en tu Proyecto Final!

Has recibido:
- ✅ Todos los datos necesarios
- ✅ Análisis exploratorio completo
- ✅ Script de limpieza funcional
- ✅ Plantillas de documentación
- ✅ Código completo del modelo
- ✅ Instrucciones detalladas

**Solo necesitas:**
1. Crear y ejecutar el notebook `Modelo.ipynb`
2. Completar el consolidado con tus resultados
3. Hacer los commits en Git
4. ¡Entregar!

---

**¿Dudas?** Revisa:
- `Proyecto - Entrega final.md` (instrucciones oficiales)
- `README.md` (documentación del proyecto)
- `Ejercicios Complementarios-6.md` (conceptos teóricos)

**¡Mucho éxito! 🚀**
