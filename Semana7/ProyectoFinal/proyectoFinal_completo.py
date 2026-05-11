#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PROYECTO FINAL - CIENCIA DE DATOS
Análisis Predictivo del Mercado Inmobiliario

Curso: QR.LSTI2309TEO — Universidad Tecmilenio
Ponderación: 35%
Temas: Regresión Lineal Múltiple y Comunicación de Datos

Este script contiene TODO el análisis realizado hasta ahora:
- Secciones 1.1 a 1.13 (Limpieza y análisis exploratorio)
"""


# ============================================
# IMPORTACIÓN DE LIBRERÍAS
# ============================================

# Manipulación de datos
import pandas as pd
import numpy as np

# Visualización
import matplotlib.pyplot as plt
import seaborn as sns

# Machine Learning
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# Análisis estadístico
from statsmodels.stats.outliers_influence import variance_inflation_factor
from scipy import stats

# Sistema de archivos
import os
from pathlib import Path

# Configuración
import warnings
warnings.filterwarnings('ignore')

# Configuración de visualización
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

# Mostrar todas las columnas en pandas
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 100)
pd.set_option('display.width', None)

# ============================================
# CONFIGURACIÓN DE CARPETAS PARA VISUALIZACIONES
# ============================================

# Nombre del archivo (sin extensión) para organizar visualizaciones
NOMBRE_PROYECTO = 'proyectoFinal'

# Crear estructura de carpetas
BASE_VIZ = Path('Visualizaciones')
CARPETA_VIZ = BASE_VIZ / NOMBRE_PROYECTO
CARPETA_VIZ.mkdir(parents=True, exist_ok=True)

def guardar_grafico(nombre_archivo, dpi=300):
    """Guarda el gráfico actual en la carpeta de visualizaciones"""
    ruta = CARPETA_VIZ / nombre_archivo
    plt.savefig(ruta, dpi=dpi, bbox_inches='tight')
    print(f"   💾 Guardado: {ruta}")

print("✅ Librerías importadas exitosamente")
print(f"📊 Pandas version: {pd.__version__}")
print(f"🔢 NumPy version: {np.__version__}")
print(f"\n📁 Carpeta de visualizaciones: {CARPETA_VIZ}")

# ============================================
# 1.1 CARGA DE DATOS
# ============================================

print("="*70)
print("📂 CARGANDO DATOS")
print("="*70)

# Cargar dataset
df = pd.read_csv('Datos/train.csv')

print(f"\n✅ Datos cargados exitosamente")
print(f"   Dimensiones: {df.shape[0]} filas × {df.shape[1]} columnas")
print(f"   Memoria utilizada: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")

# ============================================
# 1.2 EXPLORACIÓN INICIAL
# ============================================

print("="*70)
print("🔍 EXPLORACIÓN INICIAL DE DATOS")
print("="*70)

# Primeras filas
print("\n📋 Primeras 5 filas del dataset:")
display(df.head())

# Información general
print("\n📊 Información general del dataset:")
df.info()

# ============================================
# 1.3 ANÁLISIS DE TIPOS DE DATOS
# ============================================

print("="*70)
print("📊 ANÁLISIS DE TIPOS DE DATOS")
print("="*70)

# Crear DataFrame con información de columnas
info_columnas = pd.DataFrame({
    'Columna': df.columns,
    'Tipo': df.dtypes.values,
    'No_Nulos': df.count().values,
    'Nulos': df.isnull().sum().values,
    '%_Nulos': (df.isnull().sum() / len(df) * 100).round(2).values,
    'Valores_Únicos': [df[col].nunique() for col in df.columns]
})

print("\n📋 Resumen de todas las columnas:")
display(info_columnas)

# Estadísticas por tipo
print("\n📊 Distribución de tipos de datos:")
print(df.dtypes.value_counts())

# ============================================
# 1.4 IDENTIFICACIÓN DE VARIABLES NUMÉRICAS
# ============================================

print("="*70)
print("🔢 VARIABLES NUMÉRICAS")
print("="*70)

# Identificar columnas numéricas
columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()

print(f"\n✅ Total de variables numéricas: {len(columnas_numericas)}")
print("\n📋 Lista de variables numéricas:")
for i, col in enumerate(columnas_numericas, 1):
    print(f"   {i:2d}. {col:<30} (tipo: {df[col].dtype})")

# Estadísticas descriptivas
print("\n📊 Estadísticas descriptivas de variables numéricas:")
display(df[columnas_numericas].describe().T)

# ============================================
# 1.5 IDENTIFICACIÓN DE VARIABLES CATEGÓRICAS
# ============================================

print("="*70)
print("📝 VARIABLES CATEGÓRICAS")
print("="*70)

# Identificar columnas categóricas
columnas_categoricas = df.select_dtypes(include=['object']).columns.tolist()

print(f"\n✅ Total de variables categóricas: {len(columnas_categoricas)}")
print("\n📋 Lista de variables categóricas:")
for i, col in enumerate(columnas_categoricas, 1):
    n_unique = df[col].nunique()
    print(f"   {i:2d}. {col:<30} ({n_unique} valores únicos)")

# Análisis detallado de cada variable categórica
print("\n📊 Análisis detallado de variables categóricas:")
for col in columnas_categoricas:
    print(f"\n{'='*70}")
    print(f"Variable: {col}")
    print(f"{'='*70}")
    print(f"Valores únicos: {df[col].nunique()}")
    print(f"Valores nulos: {df[col].isnull().sum()} ({df[col].isnull().sum()/len(df)*100:.2f}%)")
    
    # Mostrar distribución si tiene pocos valores únicos
    if df[col].nunique() <= 20:
        print("\nDistribución de valores:")
        print(df[col].value_counts())
    else:
        print("\nTop 10 valores más frecuentes:")
        print(df[col].value_counts().head(10))

# ============================================
# 1.6 ANÁLISIS DE VALORES FALTANTES
# ============================================

print("="*70)
print("🔍 ANÁLISIS DE VALORES FALTANTES")
print("="*70)

# Calcular valores faltantes
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(2)
missing_df = pd.DataFrame({
    'Columna': missing.index,
    'Valores_Faltantes': missing.values,
    'Porcentaje': missing_pct.values
})
missing_df = missing_df[missing_df['Valores_Faltantes'] > 0].sort_values(
    'Valores_Faltantes', ascending=False
)

if len(missing_df) > 0:
    print(f"\n⚠️  Columnas con valores faltantes: {len(missing_df)}")
    display(missing_df)
    
    # Visualización
    plt.figure(figsize=(12, 6))
    plt.barh(missing_df['Columna'], missing_df['Porcentaje'])
    plt.xlabel('Porcentaje de Valores Faltantes (%)')
    plt.title('Valores Faltantes por Columna')
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    guardar_grafico('01_valores_faltantes.png')
    plt.show()
else:
    print("\n✅ No hay valores faltantes en el dataset")

# ============================================
# 1.7 IMPUTACIÓN DE VALORES FALTANTES
# ============================================

print("="*70)
print("🔧 IMPUTACIÓN DE VALORES FALTANTES")
print("="*70)

for col in columnas_imputar_numericas:
    if col in df_limpio_limpio.columns:
        mediana = df_limpio_limpio[col].median()
        # Asignación directa en lugar de inplace=True
        df_limpio_limpio[col] = df_limpio_limpio[col].fillna(mediana)

# Validar nuevamente
print(df_limpio_limpio[columnas_imputar_numericas].isnull().sum())
df_limpio = df_limpio_limpio.copy() 

# ============================================
# 1.8 ELIMINACIÓN DE COLUMNAS IRRELEVANTES
# ============================================

print("="*70)
print("🗑️  ELIMINACIÓN DE COLUMNAS IRRELEVANTES")
print("="*70)

# Columnas a eliminar (lista exacta proporcionada)
columnas_eliminar = [
    'id',
    'first_review',
    'host_has_profile_pic',
    'host_identity_verified',
    'host_response_rate',
    'host_since',
    'instant_bookable',
    'last_review',
    'name',
    'neighbourhood',
    'thumbnail_url',
    'zipcode',
    'cancellation_policy',
    'description'
]

# Verificar cuáles existen en el dataset
columnas_eliminar_existentes = [col for col in columnas_eliminar if col in df_limpio.columns]

print(f"\n📋 Número de columnas a eliminar: {len(columnas_eliminar_existentes)}")

# Eliminar columnas
if columnas_eliminar_existentes:
    df_limpio = df_limpio.drop(columns=columnas_eliminar_existentes)
    print(f"✅ Eliminadas {len(columnas_eliminar_existentes)} columnas")
else:
    print("✅ No hay columnas para eliminar")

print(f"\n📊 Dimensiones después de eliminación: {df_limpio.shape}")

# ============================================
# 1.9 DETECCIÓN DE OUTLIERS
# ============================================

print("="*70)
print("📊 DETECCIÓN DE OUTLIERS (MÉTODO IQR)")
print("="*70)

def detectar_outliers_iqr(data, columna, factor=1.5):
    """Detecta outliers usando el método IQR"""
    Q1 = data[columna].quantile(0.25)
    Q3 = data[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - factor * IQR
    limite_superior = Q3 + factor * IQR
    
    outliers = data[(data[columna] < limite_inferior) | (data[columna] > limite_superior)]
    
    return len(outliers), limite_inferior, limite_superior

# Analizar outliers en variables numéricas clave
variables_analizar = ['log_price', 'accommodates', 'bedrooms', 'beds', 'bathrooms']
variables_analizar = [col for col in variables_analizar if col in df_limpio.columns]

outliers_info = []
for col in variables_analizar:
    n_outliers, lim_inf, lim_sup = detectar_outliers_iqr(df_limpio, col)
    outliers_info.append({
        'Variable': col,
        'N_Outliers': n_outliers,
        'Porcentaje': f"{n_outliers/len(df_limpio)*100:.2f}%",
        'Límite_Inferior': f"{lim_inf:.2f}",
        'Límite_Superior': f"{lim_sup:.2f}"
    })

outliers_df = pd.DataFrame(outliers_info)
print("\n📊 Resumen de outliers:")
display(outliers_df)

# Visualización de boxplots
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, col in enumerate(variables_analizar):
    if i < len(axes):
        axes[i].boxplot(df_limpio[col].dropna())
        axes[i].set_title(f'Boxplot: {col}')
        axes[i].set_ylabel('Valor')
        axes[i].grid(True, alpha=0.3)

# Ocultar ejes no utilizados
for i in range(len(variables_analizar), len(axes)):
    axes[i].axis('off')

plt.tight_layout()
guardar_grafico('02_outliers_boxplots.png')
plt.show()

print("\n✅ Análisis de outliers completado")
print("💡 Nota: Los outliers se mantienen por ahora para análisis posterior")

# ====================================================================
# ============================================
# 1.9.1 ELIMINACIÓN DE OUTLIERS
# ============================================

print("="*70)
print("🗑️  ELIMINACIÓN DE OUTLIERS (MÉTODO IQR)")
print("="*70)

def eliminar_outliers_iqr(data, columna, factor=1.5):
    """Elimina outliers usando el método IQR"""
    Q1 = data[columna].quantile(0.25)
    Q3 = data[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - factor * IQR
    limite_superior = Q3 + factor * IQR
    
    # Contar outliers antes de eliminar
    outliers_antes = len(data[(data[columna] < limite_inferior) | (data[columna] > limite_superior)])
    
    # Filtrar datos sin outliers
    data_filtrado = data[(data[columna] >= limite_inferior) & (data[columna] <= limite_superior)]
    
    return data_filtrado, outliers_antes, limite_inferior, limite_superior

# Variables a limpiar de outliers
variables_limpiar = ['beds', 'accommodates', 'log_price']

print(f"\n📊 Dimensiones antes de eliminar outliers: {df_limpio.shape}")
print(f"   Filas: {df_limpio.shape[0]:,}")

# Eliminar outliers de cada variable
for col in variables_limpiar:
    if col in df_limpio.columns:
        filas_antes = len(df_limpio)
        df_limpio, n_outliers, lim_inf, lim_sup = eliminar_outliers_iqr(df_limpio, col)
        filas_despues = len(df_limpio)
        eliminadas = filas_antes - filas_despues
        
        print(f"\n✅ {col}:")
        print(f"   Outliers detectados: {n_outliers}")
        print(f"   Filas eliminadas: {eliminadas}")
        print(f"   Límite inferior: {lim_inf:.2f}")
        print(f"   Límite superior: {lim_sup:.2f}")
        print(f"   Filas restantes: {filas_despues:,}")

print(f"\n📊 Dimensiones después de eliminar outliers: {df_limpio.shape}")
print(f"   Filas: {df_limpio.shape[0]:,}")
print(f"   Columnas: {df_limpio.shape[1]}")

filas_eliminadas_total = df.shape[0] - df_limpio.shape[0]
porcentaje_eliminado = (filas_eliminadas_total / df.shape[0]) * 100

print(f"\n📉 Total de filas eliminadas: {filas_eliminadas_total:,} ({porcentaje_eliminado:.2f}%)")
print(f"✅ Limpieza de outliers completada")

# ============================================
# 1.10 RESUMEN DE LIMPIEZA
# ============================================

print("="*70)
print("📋 RESUMEN DE LIMPIEZA DE DATOS")
print("="*70)

print(f"\n📊 Dataset Original:")
print(f"   Filas: {df.shape[0]:,}")
print(f"   Columnas: {df.shape[1]}")
print(f"   Valores faltantes: {df.isnull().sum().sum():,}")

print(f"\n📊 Dataset Limpio:")
print(f"   Filas: {df_limpio.shape[0]:,}")
print(f"   Columnas: {df_limpio.shape[1]}")
print(f"   Valores faltantes: {df_limpio.isnull().sum().sum():,}")

print(f"\n✅ Limpieza completada exitosamente")

# ============================================
# 1.110 MAPA DE CALOR - TODAS LAS VARIABLES NUMÉRICAS
# ============================================

print("="*70)
print("🔥 MAPA DE CALOR - CORRELACIÓN DE VARIABLES NUMÉRICAS")
print("="*70)

# Seleccionar solo variables numéricas
df_numerico = df_limpio.select_dtypes(include=[np.number])

print(f"\n📊 Variables numéricas disponibles: {df_numerico.shape[1]}")
print("\n📋 Lista de variables numéricas:")
for i, col in enumerate(df_numerico.columns, 1):
    print(f"   {i:2d}. {col}")

# Calcular matriz de correlación
correlacion_matriz = df_numerico.corr()

# Crear mapa de calor
plt.figure(figsize=(14, 12))
sns.heatmap(
    correlacion_matriz,
    annot=True,
    fmt='.2f',
    cmap='RdBu_r',
    center=0,
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)
plt.title('Mapa de Calor - Correlación entre Variables Numéricas', fontsize=14, pad=20)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
guardar_grafico('03_mapa_calor_completo.png')
plt.show()

# Análisis de correlaciones con log_price
if 'log_price' in df_numerico.columns:
    print("\n📊 Correlaciones con log_price (variable objetivo):")
    correlaciones_precio = correlacion_matriz['log_price'].sort_values(ascending=False)
    
    print("\n🔝 Top 10 correlaciones positivas:")
    for i, (var, corr) in enumerate(correlaciones_precio.head(11).items(), 1):
        if var != 'log_price':  # Excluir la correlación consigo misma
            print(f"   {i:2d}. {var:<30} {corr:>7.4f}")
    
    print("\n🔻 Top 5 correlaciones negativas:")
    for i, (var, corr) in enumerate(correlaciones_precio.tail(5).items(), 1):
        print(f"   {i:2d}. {var:<30} {corr:>7.4f}")
    
    # Visualización de correlaciones con log_price
    plt.figure(figsize=(10, 8))
    correlaciones_precio_sorted = correlaciones_precio.drop('log_price').sort_values()
    colors = ['red' if x < 0 else 'green' for x in correlaciones_precio_sorted]
    plt.barh(range(len(correlaciones_precio_sorted)), correlaciones_precio_sorted, color=colors, alpha=0.7)
    plt.yticks(range(len(correlaciones_precio_sorted)), correlaciones_precio_sorted.index)
    plt.xlabel('Correlación con log_price')
    plt.title('Correlación de Variables Numéricas con log_price')
    plt.axvline(x=0, color='black', linestyle='--', linewidth=1)
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    guardar_grafico('04_correlaciones_log_price.png')
    plt.show()

# Identificar pares de variables altamente correlacionadas
print("\n⚠️  Pares de variables con alta correlación (|r| > 0.8):")
alta_correlacion = []
for i in range(len(correlacion_matriz.columns)):
    for j in range(i+1, len(correlacion_matriz.columns)):
        if abs(correlacion_matriz.iloc[i, j]) > 0.8:
            var1 = correlacion_matriz.columns[i]
            var2 = correlacion_matriz.columns[j]
            corr = correlacion_matriz.iloc[i, j]
            alta_correlacion.append((var1, var2, corr))

if alta_correlacion:
    for i, (var1, var2, corr) in enumerate(alta_correlacion, 1):
        print(f"   {i}. {var1} ↔ {var2}: {corr:.4f}")
    print("\n💡 Nota: Alta correlación entre variables puede indicar multicolinealidad")
else:
    print("   ✅ No se encontraron pares con correlación > 0.8")

print("\n✅ Análisis de correlación completado")

# ============================================
# 2.1 DEFINICIÓN DE VARIABLES
# ============================================

print("="*70)
print("🎯 IDENTIFICACIÓN DE VARIABLES")
print("="*70)

# Variable dependiente (target)
variable_dependiente = 'log_price'

print(f"\n🎯 VARIABLE DEPENDIENTE (Y):")
print(f"   {variable_dependiente}")
print(f"   Descripción: Logaritmo natural del precio de la propiedad")
print(f"   Tipo: {df_limpio[variable_dependiente].dtype}")
print(f"   Rango: [{df_limpio[variable_dependiente].min():.2f}, {df_limpio[variable_dependiente].max():.2f}]")
print(f"   Media: {df_limpio[variable_dependiente].mean():.2f}")
print(f"   Mediana: {df_limpio[variable_dependiente].median():.2f}")

# Variables independientes candidatas
print(f"\n📊 VARIABLES INDEPENDIENTES CANDIDATAS (X):")
print(f"\n🔢 Variables Numéricas:")
vars_numericas = df_limpio.select_dtypes(include=[np.number]).columns.tolist()
vars_numericas.remove(variable_dependiente)
for i, var in enumerate(vars_numericas, 1):
    print(f"   {i:2d}. {var}")

print(f"\n📝 Variables Categóricas:")
vars_categoricas = df_limpio.select_dtypes(include=['object']).columns.tolist()
for i, var in enumerate(vars_categoricas, 1):
    print(f"   {i:2d}. {var} ({df_limpio[var].nunique()} categorías)")

print(f"\n✅ Total de variables independientes: {len(vars_numericas) + len(vars_categoricas)}")

# ============================================
# 3.1 CÁLCULO DEL VIF (VARIANCE INFLATION FACTOR)
# ============================================

print("="*70)
print("📊 ANÁLISIS DE MULTICOLINEALIDAD (VIF)")
print("="*70)

print("\n💡 ¿Qué es el VIF?")
print("   El Factor de Inflación de la Varianza (VIF) mide cuánto aumenta")
print("   la varianza de un coeficiente debido a la correlación con otras variables.")
print("\n📏 Interpretación:")
print("   • VIF = 1      : No hay correlación")
print("   • VIF < 5      : Multicolinealidad aceptable")
print("   • VIF 5-10     : Multicolinealidad moderada (considerar eliminar)")
print("   • VIF > 10     : Multicolinealidad alta (eliminar variable)")

# Seleccionar solo variables numéricas (excluyendo log_price)
vars_para_vif = [col for col in vars_numericas if col in df_limpio.columns]

if len(vars_para_vif) > 0:
    print(f"\n📊 Calculando VIF para {len(vars_para_vif)} variables numéricas...")
    
    # Preparar datos (eliminar nulos)
    df_vif = df_limpio[vars_para_vif].dropna()
    
    # Calcular VIF para cada variable
    vif_data = pd.DataFrame()
    vif_data["Variable"] = df_vif.columns
    vif_data["VIF"] = [variance_inflation_factor(df_vif.values, i) 
                       for i in range(len(df_vif.columns))]
    
    # Ordenar por VIF descendente
    vif_data = vif_data.sort_values('VIF', ascending=False).reset_index(drop=True)
    
    # Agregar interpretación
    def interpretar_vif(vif):
        if vif < 5:
            return '✅ Aceptable'
        elif vif < 10:
            return '⚠️  Moderada'
        else:
            return '❌ Alta'
    
    vif_data['Interpretación'] = vif_data['VIF'].apply(interpretar_vif)
    
    # Mostrar resultados
    print("\n📋 Resultados del análisis VIF:")
    print("="*70)
    display(vif_data)
    
    # Resumen por categoría
    print("\n📊 Resumen:")
    aceptable = len(vif_data[vif_data['VIF'] < 5])
    moderada = len(vif_data[(vif_data['VIF'] >= 5) & (vif_data['VIF'] < 10)])
    alta = len(vif_data[vif_data['VIF'] >= 10])
    
    print(f"   ✅ Multicolinealidad aceptable (VIF < 5):    {aceptable} variables")
    print(f"   ⚠️  Multicolinealidad moderada (VIF 5-10):   {moderada} variables")
    print(f"   ❌ Multicolinealidad alta (VIF > 10):        {alta} variables")
    
    # Identificar variables problemáticas
    if alta > 0:
        print("\n⚠️  ADVERTENCIA: Variables con multicolinealidad alta:")
        vars_problematicas = vif_data[vif_data['VIF'] >= 10]
        for idx, row in vars_problematicas.iterrows():
            print(f"   • {row['Variable']}: VIF = {row['VIF']:.2f}")
        print("\n💡 Recomendación: Considerar eliminar estas variables del modelo")
    elif moderada > 0:
        print("\n⚠️  Variables con multicolinealidad moderada:")
        vars_moderadas = vif_data[(vif_data['VIF'] >= 5) & (vif_data['VIF'] < 10)]
        for idx, row in vars_moderadas.iterrows():
            print(f"   • {row['Variable']}: VIF = {row['VIF']:.2f}")
        print("\n💡 Recomendación: Monitorear estas variables durante el modelado")
    else:
        print("\n✅ ¡Excelente! No hay problemas de multicolinealidad")
    
    # Visualización del VIF
    plt.figure(figsize=(12, 8))
    
    # Colores según nivel de VIF
    colors = ['green' if x < 5 else 'orange' if x < 10 else 'red' for x in vif_data['VIF']]
    
    plt.barh(vif_data['Variable'], vif_data['VIF'], color=colors, alpha=0.7)
    plt.xlabel('VIF (Factor de Inflación de la Varianza)', fontsize=12)
    plt.ylabel('Variables', fontsize=12)
    plt.title('Análisis de Multicolinealidad - VIF por Variable', fontsize=14, pad=20)
    
    # Líneas de referencia
    plt.axvline(x=5, color='orange', linestyle='--', linewidth=2, label='VIF = 5 (Moderado)')
    plt.axvline(x=10, color='red', linestyle='--', linewidth=2, label='VIF = 10 (Alto)')
    
    plt.legend(loc='lower right')
    plt.grid(True, alpha=0.3, axis='x')
    plt.tight_layout()
    guardar_grafico('05_analisis_vif.png')
    plt.show()
    
    # Análisis de pares correlacionados
    print("\n📊 Análisis de pares de variables altamente correlacionadas:")
    print("="*70)
    
    # Calcular correlaciones
    corr_matrix = df_vif.corr()
    
    # Encontrar pares con alta correlación
    pares_alta_corr = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            if abs(corr_matrix.iloc[i, j]) > 0.7:
                var1 = corr_matrix.columns[i]
                var2 = corr_matrix.columns[j]
                corr = corr_matrix.iloc[i, j]
                pares_alta_corr.append({
                    'Variable 1': var1,
                    'Variable 2': var2,
                    'Correlación': corr,
                    'Abs': abs(corr)
                })
    
    if pares_alta_corr:
        df_pares = pd.DataFrame(pares_alta_corr).sort_values('Abs', ascending=False)
        df_pares = df_pares.drop('Abs', axis=1)
        
        print(f"\n⚠️  Encontrados {len(df_pares)} pares con |correlación| > 0.7:")
        display(df_pares)
        
        print("\n💡 Interpretación:")
        print("   Estos pares de variables están altamente correlacionados.")
        print("   Considerar mantener solo una de cada par en el modelo final.")
    else:
        print("\n✅ No se encontraron pares con correlación > 0.7")
    
    print("\n✅ Análisis de multicolinealidad completado")
    
else:
    print("\n⚠️  No hay suficientes variables numéricas para calcular VIF")


# ============================================
# 3.2 MATRIZ DE CORRELACIÓN - acciones 
# ============================================
# ====================================================================
# ============================================
# 3.2 ELIMINACIÓN DE VARIABLES CON MULTICOLINEALIDAD CRÍTICA
# ============================================

print("="*70)
print("🗑️  ELIMINACIÓN DE VARIABLES CON MULTICOLINEALIDAD CRÍTICA")
print("="*70)

print("\n📋 JUSTIFICACIÓN TÉCNICA:")
print("="*70)

# Variable 1: beds
print("\n1️⃣  VARIABLE: beds")
print("   ❌ DECISIÓN: ELIMINAR")
print("   📊 VIF: 14.89 (crítico)")
print("   🔗 Correlación con accommodates: 0.76")
print("   💡 Justificación:")
print("      • Redundancia estructural con accommodates")
print("      • VIF en nivel crítico (>10)")
print("      • accommodates tiene mayor correlación con log_price (0.52)")

# Variable 2: review_scores_rating
print("\n2️⃣  VARIABLE: review_scores_rating")
print("   ❌ DECISIÓN: ELIMINAR")
print("   📊 VIF: 11.27 (crítico)")
print("   💡 Justificación:")
print("      • VIF excede severamente el límite de viabilidad (>10)")
print("      • Produce inestabilidad matemática en coeficientes")
print("      • Compromete la interpretabilidad del modelo")

# Variable 3: accommodates
print("\n3️⃣  VARIABLE: accommodates")
print("   ✅ DECISIÓN: RETENER")
print("   📊 Correlación con log_price: 0.52 (la más alta)")
print("   💡 Justificación:")
print("      • Predictor principal de capacidad del inmueble")
print("      • Mayor correlación lineal positiva con variable objetivo")
print("      • Representa mejor la capacidad real de la propiedad")

# Dimensiones antes de eliminar
print(f"\n📊 Dimensiones antes de eliminación:")
print(f"   Filas: {df_limpio.shape[0]:,}")
print(f"   Columnas: {df_limpio.shape[1]}")

# Eliminar variables con multicolinealidad crítica
variables_eliminar_vif = ['beds', 'review_scores_rating']
variables_existentes = [col for col in variables_eliminar_vif if col in df_limpio.columns]

if variables_existentes:
    print(f"\n🗑️  Eliminando {len(variables_existentes)} variables:")
    for var in variables_existentes:
        print(f"   • {var}")
    
    df_limpio = df_limpio.drop(columns=variables_existentes)
    print(f"\n✅ Variables eliminadas exitosamente")
else:
    print(f"\n⚠️  Ninguna de las variables especificadas existe en el dataset")

# Dimensiones después de eliminar
print(f"\n📊 Dimensiones después de eliminación:")
print(f"   Filas: {df_limpio.shape[0]:,}")
print(f"   Columnas: {df_limpio.shape[1]}")

# ====================================================================
# ============================================
# 3.3 RECÁLCULO DE VIF - SEGUNDA ITERACIÓN
# ============================================

print("\n" + "="*70)
print("🔄 RECÁLCULO DE VIF - SEGUNDA ITERACIÓN")
print("="*70)

print("\n💡 OBJETIVO:")
print("   Confirmar que la inflación de varianza se redujo a niveles")
print("   funcionales (VIF < 5) tras eliminar variables problemáticas")

# Identificar variables numéricas remanentes (excluyendo log_price)
vars_numericas_remanentes = df_limpio.select_dtypes(include=[np.number]).columns.tolist()
if 'log_price' in vars_numericas_remanentes:
    vars_numericas_remanentes.remove('log_price')

print(f"\n📊 Variables numéricas para análisis VIF: {len(vars_numericas_remanentes)}")
for i, var in enumerate(vars_numericas_remanentes, 1):
    print(f"   {i}. {var}")

if len(vars_numericas_remanentes) >= 2:
    # Preparar datos
    df_vif_v2 = df_limpio[vars_numericas_remanentes].dropna()
    
    # Calcular VIF
    vif_data_v2 = pd.DataFrame()
    vif_data_v2["Variable"] = df_vif_v2.columns
    vif_data_v2["VIF"] = [variance_inflation_factor(df_vif_v2.values, i) 
                          for i in range(len(df_vif_v2.columns))]
    
    # Ordenar por VIF
    vif_data_v2 = vif_data_v2.sort_values('VIF', ascending=False).reset_index(drop=True)
    
    # Interpretación
    def interpretar_vif_v2(vif):
        if vif < 5:
            return '✅ Funcional'
        elif vif < 10:
            return '⚠️  Moderado'
        else:
            return '❌ Crítico'
    
    vif_data_v2['Estado'] = vif_data_v2['VIF'].apply(interpretar_vif_v2)
    
    # Mostrar resultados
    print("\n📋 RESULTADOS - VIF SEGUNDA ITERACIÓN:")
    print("="*70)
    display(vif_data_v2)
    
    # Análisis de resultados
    funcional = len(vif_data_v2[vif_data_v2['VIF'] < 5])
    moderado = len(vif_data_v2[(vif_data_v2['VIF'] >= 5) & (vif_data_v2['VIF'] < 10)])
    critico = len(vif_data_v2[vif_data_v2['VIF'] >= 10])
    
    print("\n📊 RESUMEN:")
    print(f"   ✅ VIF funcional (< 5):     {funcional} variables")
    print(f"   ⚠️  VIF moderado (5-10):     {moderado} variables")
    print(f"   ❌ VIF crítico (> 10):       {critico} variables")
    
    # Verificación de éxito
    if critico == 0:
        print("\n🎉 ¡ÉXITO! Todas las variables tienen VIF funcional o moderado")
        print("   La multicolinealidad crítica ha sido eliminada")
    else:
        print("\n⚠️  ADVERTENCIA: Aún existen variables con VIF crítico")
        vars_criticas = vif_data_v2[vif_data_v2['VIF'] >= 10]
        for idx, row in vars_criticas.iterrows():
            print(f"   • {row['Variable']}: VIF = {row['VIF']:.2f}")
    
    # Visualización comparativa
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: VIF Segunda Iteración
    colors_v2 = ['green' if x < 5 else 'orange' if x < 10 else 'red' 
                 for x in vif_data_v2['VIF']]
    ax1.barh(vif_data_v2['Variable'], vif_data_v2['VIF'], color=colors_v2, alpha=0.7)
    ax1.axvline(x=5, color='orange', linestyle='--', linewidth=2, label='VIF = 5')
    ax1.axvline(x=10, color='red', linestyle='--', linewidth=2, label='VIF = 10')
    ax1.set_xlabel('VIF', fontsize=12)
    ax1.set_ylabel('Variables', fontsize=12)
    ax1.set_title('VIF - Segunda Iteración\n(Después de eliminar beds y review_scores_rating)', 
                  fontsize=12, pad=15)
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 2: Comparación (si existe vif_data de la primera iteración)
    if 'vif_data' in locals():
        # Filtrar solo variables que siguen en el dataset
        vif_data_comparacion = vif_data[vif_data['Variable'].isin(vars_numericas_remanentes)]
        
        # Crear comparación
        x = np.arange(len(vif_data_v2))
        width = 0.35
        
        # Buscar valores anteriores
        vif_antes = []
        for var in vif_data_v2['Variable']:
            if var in vif_data_comparacion['Variable'].values:
                vif_antes.append(
                    vif_data_comparacion[vif_data_comparacion['Variable'] == var]['VIF'].values[0]
                )
            else:
                vif_antes.append(0)
        
        ax2.barh(x - width/2, vif_antes, width, label='Antes', alpha=0.7, color='red')
        ax2.barh(x + width/2, vif_data_v2['VIF'], width, label='Después', alpha=0.7, color='green')
        ax2.set_yticks(x)
        ax2.set_yticklabels(vif_data_v2['Variable'])
        ax2.set_xlabel('VIF', fontsize=12)
        ax2.set_title('Comparación VIF\nAntes vs Después de Eliminación', fontsize=12, pad=15)
        ax2.legend()
        ax2.grid(True, alpha=0.3, axis='x')
        ax2.axvline(x=5, color='orange', linestyle='--', linewidth=1, alpha=0.5)
        ax2.axvline(x=10, color='red', linestyle='--', linewidth=1, alpha=0.5)
    else:
        ax2.text(0.5, 0.5, 'No hay datos de\niteración anterior\npara comparar', 
                ha='center', va='center', fontsize=14, transform=ax2.transAxes)
        ax2.axis('off')
    
    plt.tight_layout()
    guardar_grafico('06_vif_segunda_iteracion.png')
    plt.show()
    
    print("\n✅ Recálculo de VIF completado")
    
else:
    print("\n⚠️  No hay suficientes variables numéricas para calcular VIF")

# ====================================================================
# ============================================
# 3.4 PREPARACIÓN DE VARIABLES CATEGÓRICAS
# ============================================

print("\n" + "="*70)
print("🏷️  PREPARACIÓN DE VARIABLES CATEGÓRICAS")
print("="*70)

print("\n💡 ESTRATEGIA:")
print("   Incorporar variables categóricas de alta relevancia mediante")
print("   transformación a variables ficticias (dummy variables) para")
print("   compensar la pérdida de predictores numéricos")

# Identificar variable categórica principal
variable_categorica_principal = 'room_type'

if variable_categorica_principal in df_limpio.columns:
    print(f"\n📊 VARIABLE CATEGÓRICA SELECCIONADA: {variable_categorica_principal}")
    
    # Análisis de la variable
    print(f"\n📋 Análisis de {variable_categorica_principal}:")
    print(f"   Valores únicos: {df_limpio[variable_categorica_principal].nunique()}")
    print(f"   Valores nulos: {df_limpio[variable_categorica_principal].isnull().sum()}")
    
    print(f"\n📊 Distribución de valores:")
    distribucion = df_limpio[variable_categorica_principal].value_counts()
    for categoria, count in distribucion.items():
        porcentaje = (count / len(df_limpio)) * 100
        print(f"   • {categoria}: {count:,} ({porcentaje:.2f}%)")
    
    # Análisis de relación con log_price
    print(f"\n📈 Relación con log_price:")
    precio_por_categoria = df_limpio.groupby(variable_categorica_principal)['log_price'].agg([
        ('Media', 'mean'),
        ('Mediana', 'median'),
        ('Desv_Est', 'std'),
        ('Count', 'count')
    ]).round(2)
    display(precio_por_categoria)
    
    # Crear variables dummy
    print(f"\n🔄 Creando variables dummy para {variable_categorica_principal}...")
    df_limpio = pd.get_dummies(df_limpio, columns=[variable_categorica_principal], 
                                drop_first=True, dtype=int)
    
    # Identificar nuevas columnas creadas
    nuevas_columnas = [col for col in df_limpio.columns if col.startswith(f'{variable_categorica_principal}_')]
    
    print(f"\n✅ Variables dummy creadas: {len(nuevas_columnas)}")
    for i, col in enumerate(nuevas_columnas, 1):
        print(f"   {i}. {col}")
    
    # Visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # Gráfico 1: Distribución de categorías
    distribucion.plot(kind='barh', ax=ax1, color='steelblue', alpha=0.7)
    ax1.set_xlabel('Frecuencia', fontsize=12)
    ax1.set_ylabel('Categoría', fontsize=12)
    ax1.set_title(f'Distribución de {variable_categorica_principal}', fontsize=12, pad=15)
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Gráfico 2: Precio promedio por categoría
    precio_por_categoria['Media'].plot(kind='barh', ax=ax2, color='coral', alpha=0.7)
    ax2.set_xlabel('log_price (Media)', fontsize=12)
    ax2.set_ylabel('Categoría', fontsize=12)
    ax2.set_title(f'Precio Promedio por {variable_categorica_principal}', fontsize=12, pad=15)
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    guardar_grafico('07_analisis_room_type.png')
    plt.show()
    
    print(f"\n✅ Transformación de variables categóricas completada")
    
else:
    print(f"\n⚠️  La variable {variable_categorica_principal} no existe en el dataset")

# Resumen final
print("\n" + "="*70)
print("📋 RESUMEN DE TRANSFORMACIONES")
print("="*70)

print(f"\n📊 Dataset final:")
print(f"   Filas: {df_limpio.shape[0]:,}")
print(f"   Columnas: {df_limpio.shape[1]}")

print(f"\n🔢 Variables numéricas: {len(df_limpio.select_dtypes(include=[np.number]).columns)}")
print(f"📝 Variables categóricas originales eliminadas: 1 ({variable_categorica_principal})")
print(f"🏷️  Variables dummy creadas: {len(nuevas_columnas) if 'nuevas_columnas' in locals() else 0}")

print("\n✅ Preparación de datos para modelado completada")


# ====================================================================
# ============================================
# 4. ANÁLISIS DE CORRELACIÓN - PAIRPLOT
# ============================================

print("="*70)
print("📊 ANÁLISIS DE CORRELACIÓN - PAIRPLOT")
print("="*70)

print("\n💡 ESTRATEGIA DE VISUALIZACIÓN:")
print("="*70)
print("   ✅ Variables seleccionadas: Solo numéricas continuas/discretas")
print("   ✅ Exclusión de variables dummy: Evita saturación visual")
print("   ✅ Configuración corner=True: Elimina duplicación de información")
print("   ✅ Líneas de regresión (kind='reg'): Evalúa relaciones lineales")
print("   ✅ Transparencia (alpha): Maneja overplotting en datasets grandes")

# Seleccionar variables numéricas para el pairplot
# Excluir variables dummy (que empiezan con 'room_type_', 'property_type_', etc.)
variables_pairplot = ['log_price', 'accommodates', 'bathrooms', 'bedrooms', 'number_of_reviews']

# Verificar que todas las variables existen
variables_disponibles = [var for var in variables_pairplot if var in df_limpio.columns]

print(f"\n📋 Variables incluidas en el Pairplot: {len(variables_disponibles)}")
for i, var in enumerate(variables_disponibles, 1):
    print(f"   {i}. {var}")

if len(variables_disponibles) >= 2:
    # Crear subset de datos
    df_pairplot = df_limpio[variables_disponibles].copy()
    
    # Información del subset
    print(f"\n📊 Información del subset:")
    print(f"   Filas: {df_pairplot.shape[0]:,}")
    print(f"   Columnas: {df_pairplot.shape[1]}")
    print(f"   Valores nulos: {df_pairplot.isnull().sum().sum()}")
    
    # Eliminar valores nulos si existen
    if df_pairplot.isnull().sum().sum() > 0:
        filas_antes = len(df_pairplot)
        df_pairplot = df_pairplot.dropna()
        filas_despues = len(df_pairplot)
        print(f"   ⚠️  Eliminadas {filas_antes - filas_despues:,} filas con valores nulos")
    
    # Estadísticas descriptivas del subset
    print(f"\n📊 Estadísticas descriptivas:")
    display(df_pairplot.describe().T)
    
    # Generar Pairplot
    print(f"\n🎨 Generando Pairplot...")
    print(f"   ⏳ Esto puede tomar varios segundos debido al tamaño del dataset...")
    
    # Configuración del pairplot
    sns.set_style("whitegrid")
    
    pairplot = sns.pairplot(
        df_pairplot,
        kind='reg',              # Incluye líneas de regresión
        diag_kind='hist',        # Histogramas en la diagonal
        corner=True,             # Solo muestra el triángulo inferior
        plot_kws={
            'scatter_kws': {'alpha': 0.3, 's': 10},  # Transparencia y tamaño de puntos
            'line_kws': {'color': 'red', 'linewidth': 2}  # Línea de regresión
        },
        diag_kws={
            'bins': 30,          # Número de bins en histogramas
            'edgecolor': 'black',
            'alpha': 0.7
        },
        height=2.5,              # Altura de cada subplot
        aspect=1                 # Aspecto cuadrado
    )
    
    # Título general
    pairplot.fig.suptitle(
        'Pairplot - Análisis de Correlación entre Variables Numéricas\n' +
        'Líneas rojas: Regresión lineal | Transparencia: Densidad de datos',
        y=1.02,
        fontsize=14,
        fontweight='bold'
    )
    
    plt.tight_layout()
    guardar_grafico('08_pairplot_correlaciones.png', dpi=300)
    plt.show()
    
    print(f"\n✅ Pairplot generado exitosamente")
    
    # Análisis de correlaciones
    print("\n" + "="*70)
    print("📊 MATRIZ DE CORRELACIÓN")
    print("="*70)
    
    # Calcular matriz de correlación
    correlacion_matriz = df_pairplot.corr()
    
    # Mostrar matriz completa
    print("\n📋 Matriz de correlación completa:")
    display(correlacion_matriz.round(3))
    
    # Visualización de la matriz de correlación
    plt.figure(figsize=(10, 8))
    
    # Crear máscara para el triángulo superior (corner=True)
    mask = np.triu(np.ones_like(correlacion_matriz, dtype=bool))
    
    sns.heatmap(
        correlacion_matriz,
        mask=mask,
        annot=True,
        fmt='.3f',
        cmap='RdBu_r',
        center=0,
        square=True,
        linewidths=1,
        cbar_kws={"shrink": 0.8, "label": "Coeficiente de Correlación"},
        vmin=-1,
        vmax=1
    )
    
    plt.title('Matriz de Correlación - Variables Numéricas\n(Triángulo inferior)', 
              fontsize=14, fontweight='bold', pad=20)
    plt.xticks(rotation=45, ha='right')
    plt.yticks(rotation=0)
    plt.tight_layout()
    guardar_grafico('09_matriz_correlacion_corner.png')
    plt.show()
    
    # Análisis detallado de correlaciones con log_price
    print("\n" + "="*70)
    print("🎯 ANÁLISIS DE CORRELACIONES CON log_price")
    print("="*70)
    
    correlaciones_precio = correlacion_matriz['log_price'].drop('log_price').sort_values(ascending=False)
    
    print("\n📊 Correlaciones ordenadas (de mayor a menor):")
    for i, (var, corr) in enumerate(correlaciones_precio.items(), 1):
        # Interpretación de la fuerza de correlación
        if abs(corr) >= 0.7:
            fuerza = "🔴 Fuerte"
        elif abs(corr) >= 0.4:
            fuerza = "🟡 Moderada"
        elif abs(corr) >= 0.2:
            fuerza = "🟢 Débil"
        else:
            fuerza = "⚪ Muy débil"
        
        signo = "+" if corr > 0 else "-"
        print(f"   {i}. {var:<25} {signo}{abs(corr):.4f}  {fuerza}")
    
    # Visualización de correlaciones con log_price
    plt.figure(figsize=(10, 6))
    
    colors = ['darkgreen' if x > 0 else 'darkred' for x in correlaciones_precio]
    bars = plt.barh(correlaciones_precio.index, correlaciones_precio.values, 
                    color=colors, alpha=0.7, edgecolor='black')
    
    plt.xlabel('Coeficiente de Correlación con log_price', fontsize=12, fontweight='bold')
    plt.ylabel('Variables', fontsize=12, fontweight='bold')
    plt.title('Correlación de Variables Numéricas con log_price\n' +
              'Verde: Correlación positiva | Rojo: Correlación negativa',
              fontsize=13, fontweight='bold', pad=20)
    plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
    plt.axvline(x=0.4, color='green', linestyle='--', linewidth=1, alpha=0.5, label='Moderada (+0.4)')
    plt.axvline(x=-0.4, color='red', linestyle='--', linewidth=1, alpha=0.5, label='Moderada (-0.4)')
    plt.grid(True, alpha=0.3, axis='x')
    plt.legend(loc='lower right')
    
    # Añadir valores en las barras
    for i, (bar, val) in enumerate(zip(bars, correlaciones_precio.values)):
        plt.text(val + (0.02 if val > 0 else -0.02), i, f'{val:.3f}',
                va='center', ha='left' if val > 0 else 'right',
                fontsize=9, fontweight='bold')
    
    plt.tight_layout()
    guardar_grafico('10_correlaciones_log_price_barras.png')
    plt.show()
    
    # Interpretación y recomendaciones
    print("\n" + "="*70)
    print("💡 INTERPRETACIÓN Y RECOMENDACIONES")
    print("="*70)
    
    # Identificar mejores predictores
    mejores_predictores = correlaciones_precio[abs(correlaciones_precio) >= 0.3]
    
    if len(mejores_predictores) > 0:
        print(f"\n✅ Variables con correlación moderada o fuerte (|r| ≥ 0.3):")
        for var, corr in mejores_predictores.items():
            print(f"   • {var}: {corr:.4f}")
        print("\n   💡 Estas variables son candidatas fuertes para el modelo de regresión")
    else:
        print("\n⚠️  No se encontraron variables con correlación moderada o fuerte")
    
    # Identificar predictores débiles
    predictores_debiles = correlaciones_precio[abs(correlaciones_precio) < 0.2]
    
    if len(predictores_debiles) > 0:
        print(f"\n⚠️  Variables con correlación muy débil (|r| < 0.2):")
        for var, corr in predictores_debiles.items():
            print(f"   • {var}: {corr:.4f}")
        print("\n   💡 Considerar excluir estas variables del modelo final")
    
    # Análisis de multicolinealidad entre predictores
    print("\n" + "="*70)
    print("🔍 ANÁLISIS DE MULTICOLINEALIDAD ENTRE PREDICTORES")
    print("="*70)
    
    # Buscar pares con alta correlación (excluyendo log_price)
    vars_sin_precio = [v for v in variables_disponibles if v != 'log_price']
    corr_predictores = df_pairplot[vars_sin_precio].corr()
    
    pares_alta_corr = []
    for i in range(len(corr_predictores.columns)):
        for j in range(i+1, len(corr_predictores.columns)):
            corr_val = corr_predictores.iloc[i, j]
            if abs(corr_val) > 0.5:
                pares_alta_corr.append({
                    'Variable 1': corr_predictores.columns[i],
                    'Variable 2': corr_predictores.columns[j],
                    'Correlación': corr_val
                })
    
    if pares_alta_corr:
        df_pares = pd.DataFrame(pares_alta_corr).sort_values('Correlación', 
                                                              key=abs, 
                                                              ascending=False)
        print(f"\n⚠️  Pares de predictores con correlación |r| > 0.5:")
        display(df_pares)
        print("\n   💡 Alta correlación entre predictores puede causar multicolinealidad")
        print("      Considerar eliminar una variable de cada par en el modelo final")
    else:
        print("\n✅ No se detectó multicolinealidad significativa entre predictores")
    
    print("\n✅ Análisis de correlación completado exitosamente")
    
else:
    print(f"\n❌ Error: Se necesitan al menos 2 variables para generar el pairplot")
    print(f"   Variables disponibles: {len(variables_disponibles)}")

# ====================================================================
# ============================================
# 4.1 SELECCIÓN FINAL DE VARIABLES PARA EL MODELO
# ============================================

print("="*70)
print("🎯 SELECCIÓN FINAL DE VARIABLES PARA EL MODELO")
print("="*70)

print("\n📊 VALIDACIÓN DE RESULTADOS DE CORRELACIÓN:")
print("="*70)
print("   ✅ Matriz de correlación triangular inferior ejecutada")
print("   ✅ Subconjunto analizado: 66,438 observaciones")
print("   ✅ Variable objetivo: log_price")

print("\n📋 DECISIONES BASADAS EN ANÁLISIS DE CORRELACIÓN:")
print("="*70)

print("\n1️⃣  VARIABLE: accommodates")
print("   ✅ DECISIÓN: INCLUIR")
print("   📊 Correlación con log_price: 0.5201")
print("   💡 Justificación: Predictor principal - mayor correlación positiva")

print("\n2️⃣  VARIABLE: bedrooms")
print("   ⚠️  DECISIÓN: EVALUAR")
print("   📊 Correlación con log_price: (a verificar)")
print("   🔗 Correlación con accommodates: 0.532")
print("   💡 Justificación: Colinealidad moderada con accommodates")

print("\n3️⃣  VARIABLE: bathrooms")
print("   ❌ DECISIÓN: EXCLUIR")
print("   📊 Correlación con log_price: 0.1478")
print("   💡 Justificación: Baja significancia lineal (<0.2)")

print("\n4️⃣  VARIABLE: number_of_reviews")
print("   ❌ DECISIÓN: EXCLUIR")
print("   📊 Correlación con log_price: -0.0057")
print("   💡 Justificación: Correlación prácticamente nula")

print("\n5️⃣  VARIABLES: room_type (dummy variables)")
print("   ✅ DECISIÓN: INCLUIR")
print("   💡 Justificación: Variables categóricas de alta relevancia")

# Identificar variables dummy de room_type
room_type_dummies = [col for col in df_limpio.columns if col.startswith('room_type_')]

print(f"\n📋 Variables dummy de room_type identificadas: {len(room_type_dummies)}")
for i, col in enumerate(room_type_dummies, 1):
    print(f"   {i}. {col}")

# Definir variables finales para el modelo
variables_independientes = ['accommodates', 'bedrooms'] + room_type_dummies
variable_dependiente = 'log_price'

print(f"\n📊 CONFIGURACIÓN FINAL DEL MODELO:")
print("="*70)
print(f"\n🎯 Variable Dependiente (Y):")
print(f"   • {variable_dependiente}")

print(f"\n📊 Variables Independientes (X): {len(variables_independientes)}")
print(f"\n   🔢 Numéricas continuas: 2")
print(f"      1. accommodates")
print(f"      2. bedrooms")

print(f"\n   🏷️  Variables dummy (categóricas): {len(room_type_dummies)}")
for i, col in enumerate(room_type_dummies, 1):
    print(f"      {i}. {col}")

# ====================================================================
# ============================================
# 5. DIVISIÓN EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA
# ============================================

print("\n" + "="*70)
print("✂️  DIVISIÓN EN CONJUNTOS DE ENTRENAMIENTO Y PRUEBA")
print("="*70)

# Preparar datos
X = df_limpio[variables_independientes].copy()
y = df_limpio[variable_dependiente].copy()

print(f"\n📊 Dimensiones de los datos:")
print(f"   X (variables independientes): {X.shape}")
print(f"   y (variable dependiente): {y.shape}")

# Verificar valores nulos
print(f"\n🔍 Verificación de valores nulos:")
print(f"   X: {X.isnull().sum().sum()} valores nulos")
print(f"   y: {y.isnull().sum()} valores nulos")

# Eliminar filas con valores nulos si existen
if X.isnull().sum().sum() > 0 or y.isnull().sum() > 0:
    filas_antes = len(X)
    mask = ~(X.isnull().any(axis=1) | y.isnull())
    X = X[mask]
    y = y[mask]
    filas_despues = len(X)
    print(f"   ⚠️  Eliminadas {filas_antes - filas_despues:,} filas con valores nulos")

# División 80-20
test_size = 0.2
random_state = 42

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=test_size, 
    random_state=random_state
)

print(f"\n✅ División completada:")
print(f"   Proporción: {int((1-test_size)*100)}% entrenamiento - {int(test_size*100)}% prueba")
print(f"   Random state: {random_state}")

print(f"\n📊 Conjunto de ENTRENAMIENTO:")
print(f"   X_train: {X_train.shape[0]:,} filas × {X_train.shape[1]} columnas")
print(f"   y_train: {y_train.shape[0]:,} valores")
print(f"   Porcentaje: {len(X_train)/len(X)*100:.2f}%")

print(f"\n📊 Conjunto de PRUEBA:")
print(f"   X_test: {X_test.shape[0]:,} filas × {X_test.shape[1]} columnas")
print(f"   y_test: {y_test.shape[0]:,} valores")
print(f"   Porcentaje: {len(X_test)/len(X)*100:.2f}%")

# Estadísticas de la variable dependiente
print(f"\n📊 Estadísticas de log_price:")
print(f"\n   ENTRENAMIENTO:")
print(f"      Media: {y_train.mean():.4f}")
print(f"      Mediana: {y_train.median():.4f}")
print(f"      Desv. Est.: {y_train.std():.4f}")
print(f"      Mín: {y_train.min():.4f}")
print(f"      Máx: {y_train.max():.4f}")

print(f"\n   PRUEBA:")
print(f"      Media: {y_test.mean():.4f}")
print(f"      Mediana: {y_test.median():.4f}")
print(f"      Desv. Est.: {y_test.std():.4f}")
print(f"      Mín: {y_test.min():.4f}")
print(f"      Máx: {y_test.max():.4f}")

# Visualización de la distribución
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Histograma conjunto de entrenamiento
axes[0].hist(y_train, bins=50, edgecolor='black', alpha=0.7, color='steelblue')
axes[0].axvline(y_train.mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {y_train.mean():.2f}')
axes[0].axvline(y_train.median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: {y_train.median():.2f}')
axes[0].set_xlabel('log_price', fontsize=12)
axes[0].set_ylabel('Frecuencia', fontsize=12)
axes[0].set_title(f'Distribución de log_price - ENTRENAMIENTO\n(n={len(y_train):,})', fontsize=12, fontweight='bold')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Histograma conjunto de prueba
axes[1].hist(y_test, bins=50, edgecolor='black', alpha=0.7, color='coral')
axes[1].axvline(y_test.mean(), color='red', linestyle='--', linewidth=2, label=f'Media: {y_test.mean():.2f}')
axes[1].axvline(y_test.median(), color='green', linestyle='--', linewidth=2, label=f'Mediana: {y_test.median():.2f}')
axes[1].set_xlabel('log_price', fontsize=12)
axes[1].set_ylabel('Frecuencia', fontsize=12)
axes[1].set_title(f'Distribución de log_price - PRUEBA\n(n={len(y_test):,})', fontsize=12, fontweight='bold')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
guardar_grafico('11_distribucion_train_test.png')
plt.show()

print("\n✅ División de datos completada exitosamente")

# ====================================================================
# ============================================
# 6. CONSTRUCCIÓN Y ENTRENAMIENTO DEL MODELO
# ============================================

print("\n" + "="*70)
print("🤖 CONSTRUCCIÓN Y ENTRENAMIENTO DEL MODELO")
print("="*70)

print("\n📋 ESPECIFICACIONES DEL MODELO:")
print("   • Tipo: Regresión Lineal Múltiple")
print("   • Método: Mínimos Cuadrados Ordinarios (OLS)")
print("   • Variables independientes: " + str(len(variables_independientes)))
print("   • Observaciones de entrenamiento: " + f"{len(X_train):,}")

# Crear modelo
modelo = LinearRegression()

# Entrenar modelo
print("\n⏳ Entrenando modelo...")
modelo.fit(X_train, y_train)
print("✅ Modelo entrenado exitosamente")

# Coeficientes del modelo
print("\n📊 COEFICIENTES DEL MODELO:")
print("="*70)

coeficientes = pd.DataFrame({
    'Variable': variables_independientes,
    'Coeficiente': modelo.coef_
}).sort_values('Coeficiente', key=abs, ascending=False)

print(f"\n📈 Intercepto (β₀): {modelo.intercept_:.6f}")
print(f"\n📊 Coeficientes de las variables (βᵢ):")
display(coeficientes)

# Interpretación de coeficientes
print("\n💡 INTERPRETACIÓN DE COEFICIENTES:")
print("="*70)
print("   Dado que la variable dependiente es log_price:")
print("   • Un aumento de 1 unidad en una variable numérica aumenta")
print("     el log_price en βᵢ unidades")
print("   • Para variables dummy, el coeficiente representa la diferencia")
print("     en log_price respecto a la categoría de referencia")

# Visualización de coeficientes
plt.figure(figsize=(12, 8))

colors = ['darkgreen' if x > 0 else 'darkred' for x in coeficientes['Coeficiente']]
bars = plt.barh(coeficientes['Variable'], coeficientes['Coeficiente'], 
                color=colors, alpha=0.7, edgecolor='black')

plt.xlabel('Coeficiente (β)', fontsize=12, fontweight='bold')
plt.ylabel('Variables', fontsize=12, fontweight='bold')
plt.title('Coeficientes del Modelo de Regresión Lineal Múltiple\n' +
          'Verde: Efecto positivo | Rojo: Efecto negativo',
          fontsize=13, fontweight='bold', pad=20)
plt.axvline(x=0, color='black', linestyle='-', linewidth=1.5)
plt.grid(True, alpha=0.3, axis='x')

# Añadir valores en las barras
for i, (bar, val) in enumerate(zip(bars, coeficientes['Coeficiente'])):
    plt.text(val + (0.01 if val > 0 else -0.01), i, f'{val:.4f}',
            va='center', ha='left' if val > 0 else 'right',
            fontsize=9, fontweight='bold')

plt.tight_layout()
guardar_grafico('12_coeficientes_modelo.png')
plt.show()

# ====================================================================
# ============================================
# 7. EVALUACIÓN DEL MODELO
# ============================================

print("\n" + "="*70)
print("📊 EVALUACIÓN DEL MODELO")
print("="*70)

# Predicciones en conjunto de entrenamiento
y_train_pred = modelo.predict(X_train)

# Predicciones en conjunto de prueba
y_test_pred = modelo.predict(X_test)

# Métricas de entrenamiento
r2_train = r2_score(y_train, y_train_pred)
mse_train = mean_squared_error(y_train, y_train_pred)
rmse_train = np.sqrt(mse_train)
mae_train = mean_absolute_error(y_train, y_train_pred)

# Métricas de prueba
r2_test = r2_score(y_test, y_test_pred)
mse_test = mean_squared_error(y_test, y_test_pred)
rmse_test = np.sqrt(mse_test)
mae_test = mean_absolute_error(y_test, y_test_pred)

print("\n📊 MÉTRICAS DE RENDIMIENTO:")
print("="*70)

print("\n🔵 CONJUNTO DE ENTRENAMIENTO:")
print(f"   R² (Coeficiente de Determinación): {r2_train:.6f}")
print(f"   MSE (Error Cuadrático Medio):      {mse_train:.6f}")
print(f"   RMSE (Raíz del MSE):               {rmse_train:.6f}")
print(f"   MAE (Error Absoluto Medio):        {mae_train:.6f}")

print("\n🟢 CONJUNTO DE PRUEBA:")
print(f"   R² (Coeficiente de Determinación): {r2_test:.6f}")
print(f"   MSE (Error Cuadrático Medio):      {mse_test:.6f}")
print(f"   RMSE (Raíz del MSE):               {rmse_test:.6f}")
print(f"   MAE (Error Absoluto Medio):        {mae_test:.6f}")

# Diferencia entre entrenamiento y prueba
print("\n📊 ANÁLISIS DE SOBREAJUSTE:")
print("="*70)
diferencia_r2 = abs(r2_train - r2_test)
print(f"   Diferencia en R²: {diferencia_r2:.6f}")

if diferencia_r2 < 0.05:
    print("   ✅ Diferencia mínima - Modelo generaliza bien")
elif diferencia_r2 < 0.10:
    print("   ⚠️  Diferencia moderada - Revisar posible sobreajuste")
else:
    print("   ❌ Diferencia significativa - Modelo sobreajustado")

# Interpretación del R²
print("\n💡 INTERPRETACIÓN DEL R²:")
print("="*70)
print(f"   El modelo explica el {r2_test*100:.2f}% de la variabilidad")
print(f"   en log_price usando las variables seleccionadas.")

if r2_test >= 0.7:
    calidad = "🟢 EXCELENTE"
elif r2_test >= 0.5:
    calidad = "🟡 BUENO"
elif r2_test >= 0.3:
    calidad = "🟠 MODERADO"
else:
    calidad = "🔴 BAJO"

print(f"\n   Calidad del ajuste: {calidad}")

# Tabla comparativa
metricas_comparacion = pd.DataFrame({
    'Métrica': ['R²', 'MSE', 'RMSE', 'MAE'],
    'Entrenamiento': [r2_train, mse_train, rmse_train, mae_train],
    'Prueba': [r2_test, mse_test, rmse_test, mae_test],
    'Diferencia': [
        abs(r2_train - r2_test),
        abs(mse_train - mse_test),
        abs(rmse_train - rmse_test),
        abs(mae_train - mae_train)
    ]
})

print("\n📋 TABLA COMPARATIVA DE MÉTRICAS:")
display(metricas_comparacion)

# ====================================================================
# ============================================
# 8. PREDICCIONES Y COMPARACIÓN
# ============================================

print("\n" + "="*70)
print("🎯 PREDICCIONES Y COMPARACIÓN CON VALORES REALES")
print("="*70)

# Crear DataFrame con predicciones
resultados = pd.DataFrame({
    'Real': y_test,
    'Predicción': y_test_pred,
    'Error': y_test - y_test_pred,
    'Error_Absoluto': np.abs(y_test - y_test_pred),
    'Error_Porcentual': np.abs((y_test - y_test_pred) / y_test) * 100
})

print("\n📊 PRIMERAS 10 PREDICCIONES:")
display(resultados.head(10))

print("\n📊 ESTADÍSTICAS DE LOS ERRORES:")
print("="*70)
print(f"   Error medio: {resultados['Error'].mean():.6f}")
print(f"   Error absoluto medio: {resultados['Error_Absoluto'].mean():.6f}")
print(f"   Error porcentual medio: {resultados['Error_Porcentual'].mean():.2f}%")
print(f"   Error máximo: {resultados['Error_Absoluto'].max():.6f}")
print(f"   Error mínimo: {resultados['Error_Absoluto'].min():.6f}")

# Visualización: Valores reales vs predicciones
fig, axes = plt.subplots(2, 2, figsize=(16, 14))

# Gráfico 1: Scatter plot - Real vs Predicción
axes[0, 0].scatter(y_test, y_test_pred, alpha=0.3, s=10, color='steelblue')
axes[0, 0].plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
                'r--', linewidth=2, label='Predicción perfecta')
axes[0, 0].set_xlabel('log_price Real', fontsize=12, fontweight='bold')
axes[0, 0].set_ylabel('log_price Predicho', fontsize=12, fontweight='bold')
axes[0, 0].set_title(f'Valores Reales vs Predicciones\nR² = {r2_test:.4f}', 
                     fontsize=12, fontweight='bold')
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Gráfico 2: Distribución de errores
axes[0, 1].hist(resultados['Error'], bins=50, edgecolor='black', alpha=0.7, color='coral')
axes[0, 1].axvline(0, color='red', linestyle='--', linewidth=2, label='Error = 0')
axes[0, 1].axvline(resultados['Error'].mean(), color='green', linestyle='--', 
                   linewidth=2, label=f'Media: {resultados["Error"].mean():.4f}')
axes[0, 1].set_xlabel('Error (Real - Predicción)', fontsize=12, fontweight='bold')
axes[0, 1].set_ylabel('Frecuencia', fontsize=12, fontweight='bold')
axes[0, 1].set_title('Distribución de Errores', fontsize=12, fontweight='bold')
axes[0, 1].legend()
axes[0, 1].grid(True, alpha=0.3)

# Gráfico 3: Residuos vs Predicciones
axes[1, 0].scatter(y_test_pred, resultados['Error'], alpha=0.3, s=10, color='purple')
axes[1, 0].axhline(0, color='red', linestyle='--', linewidth=2)
axes[1, 0].set_xlabel('log_price Predicho', fontsize=12, fontweight='bold')
axes[1, 0].set_ylabel('Residuos (Error)', fontsize=12, fontweight='bold')
axes[1, 0].set_title('Análisis de Residuos', fontsize=12, fontweight='bold')
axes[1, 0].grid(True, alpha=0.3)

# Gráfico 4: Q-Q Plot (normalidad de residuos)
stats.probplot(resultados['Error'], dist="norm", plot=axes[1, 1])
axes[1, 1].set_title('Q-Q Plot - Normalidad de Residuos', fontsize=12, fontweight='bold')
axes[1, 1].grid(True, alpha=0.3)

plt.tight_layout()
guardar_grafico('13_analisis_predicciones.png', dpi=300)
plt.show()

print("\n✅ Análisis de predicciones completado")

# ====================================================================
# ============================================
# 9. CÁLCULO DEL ERROR CUADRÁTICO MEDIO (MSE)
# ============================================

print("\n" + "="*70)
print("📐 CÁLCULO DEL ERROR CUADRÁTICO MEDIO (MSE)")
print("="*70)

print("\n💡 DEFINICIÓN:")
print("   El MSE mide el promedio de los errores al cuadrado entre")
print("   las predicciones y los valores reales.")
print("\n   Fórmula: MSE = (1/n) × Σ(yᵢ - ŷᵢ)²")

print("\n📊 RESULTADOS:")
print("="*70)
print(f"\n🔵 MSE - Conjunto de ENTRENAMIENTO: {mse_train:.6f}")
print(f"🟢 MSE - Conjunto de PRUEBA:        {mse_test:.6f}")

print(f"\n📊 RMSE (Raíz del MSE):")
print(f"   Entrenamiento: {rmse_train:.6f}")
print(f"   Prueba:        {rmse_test:.6f}")

print("\n💡 INTERPRETACIÓN DEL MSE:")
print("="*70)
print(f"   • El MSE en el conjunto de prueba es {mse_test:.6f}")
print(f"   • El RMSE es {rmse_test:.6f}, que representa el error")
print(f"     promedio en la escala de log_price")
print(f"   • Un RMSE más bajo indica mejores predicciones")

# Comparación visual
fig, ax = plt.subplots(1, 1, figsize=(10, 6))

metricas = ['MSE', 'RMSE', 'MAE']
train_vals = [mse_train, rmse_train, mae_train]
test_vals = [mse_test, rmse_test, mae_test]

x = np.arange(len(metricas))
width = 0.35

bars1 = ax.bar(x - width/2, train_vals, width, label='Entrenamiento', 
               alpha=0.8, color='steelblue', edgecolor='black')
bars2 = ax.bar(x + width/2, test_vals, width, label='Prueba', 
               alpha=0.8, color='coral', edgecolor='black')

ax.set_xlabel('Métricas de Error', fontsize=12, fontweight='bold')
ax.set_ylabel('Valor', fontsize=12, fontweight='bold')
ax.set_title('Comparación de Métricas de Error\nEntrenamiento vs Prueba', 
             fontsize=13, fontweight='bold', pad=20)
ax.set_xticks(x)
ax.set_xticklabels(metricas)
ax.legend()
ax.grid(True, alpha=0.3, axis='y')

# Añadir valores en las barras
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height:.4f}',
                ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
guardar_grafico('14_metricas_error_comparacion.png')
plt.show()

# ====================================================================
# ============================================
# RESUMEN FINAL DEL MODELO
# ============================================

print("\n" + "="*70)
print("📋 RESUMEN FINAL DEL MODELO")
print("="*70)

print("\n🎯 CONFIGURACIÓN DEL MODELO:")
print(f"   • Tipo: Regresión Lineal Múltiple")
print(f"   • Variables independientes: {len(variables_independientes)}")
print(f"   • Observaciones totales: {len(X):,}")
print(f"   • Entrenamiento: {len(X_train):,} ({len(X_train)/len(X)*100:.1f}%)")
print(f"   • Prueba: {len(X_test):,} ({len(X_test)/len(X)*100:.1f}%)")

print("\n📊 RENDIMIENTO DEL MODELO:")
print(f"   • R² (Prueba): {r2_test:.4f} ({r2_test*100:.2f}% de varianza explicada)")
print(f"   • MSE (Prueba): {mse_test:.6f}")
print(f"   • RMSE (Prueba): {rmse_test:.6f}")
print(f"   • MAE (Prueba): {mae_test:.6f}")

print("\n🔝 TOP 3 VARIABLES MÁS INFLUYENTES:")
top_3 = coeficientes.head(3)
for i, row in top_3.iterrows():
    print(f"   {i+1}. {row['Variable']}: {row['Coeficiente']:.6f}")

print("\n✅ ANÁLISIS COMPLETADO EXITOSAMENTE")
print("="*70)


"""
- la cantidad permitida de personas en un aribnb es la que mas afecta el precio con un r de ~50% de la varianza
- otros factores con poco valor es el numero de habitaciones y el numero de baños pero son irrelavantes y realmente no tiene peso que puda describir el precio
- el modelo entrenado explica el 44% de la variancia sirve para generar 

"""
