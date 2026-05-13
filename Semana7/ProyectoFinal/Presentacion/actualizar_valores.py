#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para automatizar la actualización de la presentación LaTeX
inyectando directamente las métricas guardadas en metricas_modelo.json
"""

import json
import re
from pathlib import Path

def actualizar_presentacion():
    base_dir = Path(__file__).parent
    json_path = base_dir / 'metricas_modelo.json'
    
    # Buscar keynote.tex o presentacion.tex
    tex_path = base_dir / 'keynote.tex'
    if not tex_path.exists():
        tex_path = base_dir / 'presentacion.tex'
        if not tex_path.exists():
            print("❌ No se encontró keynote.tex ni presentacion.tex en el directorio.")
            return

    if not json_path.exists():
        print("❌ No se encontró metricas_modelo.json. ¡Ejecuta el script principal de Python primero!")
        return

    print(f"📖 Leyendo métricas desde {json_path.name}...")
    with open(json_path, 'r', encoding='utf-8') as f:
        metricas = json.load(f)

    print(f"📝 Inyectando datos en {tex_path.name}...")
    with open(tex_path, 'r', encoding='utf-8') as f:
        contenido = f.read()

    # 1. Actualizar métricas generales
    r2_tr = f"{metricas['metricas']['entrenamiento']['r2']:.4f}"
    r2_te = f"{metricas['metricas']['prueba']['r2']:.4f}"
    mse_tr = f"{metricas['metricas']['entrenamiento']['mse']:.4f}"
    mse_te = f"{metricas['metricas']['prueba']['mse']:.4f}"
    rmse_tr = f"{metricas['metricas']['entrenamiento']['rmse']:.4f}"
    rmse_te = f"{metricas['metricas']['prueba']['rmse']:.4f}"
    mae_tr = f"{metricas['metricas']['entrenamiento']['mae']:.4f}"
    mae_te = f"{metricas['metricas']['prueba']['mae']:.4f}"

    # Regex para la tabla principal
    contenido = re.sub(r'R²\s*&\s*[\d.]+\s*&\s*[\d.]+\s*\\\\', f'R² & {r2_tr} & {r2_te} \\\\', contenido)
    contenido = re.sub(r'MSE\s*&\s*[\d.]+\s*&\s*[\d.]+\s*\\\\', f'MSE & {mse_tr} & {mse_te} \\\\', contenido)
    contenido = re.sub(r'RMSE\s*&\s*[\d.]+\s*&\s*[\d.]+\s*\\\\', f'RMSE & {rmse_tr} & {rmse_te} \\\\', contenido)
    contenido = re.sub(r'MAE\s*&\s*[\d.]+\s*&\s*[\d.]+\s*\\\\', f'MAE & {mae_tr} & {mae_te} \\\\', contenido)

    # 2. Textos interpretativos y de Dataset
    r2_pct = f"{metricas['metricas']['prueba']['r2']*100:.2f}"
    filas = metricas['dataset']['limpio']['filas']
    n_vars = metricas['modelo']['n_variables']
    cols = metricas['dataset']['limpio']['columnas']
    
    contenido = re.sub(r'explica el \\alert\{[\d.]+\\%\}', f'explica el \\alert{{{r2_pct}\\%}}', contenido)
    contenido = re.sub(r'\\alert\{[\d,]+\sobservaciones\}\sy\s\\alert\{\d+\svariables\}', f'\\\\alert{{{filas:,} observaciones}} y \\\\alert{{{cols} variables}}', contenido)
    contenido = re.sub(r'\\textbf\{Variables independientes:\}\s*\d+', f'\\\\textbf{{Variables independientes:}} {n_vars}', contenido)
    
    # 3. Resumen Ejecutivo (al final de la diapo)
    contenido = re.sub(r'\\textbf\{Dataset:\}\s*&\s*[\d,]+\s*observaciones', f'\\\\textbf{{Dataset:}} & {filas:,} observaciones', contenido)
    contenido = re.sub(r'\\textbf\{Variables:\}\s*&\s*[\d]+\s*predictores', f'\\\\textbf{{Variables:}} & {n_vars} predictores', contenido)
    contenido = re.sub(r'\\textbf\{R²:\}\s*&\s*[\d.]+\\%', f'\\\\textbf{{R²:}} & {r2_pct}\\%', contenido)
    contenido = re.sub(r'\\textbf\{RMSE:\}\s*&\s*[\d.]+', f'\\\\textbf{{RMSE:}} & {rmse_te}', contenido)

    # 4. Tabla dinámica de predicciones / errores
    err_med = f"{metricas['errores']['error_medio']:.4f}"
    err_max = f"{metricas['errores']['error_maximo']:.4f}"
    err_min = f"{metricas['errores']['error_minimo']:.4f}"
    err_pct = f"{metricas['errores'].get('error_porcentual_medio', 0.0):.2f}"
    
    contenido = re.sub(r'Error medio\s*&\s*[\d.-]+\s*\\\\', f'Error medio & {err_med} \\\\', contenido)
    contenido = re.sub(r'Error absoluto medio \(MAE\)\s*&\s*[\d.-]+\s*\\\\', f'Error absoluto medio (MAE) & {mae_te} \\\\', contenido)
    contenido = re.sub(r'Error porcentual medio\s*&\s*[\d.-]+\\%', f'Error porcentual medio & {err_pct}\\%', contenido)
    contenido = re.sub(r'Error máximo\s*&\s*[\d.-]+\s*\\\\', f'Error máximo & {err_max} \\\\', contenido)
    contenido = re.sub(r'Error mínimo\s*&\s*[\d.-]+\s*\\\\', f'Error mínimo & {err_min} \\\\', contenido)

    # 5. Tabla de coeficientes dinámica (Top 4)
    top_coefs = sorted(metricas['modelo']['coeficientes'].items(), key=lambda x: abs(x[1]), reverse=True)
    coef_str = r"\midrule" + "\n"
    coef_str += f"      Intercepto & {metricas['modelo']['intercepto']:.4f} \\\\\n"
    
    for var, coef in top_coefs[:4]:
        escaped_var = var.replace('_', '\\_')
        sign = "+" if coef > 0 else ""
        coef_str += f"      \\texttt{{{escaped_var}}} & {sign}{coef:.4f} \\\\\n"
        
    contenido = re.sub(r'\\midrule\s*Intercepto.*?\\bottomrule', coef_str + "      \\\\bottomrule", contenido, flags=re.DOTALL)

    # Guardar cambios
    with open(tex_path, 'w', encoding='utf-8') as f:
        f.write(contenido)
        
    print(f"✅ ¡Actualización completada! Tu {tex_path.name} está ahora sincronizado con el modelo final.")

if __name__ == '__main__':
    print("🚀 Sincronizador Automático de Resultados -> LaTeX")
    print("="*60)
    actualizar_presentacion()
