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
print("\n\nAffichage des 2 premières lignes du DataFrame\n", df.head(2))

# Affichage des 2 dernières lignes du DataFrame
print("\n\nAffichage des 2 dernières lignes du DataFrame\n", df.tail(2))

# Affichage de la colonne 'name'
print("\n\nAffichage de la colonne 'name'\n", df['name'])

# Affichage des colonnes 'name' et 'age'
print("\n\nAffichage des colonnes 'name' et 'age'\n", df[['name', 'age']])

# Affichage des lignes où l'âge est supérieur à 25
print("\n\nAffichage des lignes où l'âge est supérieur à 25\n", df[df['age'] > 25])

# Affichage du type de données de chaque colonne
print("\n\nAffichage du type de données de chaque colonne\n", df.dtypes)

# Affichage des statistiques descriptives du DataFrame
# Cela inclut des mesures telles que la moyenne, l'écart-type, les valeurs minimales et maximales, etc.
print("\n\nAffichage des statistiques descriptives du DataFrame\n", df.describe())

# Affichage du nombre de valeurs uniques dans la colonne 'job'
print("\n\nAffichage du nombre de valeurs uniques dans la colonne 'job'\n", df['job'].nunique())

# Affichage des valeurs uniques dans la colonne 'job'
print("\n\nAffichage du nombre de valeurs uniques dans la colonne 'job'\n", df['job'].unique())

# Affichage des colonnes du DataFrame
print("\n\nAffichage des colonnes du DataFrame\n", df.columns)

# Affichage de la forme du DataFrame (nombre de lignes et de colonnes)
print("\n\nAffichage de la forme du DataFrame (nombre de lignes et de colonnes)\n", df.shape)



# Creer un Dataframe avec un ficher csv
myDF = pd.read_csv('datas/etudiants.csv', sep=',')
print(myDF)

# Afficher le premier element sous forme d'objet
print("\n\nAfficher le premier element sous forme d'objet\n", myDF.loc[0])

# # Definir l'index du tableau
# myDF.set_index(['Nom'])
# print("\n\n", myDF)