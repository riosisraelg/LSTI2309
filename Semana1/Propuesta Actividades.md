# Actividades Prácticas - Semana 1

## Preparación para: Actividad 1

**Temas cubiertos:** Fundamentos de Ciencia de Datos y Big Data

---

## IMPORTANTE: Ejercicios Complementarios

Antes de comenzar con las actividades prácticas, es **fundamental** completar los ejercicios del archivo [`Ejercicios Complementarios.md`](Ejercicios%20Complementarios.md).

### ¿Por qué realizar estos ejercicios?

Los ejercicios complementarios te proporcionan la base matemática y lógica necesaria para:

1. **Comprender los conceptos teóricos** de ciencia de datos y Big Data
2. **Realizar cálculos básicos** que se aplican en el análisis de datos
3. **Desarrollar pensamiento lógico** computacional necesario para la programación
4. **Manejar escalas y volúmenes** de datos Big Data

> **Justificación:** Estos conocimientos son prerrequisitos básicos que facilitan la comprensión de los temas de esta semana. Sin esta base, será más difícil completar las actividades prácticas de manera efectiva.

**Tiempo estimado:** 1-2 horas

---

## Objetivo

Estas actividades prácticas te prepararán para completar la Actividad 1, enfocándose en los fundamentos teóricos de ciencia de datos y conceptos de Big Data.

---

## Estructura del Repositorio

Primero, crea la siguiente estructura de carpetas en tu computadora:

```
CienciaDeDatos/
├── README.md
├── Semana1/
│   └── Actividades/
├── Semana2/
│   └── Actividades/
├── Semana3/
│   ├── Actividades/
│   └── Proyecto/
├── Semana4/
│   └── Actividades/
├── Semana5/
│   └── Actividades/
├── Semana6/
│   └── Actividades/
├── Semana7/
│   ├── Actividades/
│   └── ProyectoFinal/
└── Documentacion/
    ├── Semana1.md
    ├── Semana2.md
    └── ...
```

---

## GIT: Comandos Básicos

### Configuración Inicial (solo una vez)
```bash
# Configurar tu nombre
git config --global user.name "Tu Nombre"

# Configurar tu email
git config --global user.email "tu@email.com"

# Verificar configuración
git config --list
```

### Flujo de Trabajo Regular
```bash
# 1. Ver estado del repositorio
git status

# 2. Agregar archivos modificados
git add .

# 3. Crear commit con mensaje
git commit -m "Mensaje descriptivo de los cambios"

# 4. Subir cambios al repositorio remoto
git push origin main

# 5. Actualizar repositorio local con cambios remotos
git pull origin main
```

### Comandos Adicionales
```bash
# Ver historial de commits
git log --oneline

# Ver diferencias
git diff

# Crear nueva rama
git checkout -b nombre-rama

# Cambiar de rama
git checkout nombre-rama
```

---

## Actividades Propuestas

### Actividad 1.0: Configuracion de Git y Repositorio (NUEVA)

**Descripción:** Crea tu repositorio local y conéctalo a GitHub.

**Instrucciones:**

1. **Crea una cuenta en GitHub** (si no tienes una)
   - Ve a https://github.com
   - Crea una cuenta gratuita

2. **Crea un nuevo repositorio en GitHub**
   - Click en "New repository"
   - Nombre: `CienciaDeDatos`
   - Descripción: "Actividades del curso de Ciencia de Datos"
   - Selecciona "Public"
   - No inicialices con README (lo harás localmente)

3. **Crea la estructura de carpetas localmente** (según la estructura mostrada arriba)

4. **Inicializa Git en tu proyecto:**
   ```bash
   cd CienciaDeDatos
   git init
   ```

5. **Crea el README.md inicial:**
   ```markdown
   # Curso de Ciencia de Datos

   Este repositorio contiene las actividades del curso de Ciencia de Datos.

   ## Progreso

   - [ ] Semana 1: Fundamentos y Big Data
   - [ ] Semana 2: Arquitecturas y MongoDB
   - [ ] Semana 3: Python y Análisis Exploratorio
   - [ ] Semana 4: Preparación de Datos
   - [ ] Semana 5: Regresión Lineal Simple
   - [ ] Semana 6: Regresión Lineal Múltiple
   - [ ] Semana 7: Regresión Logística y Comunicación
   ```

6. **Conecta tu repositorio local con GitHub:**
   ```bash
   git remote add origin https://github.com/TU_USUARIO/CienciaDeDatos.git
   ```

7. **Sube los cambios:**
   ```bash
   git add .
   git commit -m "Initial commit: Estructura inicial del repositorio"
   git push -u origin main
   ```

**Entregable:** 
- Repositorio creado en GitHub
- Estructura de carpetas local
- Primer commit realizado

---

### Actividad 1.1: Investigación de Conceptos Fundamentales

**Descripción:** Investiga y resume los conceptos básicos de la ciencia de datos.

**Instrucciones:**
1. Define qué es la ciencia de datos y menciona sus componentes principales
2. Explica la diferencia entre datos estructurados y no estructurados
3. Investiga qué son las 5 V del Big Data y da un ejemplo de cada una
4. Crea un mapa conceptual con los diferentes perfiles profesionales en ciencia de datos

**Carpeta de entrega:** `Semana1/Actividades/Actividad1.1/`

**Git:**
```bash
git add Semana1/Actividades/Actividad1.1/
git commit -m "Semana1: Actividad 1.1 - Conceptos fundamentales"
git push
```

---

### Actividad 1.2: Análisis de Casos de Uso

**Descripción:** Analiza casos reales de aplicación de ciencia de datos.

**Instrucciones:**
1. Investiga 3 empresas que utilizan ciencia de datos (ej: Netflix, Amazon, Spotify)
aws
amazon
google con youtube
2. Para cada empresa, identifica:
   - Qué tipo de datos recopilan
      - aws: en el servico de ec2 recopila los eventos de modificcion de configuracion, accesos por los puertos avilitados y las horas de uso para el cobro. tambien recopila datos de monitoreo del equipo virtualizad uso de recursos del hardware.
      - amazon: registra las ventas del servicio que pagues o compres, tambien los cometarios
      - youtube: recopila el historial de videos vistos
   - Qué técnicas de análisis utilizan
      - aws: sreaming para los recursos y visuaizacion en graficas y dashboard, los datos de uso del ec2 es a traves de batches
      - amazon utiiza batches que ba usando para modelar algoritmos y modelos predicivos
      - youtube: entrena modelos predicivios persoanlizados para recomendacion de videos a cada usario en particular en su seccion de home y despues de ver un video....
   - Qué problemas resuelven con los datos
      - aws: el cobro automatico del servicio. monitoreo de los recursos.
      - amazon: impulsa ventas recomendads de productos propios o de afiliados aumentando la confiazna del cliente.
      - Aumentan cantidad de retencion de tiempo de los usarios en la plataforma y fomentan el interes del mismo para utiilzar el sistema para informarse al tener contenido sugerido personalizado a sus gustos.
3. Crea una presentación breve resumiendo tus hallazgos

**Carpeta de entrega:** `Semana1/Actividades/Actividad1.2/`

**Git:**
```bash
git add Semana1/Actividades/Actividad1.2/
git commit -m "Semana1: Actividad 1.2 - Casos de uso"
git push
```

---

### Actividad 1.3: Configuración del Entorno de Trabajo

**Descripción:** Prepara tu entorno de trabajo para el curso.

**Instrucciones:**
1. Instala Python (si no lo tienes)
2. Instala las librerías principales:
   - NumPy
   - Pandas
   - Matplotlib
   - Seaborn
   - Scikit-learn
3. Verifica la instalación ejecutando un script básico
4. Crea un cuaderno Jupyter con un ejemplo de carga de datos

**Carpeta de entrega:** `Semana1/Actividades/Actividad1.3/`

**Git:**
```bash
git add Semana1/Actividades/Actividad1.3/
git commit -m "Semana1: Actividad 1.3 - Entorno de trabajo"
git push
```

---

### Actividad 1.4: Exploración de Fuentes de Datos

**Descripción:** Explora diferentes fuentes de datos disponibles.

**Instrucciones:**
1. Investiga qué es Kaggle y cómo puedes usarlo
2. Explora al menos 3 datasets públicos en Kaggle
3. Identifica qué tipo de datos contiene cada uno
4. Elige un dataset que te interese y describe:
   - Qué información contiene
   - Qué preguntas podrías responder con esos datos

**Carpeta de entrega:** `Semana1/Actividades/Actividad1.4/`

**Git:**
```bash
git add Semana1/Actividades/Actividad1.4/
git commit -m "Semana1: Actividad 1.4 - Fuentes de datos"
git push
```

---

## Actualizar Documentación Semanal

**Después de completar las actividades, actualiza tu documentación:**

Crea/actualiza el archivo `Documentacion/Semana1.md`:

```markdown
# Semana 1: Fundamentos de Ciencia de Datos y Big Data

## Fecha: [DD/MM/AAAA]

## Actividades Completadas
- [x] Actividad 1.0: Configuración de Git y Repositorio
- [x] Actividad 1.1: Conceptos Fundamentales
- [x] Actividad 1.2: Casos de Uso
- [x] Actividad 1.3: Entorno de Trabajo
- [x] Actividad 1.4: Fuentes de Datos

## Aprendido
- [Puntos clave aprendidos]

## Dudas o Bloqueos
- [Si tienes alguna duda, documentala aqui]

## Commits Realizados
- Initial commit: Estructura inicial
- Semana1: Actividad 1.1 - Conceptos fundamentales
- Semana1: Actividad 1.2 - Casos de uso
- Semana1: Actividad 1.3 - Entorno de trabajo
- Semana1: Actividad 1.4 - Fuentes de datos
```

**Git:**
```bash
git add Documentacion/Semana1.md README.md
git commit -m "Semana1: Documentacion actualizada"
git push
```

---

## Recursos Adicionales

- Tutorial de instalación de Python: https://www.python.org/
- GitHub: https://github.com/
- Kaggle: https://www.kaggle.com/
- Documentación de Pandas: https://pandas.pydata.org/
- Guía de Git: https://docs.github.com/es/get-started/using-git/about-git

---

## Recordatorio

La Actividad 1 tiene una ponderación del 6% y cubre los Temas 1 y 2 del temario.

---

## 📋 Consolidado Semanal: Semana 1

Al finalizar todas las actividades de esta semana, debes crear un archivo consolidado llamado `Semana1_Consolidado.md` que contenga:

### Estructura del consolidado:

```markdown
# Semana 1: Fundamentos de Ciencia de Datos y Big Data

## 1. Ejercicios Complementarios

### Ejercicio 1: [Nombre]
**Solución:**
[Tu respuesta/solución]

### Ejercicio 2: [Nombre]
**Solución:**
[Tu respuesta/solución]

## 2. Actividades Prácticas

### Actividad 1.1: [Nombre]
**Entregable:** [Descripción]

### Actividad 1.2: [Nombre]
**Entregable:** [Descripción]

## 3. Resumen de Aprendizaje

- [Aprendizaje 1]
- [Aprendizaje 2]
- [Aprendizaje 3]

## 4. Dudas o Preguntas

- [Pregunta 1]
- [Pregunta 2]

## 5. Referencias

- [Referencia 1]
- [Referencia 2]
```

### Instrucciones de entrega:
1. Completa todos los ejercicios y actividades
2. Organiza todo en el archivo consolidado
3. Guarda en `Semana1/Semana1_Consolidado.md`
4. Realiza el commit correspondiente:
   ```bash
   git add Semana1/
   git commit -m "Semana1: Consolidado completo"
   git push
   ```

---

## ✅ Actividad Evaluable: Actividad 1

**Fecha de entrega:** [Según calendario del curso]

**Ponderación:** 6%

**Temas evaluados:** T1 y T2

**Instrucciones:**
1. Completa todos los ejercicios complementarios
2. Completa todas las actividades prácticas
3. Verifica tu consolidado semanal
4. Entrega según las indicaciones del profesor

**Criterios de evaluación:**
- [ ] Completó los ejercicios complementarios
- [ ] Completó todas las actividades prácticas
- [ ] El consolidado está organizado y completo
- [ ] Commits realizados correctamente en Git
