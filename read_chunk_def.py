import re
import csv
from collections import defaultdict
import sys

# Rutas de entrada y salida
entrada = sys.argv[1]
salida = sys.argv[2]
# debug = sys.argv[3]

def debug_print(*args):
    if DEBUG_MODE:
        print(*args)

DEBUG_MODE = False  # Cambiar a False en producción
TOTAL_LINEAS = 5000000

# Expresiones regulares usando prefijos y re.search()
mention_re = re.compile(r'(_:[^\s]+)\s+schema:mentions\s+(_:[^\s]+)')  # Más específico para tags
tag_type_re = re.compile(r'(_:h\d+_\d+)\s+rdf:type\s+sioc_t:Tag[;\s.]')  # Formato exacto de tus tag
# tag_label_re = re.compile(
#     r'(_:h\d+_\d+)[\s\S]*?rdfs:label\s+"([^"]+)"'
# )
tag_label_re = re.compile(r'(_:h\d+_\d+)[\s\S]*?rdfs:label\s+"([^"]+)"')


# Estructuras para almacenar datos
tag_ids    = set()
tag_labels = {}
post_tags  = defaultdict(list)

print("Leyendo y extrayendo triples...")
total_lineas_leidas = 0
lineas = []

with open(entrada, encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        # lineas.append(linea)
        # # print(linea)
        # total_lineas_leidas += 1
        # if(total_lineas_leidas >= TOTAL_LINEAS):
        #     break
    
        m = tag_type_re.match(linea)
        if m:
            tag_ids.add(m.group(1))
        
        # ¿Es la etiqueta de un tag?
        m = tag_label_re.match(linea)
        if(m):
            # print("bingo!!!")
            # print(linea)
            if m.group(1) in tag_ids:
                tag_labels[m.group(1)] = m.group(2).strip()
                # print(tag_labels)
    f.close()

total_lineas_leidas = 0
lineas = []
with open(entrada, encoding="utf-8") as f:
    for linea in f:

        linea = linea.strip()
        # lineas.append(linea)
        # # print(linea)
        # total_lineas_leidas += 1
        # if(total_lineas_leidas >= TOTAL_LINEAS):
        #     break
         # ¿Un post menciona una entidad?
        m = mention_re.match(linea)
        if(m):
            # print("bingo!!!")
            # print(linea)
            if m.group(2) in tag_ids:
                post_id = m.group(1)
                tag_id = m.group(2)
                post_tags[post_id].append(tag_id)
    f.close()

    
print(f"Total tags identificados: {len(tag_ids)}")
print(f"Total labels capturados: {len(tag_labels)}")
print(f"Total mentions encontrados: {sum(len(v) for v in post_tags.values())}")

print(f"Exportando {len(post_tags)} posts con hashtags...")

# with open(debug, "w", newline="", encoding="utf-8") as out:
#     out.write("\n".join(lineas))

with open(salida, "w", newline="", encoding="utf-8") as out:
    writer = csv.writer(out)
    writer.writerow(["post_id", "hashtags"])
    for post_id, tags in post_tags.items():
        # Sustituye cada tag_id por su texto y únelos con comas
        etiquetas = [tag_labels[t] for t in tags if t in tag_labels]
        if etiquetas:
            writer.writerow([post_id, ",".join(etiquetas)])

print("Listo. Archivo generado:", salida)
