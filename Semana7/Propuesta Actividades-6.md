# Actividades Prácticas - Semana 7

## Preparación para: Entrega Final del Proyecto

**Temas cubiertos:** Regresión logística binaria en Python (Partes 1 y 2), Estrategias de comunicación de datos en Python

---

## IMPORTANTE: Ejercicios Complementarios

Antes de comenzar con las actividades prácticas, es **fundamental** completar los ejercicios del archivo [`Ejercicios Complementarios.md`](Ejercicios%20Complementarios.md).

### ¿Por qué realizar estos ejercicios?

Los ejercicios complementarios te proporcionan la base matemática y estadística necesaria para:

1. **Comprender funciones exponenciales y logaritmos**
2. **Entender la función sigmoide** y probabilidades
3. **Manejar Odds y Odds Ratio**
4. **Evaluar modelos** usando matriz de confusión, ROC/AUC
5. **Comunicar resultados** de manera efectiva

> **Justificación:** Estos conocimientos son prerrequisitos básicos que facilitan la comprensión de regresión logística y comunicación de datos. Sin esta base, será más difícil completar las actividades prácticas de manera efectiva.

**Tiempo estimado:** 1-2 horas

---

## Objetivo

Estas actividades prácticas te prepararán para completar la Entrega Final del Proyecto, enfocándose en regresión logística y comunicación de resultados.

---

## GIT: Recordatorio de Comandos

```bash
# Ver estado
git status

# Agregar cambios
git add .

# Crear commit
git commit -m "Mensaje descriptivo"

# Subir al repositorio
git push origin main

# Actualizar repositorio local
git pull origin main
```

---

## Actividades Propuestas

### Actividad 7.1: Regresión Logística - Introducción

**Descripción:** Aprende los conceptos de regresión logística.

**Instrucciones:**
1. Investiga la diferencia entre regresión lineal y logística
2. Entiende el concepto de función sigmoide
3. Aprende qué son los odds y odds ratio
4. Explica cuándo usar regresión logística

**Carpeta de entrega:** `Semana7/Actividades/Actividad7.1/`

**Git:**
```bash
git add Semana7/Actividades/Actividad7.1/
git commit -m "Semana7: Actividad 7.1 - Intro a regresión logística"
git push
```

---

### Actividad 7.2: Regresión Logística - Implementación

**Descripción:** Implementa un modelo de regresión logística.

**Instrucciones:**
1. Usa un dataset de clasificación binaria
2. Prepara los datos (codificación, escalado)
3. Divide en entrenamiento y prueba
4. Entrena el modelo de regresión logística
5. Realiza predicciones
6. Evalúa usando accuracy, precisión, recall, F1

**Carpeta de entrega:** `Semana7/Actividades/Actividad7.2/`

**Git:**
```bash
git add Semana7/Actividades/Actividad7.2/
git commit -m "Semana7: Actividad 7.2 - Regresión logística"
git push
```

---

### Actividad 7.3: Matriz de Confusión y Métricas

**Descripción:** Aprende a evaluar modelos de clasificación.

**Instrucciones:**
1. Continúa con el modelo de la actividad anterior
2. Crea la matriz de confusión
3. Calcula todas las métricas:
   - Accuracy
   - Precisión
   - Recall/Sensitivity
   - Specificity
   - F1-Score
4. Crea la curva ROC
5. Calcula el AUC
6. Interpreta los resultados

**Carpeta de entrega:** `Semana7/Actividades/Actividad7.3/`

**Git:**
```bash
git add Semana7/Actividades/Actividad7.3/
git commit -m "Semana7: Actividad 7.3 - Métricas de evaluación"
git push
```

---

### Actividad 7.4: Comunicación de Resultados

**Descripción:** Practica comunicar resultados de análisis.

**Instrucciones:**
1. Toma el análisis de actividades anteriores
2. Crea visualizaciones efectivas:
   - Gráficas de dispersión
   - Gráficos de barras
   - Mapas de calor
3. Redacta un informe ejecutivo
4. Incluye:
   - Resumen de hallazgos
   - Visualizaciones clave
   - Recomendaciones
5. Practica storytelling con datos

**Carpeta de entrega:** `Semana7/Actividades/Actividad7.4/`

**Git:**
```bash
git add Semana7/Actividades/Actividad7.4/
git commit -m "Semana7: Actividad 7.4 - Comunicación de resultados"
git push
```

---

### Actividad 7.5: Proyecto Final - Entrega

**Descripción:** Prepara y entrega tu proyecto final.

**Instrucciones:**
1. Reúne todo el trabajo del curso
2. Asegúrate de incluir:
   - Limpieza de datos
   - Análisis exploratorio
   - Modelo predictivo (regresión múltiple o logística)
   - Evaluación del modelo
   - Visualizaciones
   - Comunicación de resultados
3. Revisa que todo esté bien documentado
4. Prepara la presentación final

**Carpeta de entrega:** `Semana7/ProyectoFinal/`

**Git:**
```bash
git add Semana7/ProyectoFinal/
git commit -m "Semana7: Entrega final del proyecto"
git push
```

---

## Actualizar Documentación Semanal

Crea/actualiza el archivo `Documentacion/Semana7.md`:

```markdown
# Semana 7: Regresión Logística y Comunicación

## Fecha: [DD/MM/AAAA]

## Actividades Completadas
- [ ] Actividad 7.1: Intro a Regresión Logística
- [ ] Actividad 7.2: Implementación
- [ ] Actividad 7.3: Métricas de Evaluación
- [ ] Actividad 7.4: Comunicación de Resultados
- [ ] Entrega Final del Proyecto

## Resultados del Proyecto
- [Documenta los hallazgos principales]

## Conclusiones
- [Conclusiones del curso]

## Commits Realizados
- Listar los commits de esta semana
```

**Git:**
```bash
git add Documentacion/Semana7.md
git commit -m "Semana7: Documentación final actualizada"
git push
```

---

## Actualizar README Final

Actualiza tu `README.md` con el progreso completo:

```markdown
## Progreso

- [x] Semana 1: Fundamentos y Big Data
- [x] Semana 2: Arquitecturas y MongoDB
- [x] Semana 3: Python y Análisis Exploratorio
- [x] Semana 4: Preparación de Datos
- [x] Semana 5: Regresión Lineal Simple
- [x] Semana 6: Regresión Lineal Múltiple
- [x] Semana 7: Regresión Logística y Comunicación

## Proyecto Final
- [x] Entregado
```

```bash
git add README.md
git commit -m "README: Curso completado"
git push
```

---

## Recursos Adicionales

- Sklearn Logistic Regression: https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
- Matplotlib Gallery: https://matplotlib.org/stable/gallery/index.html

---

## Recordatorio

La Entrega Final del Proyecto tiene una ponderación del 35% y cubre los Temas 16, 17 y 18 del temario.

---

## 📋 Consolidado Semanal: Semana 7

Al finalizar todas las actividades de esta semana, debes crear un archivo consolidado llamado `Semana7_Consolidado.md` que contenga:

### Estructura del consolidado:

```markdown
# Semana 7: Regresión Logística y Comunicación de Datos

## 1. Ejercicios Complementarios

### Ejercicio 1: [Nombre]
**Solución:**
[Tu respuesta/solución]

### Ejercicio 2: [Nombre]
**Solución:**
[Tu respuesta/solución]

## 2. Actividades Prácticas

### Actividad 7.1: [Nombre]
**Entregable:** [Descripción]

### Actividad 7.2: [Nombre]
**Entregable:** [Descripción]

## 3. Resultados del Modelo de Clasificación

- Accuracy: [Valor]
- Precisión: [Valor]
- Recall: [Valor]
- F1-Score: [Valor]
- AUC: [Valor]

## 4. Comunicación de Resultados

- Visualizaciones creadas: [Lista]
- Hallazgos principales: [Lista]
- Recomendaciones: [Lista]

## 5. Resumen de Aprendizaje

- [Aprendizaje 1]
- [Aprendizaje 2]
- [Aprendizaje 3]

## 6. Dudas o Preguntas

- [Pregunta 1]
- [Pregunta 2]

## 7. Referencias

- [Referencia 1]
- [Referencia 2]
```

### Instrucciones de entrega:
1. Completa todos los ejercicios y actividades
2. Organiza todo en el archivo consolidado
3. Guarda en `Semana7/Semana7_Consolidado.md`
4. Realiza el commit correspondiente:
   ```bash
   git add Semana7/
   git commit -m "Semana7: Consolidado completo"
   git push
   ```

---

## ✅ Entregable Final: Proyecto

**Fecha de entrega:** [Según calendario del curso]

**Ponderación:** 35%

**Temas evaluados:** T16, T17 y T18

**Instrucciones:**
1. Completa todos los ejercicios complementarios
2. Completa todas las actividades prácticas
3. Construye tu modelo de regresión logística
4. Evalúa el modelo con métricas apropiadas
5. Crea visualizaciones efectivas
6. Prepara el consolidado semanal
7. Prepara la presentación final
8. Entrega según las indicaciones del profesor

**Criterios de evaluación:**
- [ ] Completó los ejercicios complementarios
- [ ] Completó todas las actividades prácticas
- [ ] Modelo de regresión logística correctamente implementado
- [ ] Matriz de confusión y métricas calculadas
- [ ] Curva ROC y AUC presentados
- [ ] Visualizaciones efectivas
- [ ] Comunicación de resultados (storytelling)
- [ ] El consolidado está organizado y completo
- [ ] Commits realizados correctamente en Git
