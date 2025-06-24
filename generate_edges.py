import pandas as pd
from itertools import combinations

# Carga del CSV original
df = pd.read_csv('filtered_consp_2019.csv')

# División y limpieza de hashtags por tweet
hashtags_per_tweet = (
    df['hashtags']
    .dropna()
    .str.split(',')
    .apply(lambda tags: [t.strip() for t in tags] if isinstance(tags, list) else [])
)

# Contar co-ocurrencias de pares de hashtags (sin dirección)
edge_counts = {}
for tags in hashtags_per_tweet:
    unique_tags = list(dict.fromkeys(tags))  # elimina duplicados en el mismo tweet
    if len(unique_tags) > 1:
        for tag1, tag2 in combinations(unique_tags, 2):
            pair = tuple(sorted((tag1, tag2)))
            edge_counts[pair] = edge_counts.get(pair, 0) + 1

# Construir DataFrame de aristas
edges = pd.DataFrame(
    [(f'#{t1}', f'#{t2}', w) for (t1, t2), w in edge_counts.items()],
    columns=['Source', 'Target', 'Weight']
)

# Guardar CSV para Gephi
edges.to_csv('edges_for_gephi_2019.csv', index=False)
print("Archivo 'edges_for_gephi_2019.csv' generado correctamente.")