import pandas as pd
import numpy as np
import random

#  Carica il CSV originale
df = pd.read_csv("harry_potter_1000_students.csv")

# Definizione nomi e cognomi
names = [
    "Alaric", "Isolde", "Theo", "Minerva", "Seraphina", "Kai", "Rowan", "Anya", "Lucien", "Jasper",
    "Freya", "Elio", "Zara", "Orion", "Thalia", "Dorian", "Nyx", "Leif", "Maia", "Silas",
    "Calliope", "Ezra", "Ines", "Ronan", "Lyra", "Soren", "Aurelia", "Kieran", "Cassia", "Bastian",
    "Ione", "Fenris", "Vera", "Caelum", "Amara", "Laziel", "Sorrel", "Talia", "Oswin", "Evander",
    "Caius", "Liora", "Mirek", "Eira", "Thorne", "Vesper", "Yara", "Bran", "Galen", "Nerissa"
]

families = {
    "Blackwood": 1000, "Ashcroft": 1000, "Rosenthal": 1000, "Moonvale": 1000, "Duskryn": 1000,
    "Frostbane": 1000, "Thorne": 1000, "Nightshade": 1000, "Ravenscar": 1000, "Graves": 1000,
    "Everbleed": 600, "Hawkwind": 600, "Stormrider": 500, "Emberlain": 500, "Duskwatch": 500,
    "Brightmoor": 500, "Shadowmere": 500, "Darkwater": 500, "Emberwyld": 500,
    "Whisperwind": 400, "Starcrest": 400, "Flintveil": 400, "Wyrmspire": 400, "Coldmarsh": 400,
    "Falconshade": 400, "Rookwood": 400, "Stoneveil": 400, "Stormholt": 300,
    "Thistledown": 300, "Ironhart": 300
}

#  Aumento le righe
extra = df.sample(20000 - len(df), replace=True, random_state=42).reset_index(drop=True)
df = pd.concat([df, extra], ignore_index=True)

#  Inserisco NaN casuali
def randomly_nullify(df, column, null_fraction):
    mask = np.random.rand(len(df)) < null_fraction
    df.loc[mask, column] = np.nan

for col in df.columns:
    randomly_nullify(df, col, 0.25)

#  Colonna 'id'
ids = list(range(1, 19991)) + random.sample(range(1, 19991), 10)
random.shuffle(ids)
df["id"] = ids

#  Colonna 'name'
df["name"] = [random.choice(names) if random.random() > 0.05 else np.nan for _ in range(20000)]

#  Colonna 'surname'
surname_pool = []
for s, n in families.items():
    surname_pool.extend([s] * n)
while len(surname_pool) < 20000:
    surname_pool.append(random.choice(list(families.keys())))
random.shuffle(surname_pool)
df["surname"] = [s if random.random() > 0.03 else np.nan for s in surname_pool]

#  Colonna 'age'
df["age"] = [random.randint(11, 18) if random.random() > 0.1 else np.nan for _ in range(20000)]


df.to_csv("harry_potter_students.csv", index=False)
