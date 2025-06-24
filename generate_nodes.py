import pandas as pd

# Carga del CSV original
df = pd.read_csv('filtered_consp_2020.csv')

# Listas de hashtags por categoría
alt_right_list = [
    "MAGA", "MAGA2020", "maga", "KAG", "KAG2020",
    "Trump2020", "Trump", "TRUMP2020", "Trump2020Landslide",
    "Trump2020NowMoreThanEver", "TrumpPressBriefing", "DonaldTrump",
    "Patriots", "PatriotStrikeTeam", "PatriotsFight", "PatriotsAwakened",
    "PatriotsUnited", "DemocratsHateAmerica", "Democrats",
    "DemocratsAreDestroyingAmerica", "WakeUpAmerica", "SaveAmerica",
    "VoteRedToSaveAmerica", "DrainTheSwamp", "AmericaFirst", "WalkAway",
    "FakeNewsCNN", "CNNFakeNews"
]

qanon_list = [
    "QAnon", "Qanon", "qanon", "QANON", "QAnons", "Qanons",
    "QAnon2020", "QAnon2018", "QanonArmy", "Qarmy", "QArmy",
    "Q", "q", "WWG1WGA", "WWG1WGAWORLDWIDE", "wwg1wga",
    "WWG1WGA_WORLDWIDE", "thegreatawakening", "TheGreatAwakening",
    "TheGreatAwakeningWorldwide", "GreatAwakeningWorldwide",
    "GreatAwakening", "SaveTheChildren", "savethechildren",
    "SavetheChildren", "TrustThePlan", "TheStormIsUponUs",
    "TheStormIsHere", "CrimesAgainstHumanity", "CrimesAgainstChildren"
]

otras_list = [
    "DarkToLight", "DeepState", "DeepStateExposed", "deepstate",
    "DEEPSTATETAKEDOWN", "pizzagate", "PizzaGate", "PIZZAGATEISREAL",
    "Treason", "Agenda21", "Agenda2030", "Pedogate",
    "Spygate", "SpyGate", "conspiracy", "FlatEarth"
]

politica_list = [
    "DrainTheSwamp", "VoterID", "VoterIDNow", "VoterFraud",
    "fraud", "Fraud"
]

fakenews_list = [
    "FakeNews", "FakeNewsCNN", "FAKENEWS", "Fakenews",
    "CNNFakeNews", "FakeNewsMedia", "fakenews", "FakeNewsAlert"
]

covid_list = [
    "CCPVirus", "CCPvirus", "CCP_is_terrorist", "CCPLiedPeopleDied",
    "ChinaVirus", "ChinaLiedAndPeopleDied", "BoycottChina",
    "boycott_china_mncs", "ChinaMustPay", "ChinaMustExplain",
    "Chinamustfall", "ChineseVirusCensorship", "ChineseVirus",
    "ChineseVirus19", "MakeChinaPay", "ChinaLiedPeopleDie",
    "ChinaLiedPeopleDied", "ChineseBioterrorism", "chinazi",
    "ChinaIsAsshoe", "ChineseCoronaVirus", "chinavirus",
    "covidiots", "Covidiots", "COVIDIDIOT", "COVIDIDIOTS",
    "COVIDIOT", "COVIDIOTS", "SignsYoureACOVIDIOT", "FireFauci",
    "firefauci", "FauciFraud", "FauciThefraud", "Coronavirustruth",
    "Plandemic", "plandemic", "FilmYourHospital", "EmptyHospitals",
    "CoronaHoax", "Genocide", "genocide", "FakePandemic",
    "CoronaVirusHOAX", "FakeCases", "BillGatesIsEvil", "BillGatesVirus",
    "5GCoronavirus", "BillGatesBioTerrorist", "BillGatesIsNotOurFriend",
    "endthelockdown", "LockdownEnd", "endthelockdownnow", "BigPharma"
]

# Función para asignar la categoría adecuada
def assign_category(tag):
    if tag in alt_right_list:
        return 'AltRight'
    elif tag in qanon_list:
        return 'QANON'
    elif tag in otras_list:
        return 'OTRaS'
    elif tag in politica_list:
        return 'POLITICa'
    elif tag in fakenews_list:
        return 'FAKE NEWS'
    elif tag in covid_list:
        return 'teoriasconspCOVID'
    else:
        return 'otros'

# Extraer y contar todos los hashtags
all_tags = (
    df['hashtags']
      .dropna()
      .str.split(',')   # Asumiendo que están separados por comas
      .explode()
      .str.strip()
)
counts = all_tags.value_counts()

# Construir el DataFrame de nodos
nodes = pd.DataFrame({
    'Id': range(1, len(counts) + 1),
    'Label': ['#' + tag for tag in counts.index],
    'Category': [assign_category(tag) for tag in counts.index],
    'Weight': counts.values
})

# Guardar el CSV listo para Gephi
nodes.to_csv('nodes_for_gephi_altright.csv', index=False)
print("Archivo 'nodes_for_gephi_altright.csv' generado correctamente.")
