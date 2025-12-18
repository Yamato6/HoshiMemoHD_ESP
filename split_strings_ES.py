#!/usr/bin/env python3
"""
Script para dividir el archivo de strings MemoriaES en partes.
"""

from pathlib import Path

def split_strings(input_file: str, output_dir: str, split_sizes: list):
    input_path = Path(input_file)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    
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
        
        end_pos = min(current_pos + size, total_lines)
        part_lines = lines[current_pos:end_pos]
        
        output_file = output_path / f"strings_ES_part{part_num:02d}.txt"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"# Parte {part_num} - Líneas {current_pos + 1} a {end_pos}\n")
            f.write(f"# Total en esta parte: {len(part_lines)} strings\n")
            f.write(f"# Formato: ID|ADDRESS|TEXT\n")
            f.write(f"#\n")
            f.writelines(part_lines)
        
        print(f"  Parte {part_num}: strings_ES_part{part_num:02d}.txt ({len(part_lines)} líneas) - IDs {current_pos} a {end_pos - 1}")
        
        current_pos = end_pos
        part_num += 1
    
    remaining = total_lines - current_pos
    if remaining > 0:
        print(f"\n  [AVISO] Quedaron {remaining} líneas sin asignar")
    
    print(f"\n[OK] Creadas {part_num - 1} partes en: {output_path}")
    return part_num - 1


if __name__ == '__main__':
    # Total: 59,581 strings
    # Parte 1: 4,200 (como solicitaste)
    # Restante: 55,381
    # Partes de 5,000 cada una = 11 partes más + resto
    
    split_config = [
        4200,   # Parte 1 (como solicitaste)
        5000,   # Parte 2
        5000,   # Parte 3
        5000,   # Parte 4
        5000,   # Parte 5
        5000,   # Parte 6
        5000,   # Parte 7
        5000,   # Parte 8
        5000,   # Parte 9
        5000,   # Parte 10
        5000,   # Parte 11
        5000,   # Parte 12
        5381,   # Parte 13 (resto)
    ]
    
    split_strings(
        input_file=r"c:\Users\Abraham\Documents\Programacion\HoshiMemoHD_ESP\strings_ES_full.txt",
        output_dir=r"c:\Users\Abraham\Documents\Programacion\HoshiMemoHD_ESP\strings_ES_parts",
        split_sizes=split_config
    )
