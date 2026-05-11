# 📊 Visualizaciones del Proyecto Final

Esta carpeta contiene todas las visualizaciones generadas durante el análisis del proyecto.

## 📁 Estructura de Carpetas

Las visualizaciones están organizadas por archivo fuente:

```
Visualizaciones/
├── proyectoFinal/          # Visualizaciones del notebook principal
│   ├── 01_valores_faltantes.png
│   ├── 02_outliers_boxplots.png
│   ├── 03_mapa_calor_completo.png
│   ├── 04_correlaciones_log_price.png
│   ├── 05_analisis_vif.png
│   ├── 06_correlacion_matriz.png
│   ├── 07_pairplot.png
│   ├── 08_predicciones_vs_reales.png
│   ├── 09_importancia_caracteristicas.png
│   ├── 10_analisis_residuos.png
│   └── 11_qq_plot.png
│
├── modelo_v2/              # Visualizaciones del modelo mejorado (si existe)
│   └── ...
│
└── README.md               # Este archivo
```

## 🎨 Convención de Nombres

Los archivos siguen la convención:
- **Prefijo numérico**: Indica el orden de generación (01, 02, 03...)
- **Nombre descriptivo**: Describe el contenido del gráfico
- **Extensión**: `.png` con alta resolución (300 DPI)

## 📋 Catálogo de Visualizaciones

### 1. Limpieza de Datos
- `01_valores_faltantes.png` - Análisis de valores faltantes por columna
- `02_outliers_boxplots.png` - Detección de outliers con boxplots

### 2. Análisis de Correlación
- `03_mapa_calor_completo.png` - Mapa de calor de todas las variables numéricas
- `04_correlaciones_log_price.png` - Correlaciones con la variable objetivo

### 3. Análisis de Multicolinealidad
- `05_analisis_vif.png` - Factor de Inflación de la Varianza (VIF)

### 4. Análisis Exploratorio
- `06_correlacion_matriz.png` - Matriz de correlación entre variables seleccionadas
- `07_pairplot.png` - Relaciones entre variables principales

### 5. Evaluación del Modelo
- `08_predicciones_vs_reales.png` - Comparación de predicciones vs valores reales
- `09_importancia_caracteristicas.png` - Coeficientes del modelo
- `10_analisis_residuos.png` - Análisis de residuos (4 gráficos)
- `11_qq_plot.png` - Test de normalidad de residuos

## 🔧 Configuración

Todas las visualizaciones se generan con:
- **Resolución**: 300 DPI (calidad de impresión)
- **Formato**: PNG con transparencia
- **Estilo**: seaborn-v0_8-darkgrid
- **Paleta de colores**: husl

## 📝 Notas

- Las visualizaciones se generan automáticamente al ejecutar los notebooks
- Cada notebook crea su propia subcarpeta
- Los archivos se sobrescriben si se ejecuta el notebook nuevamente
- Todas las rutas son relativas al directorio del proyecto

## 🚀 Uso en el Código

Para guardar un gráfico en el notebook:

```python
# El gráfico actual se guarda automáticamente
guardar_grafico('nombre_archivo.png')
plt.show()
```

La función `guardar_grafico()` se encarga de:
1. Crear la carpeta si no existe
2. Guardar con alta resolución (300 DPI)
3. Ajustar márgenes automáticamente
4. Mostrar mensaje de confirmación

---

**Última actualización:** Mayo 2026  
**Proyecto:** Análisis Predictivo del Mercado Inmobiliario  
**Curso:** QR.LSTI2309TEO - Universidad Tecmilenio
