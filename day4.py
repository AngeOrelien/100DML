"""
    ------------------------------------------------------------------------------------------------------------
    100DML - Day 4: Manipulation de la Bibliotheque PANDAS
    ------------------------------------------------------------------------------------------------------------
    
    Pandas est une bibliothèque Python très populaire pour la manipulation et l'analyse de données. Elle offre 
    des structures de données flexibles et puissantes, telles que les DataFrames, qui facilitent le travail avec
    des données tabulaires.
"""

import pandas as pd

# Creation d'un DataFrame à partir d'un dictionnaire
myDict = {
    "name": ["Ange", "Flora", "Andy", "Sophie"],
    "age": [25, 30, 22, 28],
    "city": ['Yaounde', 'Douala', 'Yaounde', 'Bafoussam'],
    'job': ['Data Scientist', 'Data Analyst', 'Data Engineer', 'Data Scientist']  
}

df = pd.DataFrame(myDict)
print(df)

# Affichage des 2 premières lignes du DataFrame
print(df.head(2))

# Affichage des 2 dernières lignes du DataFrame
print(df.tail(2))

# Affichage de la colonne 'name'
print(df['name'])

# Affichage des colonnes 'name' et 'age'
print(df[['name', 'age']])

# Affichage des lignes où l'âge est supérieur à 25
print(df[df['age'] > 25])

# Affichage du type de données de chaque colonne
print(df.dtypes)

# Affichage des statistiques descriptives du DataFrame
# Cela inclut des mesures telles que la moyenne, l'écart-type, les valeurs minimales et maximales, etc.
print(df.describe())

# Affichage du nombre de valeurs uniques dans la colonne 'job'
print(df['job'].nunique())

# Affichage des colonnes du DataFrame
print(df.columns)

# Affichage de la forme du DataFrame (nombre de lignes et de colonnes)
print(df.shape)