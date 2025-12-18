#!/usr/bin/env python3
"""
Script para dividir el archivo de strings en partes manejables para traducción.
"""

from pathlib import Path

def split_strings(input_file: str, output_dir: str, split_sizes: list):
    """
    Divide el archivo de strings en partes según los tamaños especificados.
    
    Args:
        input_file: Ruta al archivo strings_full.txt
        output_dir: Directorio donde guardar las partes
        split_sizes: Lista de tamaños para cada parte
    """
    input_path = Path(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Leer todas las líneas
    with open(input_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    print(f"Total de strings: {total_lines}")
    print(f"División planificada: {split_sizes}")
    print(f"Suma de partes: {sum(split_sizes)}")
    print()
    
    current_pos = 0
    part_num = 1
    
    for size in split_sizes:
        if current_pos >= total_lines:
            break
        
        # Calcular el rango
        end_pos = min(current_pos + size, total_lines)
        part_lines = lines[current_pos:end_pos]
        
        # Nombre del archivo
        output_file = output_path / f"strings_part{part_num:02d}.txt"
        
        # Escribir la parte
        with open(output_file, 'w', encoding='utf-8') as f:
            # Cabecera con información
            f.write(f"# Parte {part_num} - Líneas {current_pos + 1} a {end_pos}\n")
            f.write(f"# Total en esta parte: {len(part_lines)} strings\n")
            f.write(f"# Formato: ID|ADDRESS|TEXT\n")
            f.write(f"#\n")
            f.writelines(part_lines)
        
        print(f"  Parte {part_num}: strings_part{part_num:02d}.txt ({len(part_lines)} líneas) - IDs {current_pos} a {end_pos - 1}")
        
        current_pos = end_pos
        part_num += 1
    
    # Verificar si quedaron líneas sin procesar
    remaining = total_lines - current_pos
    if remaining > 0:
        print(f"\n  [AVISO] Quedaron {remaining} líneas sin asignar")
    
    print(f"\n[OK] Creadas {part_num - 1} partes en: {output_path}")
    return part_num - 1


if __name__ == '__main__':
    # Configuración de división:
    # - Parte 1: 4900 (como solicitado)
    # - Partes 2-12: ~10,000 cada una (manejable para una persona)
    # 
    # Total: 115,344 strings
    # Parte 1: 4,900
    # Restante: 110,444
    # 
    # Recomendación: 11 partes adicionales de ~10,000
    # Esto permite trabajar en bloques de aproximadamente 1-2 semanas cada uno
    # (asumiendo ~100-150 líneas por día de traducción)
    
    split_config = [
        4900,   # Parte 1 (como solicitaste)
        10000,  # Parte 2
        10000,  # Parte 3
        10000,  # Parte 4
        10000,  # Parte 5
        10000,  # Parte 6
        10000,  # Parte 7
        10000,  # Parte 8
        10000,  # Parte 9
        10000,  # Parte 10
        10000,  # Parte 11
        10444,  # Parte 12 (resto)
    ]
    
    split_strings(
        input_file=r"c:\Users\Abraham\Documents\Programacion\HoshiMemoHD_ESP\strings_full.txt",
        output_dir=r"c:\Users\Abraham\Documents\Programacion\HoshiMemoHD_ESP\strings_parts",
        split_sizes=split_config
    )
