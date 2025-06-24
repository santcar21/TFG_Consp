import pandas as pd
from tqdm import tqdm

def filter_by_hashtags(
    input_csv: str,
    hashtags_to_keep: list[str],
    output_csv: str = "filtered_consp_2019.csv"
):
    """
    Lee un CSV sin cabecera con columnas [id, hashtags],
    filtra filas que contengan al menos uno de los hashtags exactos
    en hashtags_to_keep, y guarda el resultado.
    """
    print(f"Leyendo archivo: {input_csv}")
    df = pd.read_csv(
        input_csv,
        header=None,
        names=['id', 'hashtags'],
        dtype=str,
        keep_default_na=False,
        quoting=0
    )
    
    keep_set = set(hashtags_to_keep)
    
    def has_any(tag_str: str) -> bool:
        tags = tag_str.split(',')
        return bool(set(tags) & keep_set)
    
    print("Filtrando filas...")
    mask = df['hashtags'].apply(has_any)
    filtered_df = df[mask]
    
    print(f"Total filas leídas: {len(df)}")
    print(f"Filas que coinciden: {len(filtered_df)}")
    
    filtered_df.to_csv(output_csv, index=False)
    print(f"Guardado en: {output_csv}")

if __name__ == "__main__":
    hashtags_to_keep = [
        "QAnon", "Qanon", "qanon", "QANON",
        "QAnon2019", "QAnon2018",
        "Q", "QArmy",
        "WWG1WGA", "wwg1wga",
        "MuellerGate", "TheGreatAwakening", "GreatAwakening",
        "ReadTheMuellerReport", "MuellerSpeaks",
        "WWG1WGAWORLDWIDE",
        "SaveTheChildren", "TrustThePlan",
        "Spygate", "SpyGate",
        "DarkToLight",
        "TREASON", "treason", "Treason",
        "FlatEarth",
        "BigPharma", "conspiracy", "occult",
        "DrainTheSwamp", "DeepState",
        "fraud",
        "DrainTheDeepState", "DrainTheDeepStateSwamp",
        "VoterFraud", "VoterID", "Fraud",
        "FakeNews", "fakenews", "FakeNewsMedia"
    ]
    
    filter_by_hashtags(
        input_csv="hashtags_2019.csv",
        hashtags_to_keep=hashtags_to_keep,
        output_csv="filtered_consp_2019.csv"
    )
