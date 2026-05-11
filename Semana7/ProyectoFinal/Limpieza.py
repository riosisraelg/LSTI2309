"""
Script de Limpieza de Datos para el Proyecto Final
Curso: QR.LSTI2309TEO - Universidad Tecmilenio

Este script contiene funciones para limpiar y preparar los datos
del dataset de Airbnb para el modelado predictivo.
"""

import pandas as pd
import numpy as np
from scipy import stats


def cargar_datos(ruta='Datos/train.csv'):
    """
    Carga el dataset desde un archivo CSV.
    
    Parameters:
    -----------
    ruta : str
        Ruta al archivo CSV
        
    Returns:
    --------
    pd.DataFrame
        DataFrame con los datos cargados
    """
    try:
        df = pd.read_csv(ruta)
        print(f"✅ Datos cargados exitosamente: {df.shape[0]} filas, {df.shape[1]} columnas")
        return df
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo en {ruta}")
        return None


def analizar_valores_faltantes(df):
    """
    Analiza y reporta los valores faltantes en el dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a analizar
        
    Returns:
    --------
    pd.DataFrame
        DataFrame con el conteo y porcentaje de valores faltantes
    """
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
    
    print(f"\n📊 Análisis de Valores Faltantes:")
    print(f"Total de columnas con valores faltantes: {len(missing_df)}")
    print(missing_df.to_string(index=False))
    
    return missing_df


def imputar_valores_numericos(df, columnas, estrategia='median'):
    """
    Imputa valores faltantes en columnas numéricas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a procesar
    columnas : list
        Lista de columnas numéricas a imputar
    estrategia : str
        Estrategia de imputación: 'mean', 'median', 'mode'
        
    Returns:
    --------
    pd.DataFrame
        DataFrame con valores imputados
    """
    df_copy = df.copy()
    
    for col in columnas:
        if col in df_copy.columns:
            antes = df_copy[col].isnull().sum()
            
            if estrategia == 'mean':
                valor = df_copy[col].mean()
            elif estrategia == 'median':
                valor = df_copy[col].median()
            elif estrategia == 'mode':
                valor = df_copy[col].mode()[0]
            else:
                raise ValueError("Estrategia debe ser 'mean', 'median' o 'mode'")
            
            df_copy[col].fillna(valor, inplace=True)
            despues = df_copy[col].isnull().sum()
            
            print(f"✅ {col}: {antes} valores imputados con {estrategia} = {valor:.2f}")
    
    return df_copy


def eliminar_columnas_irrelevantes(df, columnas):
    """
    Elimina columnas que no son relevantes para el modelo.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a procesar
    columnas : list
        Lista de columnas a eliminar
        
    Returns:
    --------
    pd.DataFrame
        DataFrame sin las columnas especificadas
    """
    df_copy = df.copy()
    columnas_existentes = [col for col in columnas if col in df_copy.columns]
    
    if columnas_existentes:
        df_copy = df_copy.drop(columns=columnas_existentes)
        print(f"✅ Eliminadas {len(columnas_existentes)} columnas: {', '.join(columnas_existentes)}")
    
    return df_copy


def detectar_outliers_iqr(df, columna, factor=1.5):
    """
    Detecta outliers usando el método IQR (Rango Intercuartílico).
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a analizar
    columna : str
        Nombre de la columna a analizar
    factor : float
        Factor multiplicador del IQR (por defecto 1.5)
        
    Returns:
    --------
    tuple
        (índices de outliers, límite inferior, límite superior)
    """
    Q1 = df[columna].quantile(0.25)
    Q3 = df[columna].quantile(0.75)
    IQR = Q3 - Q1
    
    limite_inferior = Q1 - factor * IQR
    limite_superior = Q3 + factor * IQR
    
    outliers = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    
    print(f"\n📊 Outliers en '{columna}':")
    print(f"   Límite inferior: {limite_inferior:.2f}")
    print(f"   Límite superior: {limite_superior:.2f}")
    print(f"   Total de outliers: {len(outliers)} ({len(outliers)/len(df)*100:.2f}%)")
    
    return outliers.index, limite_inferior, limite_superior


def eliminar_outliers(df, columna, factor=1.5):
    """
    Elimina outliers de una columna específica.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a procesar
    columna : str
        Nombre de la columna
    factor : float
        Factor multiplicador del IQR
        
    Returns:
    --------
    pd.DataFrame
        DataFrame sin outliers
    """
    outliers_idx, _, _ = detectar_outliers_iqr(df, columna, factor)
    df_limpio = df.drop(outliers_idx)
    
    print(f"✅ Eliminados {len(outliers_idx)} outliers de '{columna}'")
    print(f"   Registros restantes: {len(df_limpio)}")
    
    return df_limpio


def codificar_variables_categoricas(df, columnas, metodo='onehot'):
    """
    Codifica variables categóricas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a procesar
    columnas : list
        Lista de columnas categóricas a codificar
    metodo : str
        Método de codificación: 'onehot' o 'label'
        
    Returns:
    --------
    pd.DataFrame
        DataFrame con variables codificadas
    """
    df_copy = df.copy()
    
    if metodo == 'onehot':
        df_copy = pd.get_dummies(df_copy, columns=columnas, drop_first=True)
        print(f"✅ Codificación One-Hot aplicada a {len(columnas)} columnas")
    elif metodo == 'label':
        from sklearn.preprocessing import LabelEncoder
        le = LabelEncoder()
        for col in columnas:
            if col in df_copy.columns:
                df_copy[col] = le.fit_transform(df_copy[col].astype(str))
        print(f"✅ Codificación Label aplicada a {len(columnas)} columnas")
    
    return df_copy


def normalizar_datos(df, columnas, metodo='standard'):
    """
    Normaliza o estandariza columnas numéricas.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a procesar
    columnas : list
        Lista de columnas a normalizar
    metodo : str
        Método: 'standard' (z-score) o 'minmax' (0-1)
        
    Returns:
    --------
    pd.DataFrame
        DataFrame con columnas normalizadas
    """
    df_copy = df.copy()
    
    if metodo == 'standard':
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        df_copy[columnas] = scaler.fit_transform(df_copy[columnas])
        print(f"✅ Estandarización (z-score) aplicada a {len(columnas)} columnas")
    elif metodo == 'minmax':
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
        df_copy[columnas] = scaler.fit_transform(df_copy[columnas])
        print(f"✅ Normalización (min-max) aplicada a {len(columnas)} columnas")
    
    return df_copy


def pipeline_limpieza_completa(df, config=None):
    """
    Pipeline completo de limpieza de datos.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame original
    config : dict
        Configuración del pipeline (opcional)
        
    Returns:
    --------
    pd.DataFrame
        DataFrame limpio y preparado
    """
    print("\n" + "="*60)
    print("🚀 INICIANDO PIPELINE DE LIMPIEZA DE DATOS")
    print("="*60)
    
    df_limpio = df.copy()
    
    # 1. Analizar valores faltantes
    print("\n📋 PASO 1: Análisis de valores faltantes")
    analizar_valores_faltantes(df_limpio)
    
    # 2. Imputar valores numéricos
    print("\n📋 PASO 2: Imputación de valores numéricos")
    columnas_numericas = ['bathrooms', 'bedrooms', 'beds']
    df_limpio = imputar_valores_numericos(df_limpio, columnas_numericas, 'median')
    
    # 3. Eliminar columnas irrelevantes
    print("\n📋 PASO 3: Eliminación de columnas irrelevantes")
    columnas_eliminar = [
        'id', 'thumbnail_url', 'description', 'name', 
        'first_review', 'last_review', 'host_since',
        'amenities', 'zipcode'
    ]
    df_limpio = eliminar_columnas_irrelevantes(df_limpio, columnas_eliminar)
    
    # 4. Detectar outliers (sin eliminar por ahora)
    print("\n📋 PASO 4: Detección de outliers")
    detectar_outliers_iqr(df_limpio, 'log_price', factor=1.5)
    
    print("\n" + "="*60)
    print("✅ PIPELINE COMPLETADO")
    print(f"   Dimensiones finales: {df_limpio.shape[0]} filas x {df_limpio.shape[1]} columnas")
    print("="*60)
    
    return df_limpio


def guardar_datos_limpios(df, ruta='Datos/train_limpio.csv'):
    """
    Guarda el dataset limpio en un archivo CSV.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame a guardar
    ruta : str
        Ruta donde guardar el archivo
    """
    try:
        df.to_csv(ruta, index=False)
        print(f"\n✅ Datos limpios guardados en: {ruta}")
    except Exception as e:
        print(f"\n❌ Error al guardar: {e}")


# Ejemplo de uso
if __name__ == "__main__":
    # Cargar datos
    df = cargar_datos('Datos/train.csv')
    
    if df is not None:
        # Aplicar pipeline de limpieza
        df_limpio = pipeline_limpieza_completa(df)
        
        # Guardar datos limpios
        guardar_datos_limpios(df_limpio)
        
        print("\n🎉 Proceso de limpieza completado exitosamente!")
