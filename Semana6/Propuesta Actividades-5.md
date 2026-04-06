# Actividades Prácticas - Semana 6

## Preparación para: Actividad 5

**Temas cubiertos:** Regresión lineal múltiple en Python (Partes 1, 2 y 3)

---

## IMPORTANTE: Ejercicios Complementarios

Antes de comenzar con las actividades prácticas, es **fundamental** completar los ejercicios del archivo [`Ejercicios Complementarios.md`](Ejercicios%20Complementarios.md).

### ¿Por qué realizar estos ejercicios?

Los ejercicios complementarios te proporcionan la base de álgebra y estadística necesaria para:

1. **Comprender álgebra matricial** para regresión múltiple
2. **Identificar multicolinealidad** y sus efectos
3. **Aplicar regularización** (Ridge, Lasso)
4. **Validar modelos** con cross-validation

> **Justificación:** Estos conocimientos son prerrequisitos básicos que facilitan la comprensión de regresión lineal múltiple. Sin esta base, será más difícil completar las actividades prácticas de manera efectiva.

**Tiempo estimado:** 1-2 horas

---

## Objetivo

Estas actividades prácticas te prepararán para completar la Actividad 5, enfocándose en regresión lineal múltiple y técnicas de selección de variables.

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

### Actividad 6.1: Regresión Lineal Múltiple - Básica

**Descripción:** Implementa una regresión lineal múltiple básica.

**Instrucciones:**
1. Usa un dataset con múltiples variables independientes
2. Selecciona la variable dependiente
3. Implementa regresión lineal múltiple
4. Interpreta los coeficientes
5. Calcula R² y R² ajustado
6. Compara con la regresión simple

**Carpeta de entrega:** `Semana6/Actividades/Actividad6.1/`

**Git:**
```bash
git add Semana6/Actividades/Actividad6.1/
git commit -m "Semana6: Actividad 6.1 - Regresión múltiple básica"
git push
```

---

### Actividad 6.2: Supuestos de Regresión Múltiple

**Descripción:** Verifica los supuestos en regresión múltiple.

**Instrucciones:**
1. Continúa con el modelo de actividad anterior
2. Verifica cada supuesto:
   - Linealidad (gráfica de residuos)
   - Independencia (Durbin-Watson)
   - Homocedasticidad (Breusch-Pagan)
   - Normalidad (Q-Q plot)
3. Si hay violaciones, sugiere soluciones
4. Documenta hallazgos

**Carpeta de entrega:** `Semana6/Actividades/Actividad6.2/`

**Git:**
```bash
git add Semana6/Actividades/Actividad6.2/
git commit -m "Semana6: Actividad 6.2 - Supuestos de regresión"
git push
```

---

### Actividad 6.3: Selección de Variables

**Descripción:** Practica técnicas de selección de variables.

**Instrucciones:**
1. Implementa los siguientes métodos:
   - Forward Selection
   - Backward Elimination
   - Stepwise Selection
2. Compara los resultados de cada método
3. Selecciona el mejor modelo
4. Justifica tu elección

**Carpeta de entrega:** `Semana6/Actividades/Actividad6.3/`

**Git:**
```bash
git add Semana6/Actividades/Actividad6.3/
git commit -m "Semana6: Actividad 6.3 - Selección de variables"
git push
```

---

### Actividad 6.4: Regularización (Ridge y Lasso)

**Descripción:** Aprende técnicas de regularización.

**Instrucciones:**
1. Implementa regresión Ridge
2. Implementa regresión Lasso
3. Compara coeficientes con OLS tradicional
4. Encuentra el mejor alpha usando cross-validation
5. Discute cuándo usar cada técnica

**Carpeta de entrega:** `Semana6/Actividades/Actividad6.4/`

**Git:**
```bash
git add Semana6/Actividades/Actividad6.4/
git commit -m "Semana6: Actividad 6.4 - Regularización"
git push
```

---

## Actualizar Documentación Semanal

Crea/actualiza el archivo `Documentacion/Semana6.md`:

```markdown
# Semana 6: Regresión Lineal Múltiple

## Fecha: [DD/MM/AAAA]

## Actividades Completadas
- [ ] Actividad 6.1: Regresión Múltiple Básica
- [ ] Actividad 6.2: Supuestos de Regresión
- [ ] Actividad 6.3: Selección de Variables
- [ ] Actividad 6.4: Regularización

## Resultados del Modelo
- [Documenta los resultados de tu modelo]

## Dudas o Bloqueos
- [Si tienes alguna duda]

## Commits Realizados
- Listar los commits de esta semana
```

**Git:**
```bash
git add Documentacion/Semana6.md
git commit -m "Semana6: Documentación actualizada"
git push
```

---

## Actualizar README

```bash
git add README.md
git commit -m "Update README: Semana 6 completada"
git push
```

---

## Recursos Adicionales

- Sklearn Ridge/Lasso: https://scikit-learn.org/stable/modules/linear_model.html
- Regularization Tutorial: https://www.analyticsvidhya.com/blog/2016/01/ridge-lasso-regression-python-visualization/

---

## Recordatorio

La Actividad 5 tiene una ponderación del 6% y cubre los Temas 13, 14 y 15 del temario.

---

## 📋 Consolidado Semanal: Semana 6

Al finalizar todas las actividades de esta semana, debes crear un archivo consolidado llamado `Semana6_Consolidado.md` que contenga:

### Estructura del consolidado:

```markdown
# Semana 6: Regresión Lineal Múltiple

## 1. Ejercicios Complementarios

### Ejercicio 1: [Nombre]
**Solución:**
[Tu respuesta/solución]

### Ejercicio 2: [Nombre]
**Solución:**
[Tu respuesta/solución]

## 2. Actividades Prácticas

### Actividad 6.1: [Nombre]
**Entregable:** [Descripción]

### Actividad 6.4: [Nombre]
**Entregable:** [Descripción]

## 3. Resultados del Modelo

- Variables seleccionadas: [Lista]
- R² ajustado: [Valor]
- Regularización aplicada: [Ridge/Lasso/None]
- Alpha óptimo: [Valor]

## 4. Resumen de Aprendizaje

- [Aprendizaje 1]
- [Aprendizaje 2]
- [Aprendizaje 3]

## 5. Dudas o Preguntas

- [Pregunta 1]
- [Pregunta 2]

## 6. Referencias

- [Referencia 1]
- [Referencia 2]
```

### Instrucciones de entrega:
1. Completa todos los ejercicios y actividades
2. Organiza todo en el archivo consolidado
3. Guarda en `Semana6/Semana6_Consolidado.md`
4. Realiza el commit correspondiente:
   ```bash
   git add Semana6/
   git commit -m "Semana6: Consolidado completo"
   git push
   ```

---

## ✅ Actividad Evaluable: Actividad 5

**Fecha de entrega:** [Según calendario del curso]

**Ponderación:** 6%

**Temas evaluados:** T13, T14 y T15

**Instrucciones:**
1. Completa todos los ejercicios complementarios
2. Completa todas las actividades prácticas
3. Construye y evalúa tu modelo de regresión múltiple
4. Aplica regularización si es necesario
5. Verifica tu consolidado semanal
6. Entrega según las indicaciones del profesor

**Criterios de evaluación:**
- [ ] Completó los ejercicios complementarios
- [ ] Completó todas las actividades prácticas
- [ ] Modelo de regresión múltiple correctamente implementado
- [ ] Supuestos verificados
- [ ] Técnicas de regularización aplicadas
- [ ] El consolidado está organizado y completo
- [ ] Commits realizados correctamente en Git
