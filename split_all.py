#!/usr/bin/env python3
"""
Script para dividir archivos de strings en Shift-JIS.
"""

from pathlib import Path

def split_strings(input_file: str, output_dir: str, split_sizes: list, prefix: str):
    input_path = Path(input_file)
    output_path = Path(output_dir)
    
    # Limpiar directorio existente
    if output_path.exists():
        for f in output_path.glob('*.txt'):
            f.unlink()
    output_path.mkdir(parents=True, exist_ok=True)
    
    # Leer en Shift-JIS
    with open(input_path, 'r', encoding='cp932') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    print(f"Total de strings: {total_lines}")
    print(f"Codificacion: Shift-JIS (CP932)")
    print()
    
    current_pos = 0
    part_num = 1
    
    for size in split_sizes:
        if current_pos >= total_lines:
            break
        
        end_pos = min(current_pos + size, total_lines)
        part_lines = lines[current_pos:end_pos]
        
        output_file = output_path / f"{prefix}{part_num:02d}.txt"
        
        # Escribir en Shift-JIS
        with open(output_file, 'w', encoding='cp932') as f:
            f.write(f"# Parte {part_num} - Lineas {current_pos + 1} a {end_pos}\n")
            f.write(f"# Total en esta parte: {len(part_lines)} strings\n")
            f.write(f"# Formato: ID|ADDRESS|TEXT\n")
            f.write(f"#\n")
            f.writelines(part_lines)
        
        print(f"  Parte {part_num}: {prefix}{part_num:02d}.txt ({len(part_lines)} lineas)")
        
        current_pos = end_pos
        part_num += 1
    
    # Crear build.txt en Shift-JIS
    build_file = output_path / "build.txt"
    with open(build_file, 'w', encoding='cp932') as f:
        f.write(f"# Build script para reconstruir\n")
        f.write(f"# Usar: python fvp_tools.py hcb-merge {output_path.name}/build.txt strings_merged.txt\n")
        f.write(f"#\n")
        for i in range(1, part_num):
            f.write(f"{output_path.name}/{prefix}{i:02d}.txt\n")
    
    print(f"\n[OK] Creadas {part_num - 1} partes en: {output_path}")


if __name__ == '__main__':
    base = r"c:\Users\Abraham\Documents\Programacion\HoshiMemoHD_ESP"
    
    # Hoshimemo_HD: 115,344 strings
    # Parte 1: 4,900 | Resto: partes de 10,000
    print("=== Hoshimemo_HD ===")
    split_strings(
        input_file=f"{base}\\strings_full.txt",
        output_dir=f"{base}\\strings_parts",
        split_sizes=[4900, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10000, 10444],
        prefix="strings_part"
    )
    
    print()
    
    # MemoriaES: 59,581 strings  
    # Parte 1: 4,200 | Resto: partes de 5,000
    print("=== MemoriaES ===")
    split_strings(
        input_file=f"{base}\\strings_ES_full.txt",
        output_dir=f"{base}\\strings_ES_parts",
        split_sizes=[4200, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5000, 5381],
        prefix="strings_ES_part"
    )
