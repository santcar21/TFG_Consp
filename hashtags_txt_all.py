import pandas as pd
import os
from tqdm import tqdm

def parse_hashtag_list(s):
    """
    Convierte una cadena tipo "[tag1, 'tag2', \"tag3\"]" en lista de strings
    Funciona tanto si los elementos están entre comillas como si no.
    """
    s = str(s).strip().strip('[]')
    if not s:
        return []
    parts = s.split(',')
    hashtags = []
    for part in parts:
        h = part.strip().strip(' "\'')
        if h:
            hashtags.append(h)
    return hashtags


def analyze_hashtags_from_file(file_path="hashtags_2020.csv"):
    """
    Lee el CSV, analiza la frecuencia de todos los hashtags, y
    escribe en un .txt todos los hashtags sin límite de repeticiones.
    """
    print(f"Leyendo archivo: {file_path}")
    df = pd.read_csv(file_path)
    
    # Convertir la columna 'hashtags' a listas de strings
    df['hashtags'] = df['hashtags'].fillna('[]').apply(parse_hashtag_list)
    
    # Contar frecuencia de cada hashtag
    hashtag_counts = {}
    for hashtags in df['hashtags']:
        for tag in hashtags:
            hashtag_counts[tag] = hashtag_counts.get(tag, 0) + 1
    
    # Ordenar por frecuencia descendente
    sorted_hashtags = sorted(hashtag_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Mostrar resumen por consola
    print(f"\nTotal de tweets con hashtags: {len(df):,}")
    print(f"Total de hashtags únicos: {len(hashtag_counts):,}")
    print("\nTop 20 hashtags más frecuentes:")
    print("=" * 50)
    for tag, cnt in sorted_hashtags[:20]:
        print(f"#{tag}: {cnt:,} veces")
    
    # Preparar nombre de archivo de salida
    output_file = 'hashtags_extder_comparar.txt'
    try:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("Análisis de Hashtags (todas las apariciones)\n" + "="*50 + "\n\n")
            f.write(f"Total de tweets analizados: {len(df):,}\n")
            f.write(f"Total de hashtags únicos: {len(hashtag_counts):,}\n\n")
            f.write("Lista completa de hashtags ordenada por frecuencia:\n\n")
            
            print(f"\nEscribiendo {len(sorted_hashtags):,} hashtags en {output_file}")
            for tag, cnt in tqdm(sorted_hashtags, desc="Escribiendo hashtags"):
                try:
                    f.write(f"#{tag}: {cnt:,} veces\n")
                except Exception as e:
                    print(f"Error escribiendo #{tag}: {e}")
                    continue
        
        print(f"\nProceso completado. Hashtags escritos en {output_file}")
    
    except Exception as e:
        print(f"Error escribiendo el archivo: {e}")
        return
    
    # Verificar número de líneas escritas
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
            total_lines = sum(1 for _ in f)
        expected = len(sorted_hashtags) + 4  # líneas de encabezado y resumen
        print(f"\nTotal de líneas escritas en el archivo: {total_lines:,}")
        print(f"Total esperado de líneas: {expected:,}")
    except Exception as e:
        print(f"Error verificando el archivo: {e}")

if __name__ == "__main__":
    analyze_hashtags_from_file("hashtags_2020.csv")