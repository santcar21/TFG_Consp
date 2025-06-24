import pandas as pd
from tqdm import tqdm

def filter_by_hashtags(
    input_csv: str,
    hashtags_to_keep: list[str],
    output_csv: str = "filtered_consp_2020.csv"
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
        "QAnons", "Qanons", "QAnon2020", "QAnon2018",
        "QanonArmy", "Qarmy", "QArmy", "Q", "q",
        "WWG1WGA", "WWG1WGAWORLDWIDE", "wwg1wga", "WWG1WGA_WORLDWIDE",
        "thegreatawakening", "TheGreatAwakening", "TheGreatAwakeningWorldwide",
        "GreatAwakeningWorldwide", "GreatAwakening",
        "SaveTheChildren", "savethechildren", "SavetheChildren",
        "TrustThePlan", "TheStormIsUponUs", "TheStormIsHere",
        "CrimesAgainstHumanity", "CrimesAgainstChildren",
        "DarkToLight", "DeepState", "DeepStateExposed",
        "deepstate", "DEEPSTATETAKEDOWN",
        "pizzagate", "PizzaGate", "PIZZAGATEISREAL",
        "Treason",
        "Agenda21", "Agenda2030", "Pedogate",
        "Spygate", "SpyGate",
        "conspiracy", "FlatEarth", "DrainTheSwamp",
        "VoterID", "VoterIDNow", "VoterFraud",
        "fraud", "Fraud",
        "FakeNews", "FakeNewsCNN", "FAKENEWS",
        "Fakenews", "CNNFakeNews", "FakeNewsMedia",
        "fakenews", "FakeNewsAlert",
        "CCPVirus", "CCPvirus", "CCP_is_terrorist",
        "CCPLiedPeopleDied", "ChinaVirus", "ChinaLiedAndPeopleDied",
        "BoycottChina", "boycott_china_mncs",
        "ChinaMustPay", "ChinaMustExplain", "Chinamustfall",
        "ChineseVirusCensorship", "ChineseVirus",
        "ChineseVirus19", "MakeChinaPay", "ChinaLiedPeopleDie",
        "ChinaLiedPeopleDied", "ChineseBioterrorism",
        "chinazi", "ChinaIsAsshoe",
        "ChineseCoronaVirus", "chinavirus", "ChineseVirusCensorship",
        "covidiots", "Covidiots", "COVIDIDIOT", "COVIDIDIOTS",
        "COVIDIOT", "COVIDIOTS", "SignsYoureACOVIDIOT",
        "FireFauci", "firefauci", "FauciFraud", "FauciThefraud",
        "Coronavirustruth", "Plandemic", "plandemic",
        "FilmYourHospital", "EmptyHospitals", "CoronaHoax",
        "Genocide", "genocide", "FakePandemic", "CoronaVirusHOAX",
        "FakeCases", "BillGatesIsEvil", "BillGatesVirus",
        "5GCoronavirus", "BillGatesBioTerrorist", "BillGatesIsNotOurFriend",
        "endthelockdown", "LockdownEnd", "endthelockdownnow",
        "BigPharma"
    ]
    
    filter_by_hashtags(
        input_csv="hashtags_2020.csv",
        hashtags_to_keep=hashtags_to_keep,
        output_csv="filtered_consp_2020.csv"
    )
