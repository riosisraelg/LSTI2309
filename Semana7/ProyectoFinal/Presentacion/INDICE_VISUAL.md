# 📑 Índice Visual de la Presentación

## Estructura Completa (25 diapositivas)

---

### 🎬 INICIO

#### Diapositiva 1: Portada
- Título: "Análisis Predictivo del Mercado Inmobiliario"
- Subtítulo: "Regresión Lineal Múltiple - Airbnb Dataset"
- Universidad Tecmilenio
- Curso: QR.LSTI2309TEO

#### Diapositiva 2: Contenido
- Índice automático con las 10 secciones

---

### 📖 SECCIÓN 1: INTRODUCCIÓN (2 diapositivas)

#### Diapositiva 3: Contexto del Proyecto
**Contenido:**
- Objetivo del proyecto
- Dataset original: 74,111 obs × 29 vars
- Metodología en 4 pasos

**Elementos visuales:**
- 2 columnas
- Bloques de información
- Bullets

---

### 🧹 SECCIÓN 2: LIMPIEZA DE DATOS (2 diapositivas)

#### Diapositiva 4: Proceso de Limpieza
**Contenido:**
1. Imputación de valores faltantes
2. Eliminación de columnas irrelevantes
3. Detección y eliminación de outliers

**Elementos visuales:**
- Enumeración
- Sub-bullets
- Énfasis en variables

#### Diapositiva 5: Resultados de la Limpieza
**Contenido:**
- Tabla comparativa Original vs Limpio
- Alerta con resultado final

**Elementos visuales:**
- Tabla profesional (booktabs)
- Alert block
- Números destacados

---

### 🔍 SECCIÓN 3: ANÁLISIS EXPLORATORIO (4 diapositivas)

#### Diapositiva 6: Análisis de Multicolinealidad - VIF
**Contenido:**
- Variables problemáticas (beds, review_scores_rating)
- Decisión de eliminación
- **Gráfica:** `05_analisis_vif.png`

**Elementos visuales:**
- 2 columnas (texto + imagen)
- Checkmarks y X marks
- Imagen a la derecha

#### Diapositiva 7: Recálculo de VIF - Segunda Iteración
**Contenido:**
- **Gráfica:** `06_vif_segunda_iteracion.png` (comparación antes/después)
- Bloque de resultado exitoso

**Elementos visuales:**
- Imagen grande centrada
- Block con mensaje de éxito

#### Diapositiva 8: Análisis de Correlación
**Contenido:**
- **Gráfica:** `09_matriz_correlacion_corner.png`
- Matriz triangular inferior

**Elementos visuales:**
- Imagen centrada
- Subtítulo descriptivo

#### Diapositiva 9: Correlaciones con log_price
**Contenido:**
- **Gráfica:** `10_correlaciones_log_price_barras.png`
- Lista de correlaciones principales

**Elementos visuales:**
- Imagen grande
- Bullets con valores numéricos
- Colores para positivo/negativo

#### Diapositiva 10: Pairplot
**Contenido:**
- **Gráfica:** `08_pairplot_correlaciones.png`
- Relaciones entre todas las variables

**Elementos visuales:**
- Imagen a pantalla completa

---

### 🏷️ SECCIÓN 4: VARIABLES CATEGÓRICAS (1 diapositiva)

#### Diapositiva 11: Análisis de room_type
**Contenido:**
- **Gráfica:** `07_analisis_room_type.png` (distribución + precio)
- Bloque sobre transformación a dummies

**Elementos visuales:**
- Imagen grande
- Block informativo

---

### 🎯 SECCIÓN 5: SELECCIÓN DE VARIABLES (2 diapositivas)

#### Diapositiva 12: Variables Finales del Modelo
**Contenido:**
- Variable dependiente: log_price
- Variables independientes:
  - 2 numéricas (accommodates, bedrooms)
  - 3 dummies (room_type)

**Elementos visuales:**
- Bloques diferenciados
- Bullets organizados

#### Diapositiva 13: Justificación de Exclusiones
**Contenido:**
- Tabla con decisiones y justificaciones
- Variables excluidas vs incluidas

**Elementos visuales:**
- Tabla profesional
- Colores para decisiones (rojo/verde)

---

### ✂️ SECCIÓN 6: DIVISIÓN DE DATOS (1 diapositiva)

#### Diapositiva 14: Train-Test Split
**Contenido:**
- **Gráfica:** `11_distribucion_train_test.png`
- Estadísticas: 80% train, 20% test
- Random state: 42

**Elementos visuales:**
- Imagen grande (histogramas comparativos)
- Bullets con números

---

### 🤖 SECCIÓN 7: MODELO DE REGRESIÓN (3 diapositivas)

#### Diapositiva 15: Construcción del Modelo
**Contenido:**
- Ecuación del modelo (LaTeX)
- Método: OLS
- Especificaciones técnicas

**Elementos visuales:**
- Ecuación matemática
- Block con fórmula
- Bullets informativos

#### Diapositiva 16: Coeficientes del Modelo
**Contenido:**
- **Gráfica:** `12_coeficientes_modelo.png`
- Barras horizontales con coeficientes

**Elementos visuales:**
- Imagen grande centrada
- Colores verde/rojo para positivo/negativo

#### Diapositiva 17: Interpretación de Coeficientes
**Contenido:**
- Tabla con coeficientes numéricos
- Bloque de interpretación práctica

**Elementos visuales:**
- Tabla pequeña
- Block con ejemplos
- Porcentajes de impacto

---

### 📊 SECCIÓN 8: EVALUACIÓN (2 diapositivas)

#### Diapositiva 18: Métricas de Rendimiento
**Contenido:**
- Tabla comparativa Train vs Test
- Interpretación del R²
- Análisis de sobreajuste

**Elementos visuales:**
- Tabla profesional
- Block de interpretación
- Alert block para sobreajuste

#### Diapositiva 19: Comparación de Métricas
**Contenido:**
- **Gráfica:** `14_metricas_error_comparacion.png`
- Barras comparativas MSE, RMSE, MAE

**Elementos visuales:**
- Imagen grande centrada

---

### 🎯 SECCIÓN 9: PREDICCIONES (2 diapositivas)

#### Diapositiva 20: Análisis de Predicciones
**Contenido:**
- **Gráfica:** `13_analisis_predicciones.png`
- 4 subgráficas:
  1. Real vs Predicción
  2. Distribución de errores
  3. Residuos vs Predicciones
  4. Q-Q Plot

**Elementos visuales:**
- Imagen a pantalla completa

#### Diapositiva 21: Estadísticas de Errores
**Contenido:**
- Tabla con estadísticas de error
- Bloque de interpretación

**Elementos visuales:**
- Tabla profesional
- Block con conclusiones
- Bullets explicativos

---

### 💡 SECCIÓN 10: CONCLUSIONES (4 diapositivas)

#### Diapositiva 22: Hallazgos Principales
**Contenido:**
1. Predictor principal: accommodates
2. Tipo de habitación: factor crítico
3. Variables excluidas y razones

**Elementos visuales:**
- Enumeración
- Sub-bullets
- Énfasis en números clave

#### Diapositiva 23: Calidad del Modelo
**Contenido:**
- 2 columnas: Fortalezas vs Limitaciones
- Alert block con conclusión

**Elementos visuales:**
- Columnas balanceadas
- Checkmarks y X marks
- Alert destacado

#### Diapositiva 24: Recomendaciones
**Contenido:**
- Bloque: Para mejorar el modelo (5 puntos)
- Bloque: Aplicaciones prácticas (3 puntos)

**Elementos visuales:**
- 2 bloques diferenciados
- Enumeraciones
- Bullets

#### Diapositiva 25: Resumen Ejecutivo
**Contenido:**
- Título grande centrado
- Tabla resumen con métricas clave
- Conclusión principal destacada

**Elementos visuales:**
- Centrado
- Tabla compacta
- Texto en alert

---

### 🎬 CIERRE

#### Diapositiva 26: ¿Preguntas?
**Contenido:**
- Título grande: "¿Preguntas?"
- Información del proyecto
- Universidad y curso

**Elementos visuales:**
- Fondo plano (plain)
- Texto centrado
- Jerarquía de tamaños

---

## 📊 Resumen de Elementos Visuales

### Gráficas Utilizadas (10)
1. ✅ VIF inicial
2. ✅ VIF segunda iteración
3. ✅ Análisis room_type
4. ✅ Pairplot
5. ✅ Matriz correlación
6. ✅ Correlaciones con log_price
7. ✅ Distribución train/test
8. ✅ Coeficientes modelo
9. ✅ Análisis predicciones
10. ✅ Comparación métricas

### Tablas (5)
1. Resultados limpieza
2. Justificación exclusiones
3. Coeficientes numéricos
4. Métricas rendimiento
5. Estadísticas errores

### Bloques Especiales (8)
- Objetivos
- Resultados
- Transformaciones
- Interpretaciones
- Recomendaciones
- Aplicaciones
- Conclusiones
- Alertas

### Ecuaciones Matemáticas (1)
- Ecuación del modelo de regresión

---

## 🎨 Paleta de Colores

- **tecblue** (RGB: 0,56,101) - Azul institucional
- **tecgreen** (RGB: 0,128,96) - Verde institucional
- **Verde** - Elementos positivos, inclusiones
- **Rojo** - Elementos negativos, exclusiones
- **Negro** - Texto principal
- **Gris** - Texto secundario

---

## 📏 Dimensiones y Proporciones

- **Imágenes grandes:** `width=\textwidth` (100%)
- **Imágenes medianas:** `width=0.85\textwidth` (85%)
- **Imágenes pequeñas:** `width=0.7\textwidth` (70%)
- **Columnas:** 50-50 balanceadas
- **Márgenes:** Automáticos con `tight_layout`

---

## ✅ Checklist de Calidad

- [x] Todas las secciones del proyecto cubiertas
- [x] 10 visualizaciones incluidas
- [x] Tablas profesionales con booktabs
- [x] Ecuaciones matemáticas correctas
- [x] Colores consistentes
- [x] Jerarquía visual clara
- [x] Texto conciso (bullets cortos)
- [x] Números destacados
- [x] Conclusiones claras
- [x] Recomendaciones accionables

---

## 🎯 Tiempo Estimado de Presentación

- **Introducción:** 2 min
- **Limpieza:** 2 min
- **Análisis Exploratorio:** 4 min
- **Variables Categóricas:** 1 min
- **Selección:** 2 min
- **División:** 1 min
- **Modelo:** 3 min
- **Evaluación:** 2 min
- **Predicciones:** 2 min
- **Conclusiones:** 3 min
- **Preguntas:** 3 min

**Total:** ~25 minutos

---

## 📝 Notas para el Presentador

1. **Diapositiva 6-7:** Enfatizar la importancia de eliminar multicolinealidad
2. **Diapositiva 9:** Destacar que accommodates tiene la mayor correlación
3. **Diapositiva 13:** Explicar claramente por qué se excluyeron variables
4. **Diapositiva 18:** Mencionar que no hay sobreajuste (buena señal)
5. **Diapositiva 20:** Señalar que los residuos son aproximadamente normales
6. **Diapositiva 22:** Resumir los 3 hallazgos principales
7. **Diapositiva 24:** Enfatizar las recomendaciones para trabajo futuro

---

¡Presentación lista para impresionar! 🚀
