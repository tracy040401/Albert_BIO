import re


def opti_labels(input_file):
    # Lecture du fichier
    with open(input_file, "r") as file:
        data = file.read()

    # Unification des "loc"
    data = re.sub(r"(fromloc\.|toloc\.|stoploc\.)", "loc.", data)
    # Suppression des détails de départ et arrivée
    data = re.sub(r"(depart_|arrive_)", "", data)

    # Ecriture des modifs ds nouveau fichier
    with open("CRF/atis.train", "w") as file:
        file.write(data)


def add_airlines(input_file):
     # Liste des compagnies aériennes aux États-Unis (pas déjà présente dans le fichier)
    compagnies_aeriennes = [
        "allegiant","spirit","paklook","jetblue","frontier","alaska","southwest","breeze",
        "breeze-airways","avelo","linear","contour","hawaiian","sun-country","denver-air-connection","cape","boutique","ravn","ravn-alaska",
        "southern-airways-express","southern-airways","silver","silver-airways","air-choice-one","air-choice","advanced","grant-aviation","tradewind"
    ]

    with open(input_file, 'a') as f_cible:
        # Ajoute une ligne pour chaque compagnie aérienne dans le fichier cible
        f_cible.write("\n")
        for compagnie in compagnies_aeriennes:
            f_cible.write(f"{compagnie}\tB-airline_name\n")
            f_cible.write(f"{compagnie}-air\tB-airline_name\n")
            f_cible.write(f"{compagnie}-airline\tB-airline_name\n")
            f_cible.write(f"{compagnie}-airlines\tB-airline_name\n")
            f_cible.write(f"{compagnie}'s\tB-airline_name\n")


def add_cities(input_file):
    # Liste des villes ayant des aéroports aux Etats-Unis pas présente dans le fichier
    cities = [
        "birmingham", "huntsville", "tucson", "carlsbad", "fresno", "monterey", "monterey-peninsula", "palm-springs", "sacramento",
        "san-luis", "san-luis-obispo", "santa-ana", "santa-barbara", "greensboro", "greenville", "raleigh", "raleih-durham", "charleston",
        "hartford", "hartford-bradley", "hector", "jacksonville", "west-palm", "west-palm-beach", "savannah", "honolulu", "kahului", "boise",
        "moline", "peoria", "cedar", "cedar-rapids", "kansas", "wichita", "lexington", "louisville", "new-orleans", "portland", "grand-rapids",
        "rochester", "jackson-medgar", "billings", "lincoln", "omaha", "reno", "albany", "buffalo", "syracuse", "albuquerque", "columbus", "dayton",
        "oklahoma", "tulsa", "jackson", "madison", "spokane", "pasco", "des-moines", "austin", "el-paso", "lubbock", "san-antonio", "burlington",
        "norfolk", "richmond", "eugene", "rogue", "rogue-valley", "harrisburg", "pittsburgh", "knoxville"
     ]

    with open(input_file, 'a') as f_cible:
    # Ajoute une ligne pour chaque compagnie aérienne dans le fichier cible
        f_cible.write("\n")
        for city in cities:
            f_cible.write(f"{city}\tB-loc.city_name\n\n")

def add_main_code_air(input_file):
    # Liste des principaux code d'aéroport (pas forcément dans le fichier)
    airports = [
        "mia", "iad", "atl", "bos", "las", "msy","sea","iah","san","hnl","fll","den","phx","dtw","phl","tpa","dca","msp","clt","rsw",
        "rdu","aus"
    ]

    with open(input_file, 'a') as f_cible:
        # Ajoute une ligne pour chaque compagnie aérienne dans le fichier cible
        f_cible.write("\n")
        for airp in airports:
            f_cible.write(f"{airp}\tB-loc.airport_code\n\n")

def add_states(input_file):
    # Liste des états des USA
    states = [
        "alabama", "alaska", "arizona", "arkansas", "california", "colorado", "connecticut", "delaware", "florida", "georgia",
        "hawaii", "idaho", "illinois", "indiana", "iowa", "kansas", "kentucky", "louisiana", "maine", "maryland", "massachusetts",
        "michigan", "minnesota", "mississippi", "missouri", "montana", "nebraska", "nevada", "new-hampshire", "new-jersey",
        "new-mexico", "new-york", "north-carolina", "north-dakota", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode-island",
        "south-carolina", "south-dakota", "tennessee", "texas", "utah", "vermont", "virginia", "washington", "west-virginia",
        "wisconsin", "wyoming"
    ]

    with open(input_file, 'a') as f_cible:
        # Ajoute une ligne pour chaque état
        f_cible.write("\n")
        for state in states:
            f_cible.write(f"{state}\tB-loc.state_name\n\n")

def add_states_code(input_file):
    # Liste des états des USA (codes)
    codes = [
        "al", "ak", "az", "ar", "ca", "co", "ct", "de", "fl", "ga", "hi", "id", "il", "in", "ia", "ks", "ky", "la", "me", "md",
        "ma", "mi", "mn", "ms", "mo", "mt", "ne", "nv", "nh", "nj", "nm", "ny", "nc", "nd", "oh", "ok", "or", "pa", "ri", "sc",
        "sd", "tn", "tx", "ut", "vt", "va", "wa", "wv", "wi", "wy"
]

    with open(input_file, 'a') as f_cible:
        # Ajoute une ligne pour chaque code d'état
        f_cible.write("\n")
        for state in codes:
            f_cible.write(f"{state}	B-loc.state_code\n")



if __name__ == "__main__":
    input_file = "CRF/atisBase.train"
    opti_labels(input_file)
    target = "CRF/atis.train"
   # add_airlines(target)
   # add_cities(target)
    add_main_code_air(target)
    add_states(target)
    add_states_code(target)