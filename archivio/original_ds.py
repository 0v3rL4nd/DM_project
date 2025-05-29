import pandas as pd

# Carica il dataset
df = pd.read_csv("../harry_potter_students.csv")

# Trova tutte le colonne che contengono il nome della casa
house_columns = [col for col in df.columns if any(house in col.lower() for house in ["hufflepuff", "gryffindor", "slytherin", "ravenclaw"])]

# Verifica che abbia trovato le colonne corrette
print("Colonne identificate come 'house':", house_columns)

# Crea la colonna 'house' con il nome della casa in base al valore massimo (1)
df["house"] = df[house_columns].idxmax(axis=1).str.extract(r'(hufflepuff|gryffindor|slytherin|ravenclaw)', expand=False).str.lower()

# Rimuovi le vecchie colonne booleane
df.drop(columns=house_columns, inplace=True)

# Salva il file
df.to_csv("harry_potter_students_with_house_column.csv", index=False)

print("✅ Colonna 'house' creata correttamente!")
