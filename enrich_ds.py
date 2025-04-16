import pandas as pd
import numpy as np
import random

# Carica il dataset originale
df = pd.read_csv("harry_potter_students_20000.csv")

# --- Nomi eterogenei ---
names = [
    "Alaric", "Isolde", "Theo", "Minerva", "Seraphina", "Kai", "Rowan", "Anya", "Lucien", "Jasper",
    "Freya", "Elio", "Zara", "Orion", "Thalia", "Dorian", "Nyx", "Leif", "Maia", "Silas",
    "Calliope", "Ezra", "Ines", "Ronan", "Lyra", "Soren", "Aurelia", "Kieran", "Cassia", "Bastian",
    "Ione", "Fenris", "Vera", "Caelum", "Amara", "Laziel", "Sorrel", "Talia", "Oswin", "Evander",
    "Caius", "Liora", "Mirek", "Eira", "Thorne", "Vesper", "Yara", "Bran", "Galen", "Nerissa"
]

# --- Cognomi (casate) fantasy e potenti ---
families = {
    "Blackwood": 1000,
    "Ashcroft": 1000,
    "Rosenthal": 1000,
    "Moonvale": 1000,
    "Duskryn": 1000,
    "Frostbane": 1000,
    "Thorne": 1000,
    "Nightshade": 1000,
    "Ravenscar": 1000,
    "Graves": 1000,
    "Everbleed": 600,
    "Hawkwind": 600,
    "Stormrider": 500,
    "Emberlain": 500,
    "Duskwatch": 500,
    "Brightmoor": 500,
    "Shadowmere": 500,
    "Darkwater": 500,
    "Emberwyld": 500,
    "Whisperwind": 400,
    "Starcrest": 400,
    "Flintveil": 400,
    "Wyrmspire": 400,
    "Coldmarsh": 400,
    "Falconshade": 400,
    "Rookwood": 400,
    "Stoneveil": 400,
    "Stormholt": 300,
    "Thistledown": 300,
    "Ironhart": 300
}

# --- Generazione delle colonne ---

# ID con pochi duplicati
unique_ids = list(range(1, 19991))  # 19990 unici
duplicates = random.sample(unique_ids, 10)
ids = unique_ids + duplicates
random.shuffle(ids)

# Nomi con alcuni null
name_column = [random.choice(names) if random.random() > 0.05 else np.nan for _ in range(20000)]

# Cognomi: popoliamo il pool secondo le famiglie
surname_pool = []
for surname, count in families.items():
    surname_pool.extend([surname] * count)
while len(surname_pool) < 20000:
    surname_pool.append(random.choice(list(families.keys())))
surname_pool = surname_pool[:20000]
surname_column = [s if random.random() > 0.03 else np.nan for s in surname_pool]

# Età da 11 a 18 con alcuni null
age_column = [random.randint(11, 18) if random.random() > 0.1 else np.nan for _ in range(20000)]

# --- Aggiunta colonne al DataFrame ---
df["id"] = ids
df["name"] = name_column
df["surname"] = surname_column
df["age"] = age_column

# Salva il nuovo dataset
df.to_csv("harry_potter_students_enriched.csv", index=False)

print("✅ Dataset arricchito salvato come 'harry_potter_students_enriched.csv'")
