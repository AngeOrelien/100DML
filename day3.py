"""
    ------------------------------------------------------------------------------------------------------------
    100DML - Day 3: Manipulation de la Bibliotheque NUMPY
    ------------------------------------------------------------------------------------------------------------
    
    NumPy (Numerical Python) est une bibliothèque Python essentielle pour la manipulation de données numériques.
    Elle fournit des structures de données puissantes, telles que les tableaux multidimensionnels (ndarray),
    ainsi que des fonctions pour effectuer des opérations mathématiques et statistiques sur ces données.
    
    Voici quelques-unes des fonctionnalités clés de NumPy :
    - Tableaux multidimensionnels (ndarray) : NumPy permet de créer et de manipuler des tableaux multidimensionnels,
        qui sont plus efficaces que les listes Python pour le stockage et les opérations sur les données numériques.
    
    - Fonctions mathématiques : NumPy offre une large gamme de fonctions mathématiques pour effectuer des opérations
        sur les tableaux, telles que les fonctions trigonométriques, exponentielles, logarithmiques, etc.
    
    - Opérations sur les tableaux : NumPy permet d'effectuer des opérations élémentaires sur les tableaux, telles que
        l'addition, la soustraction, la multiplication, la division, etc., de manière efficace et rapide.
"""

import numpy as np

# Création d'un tableau NumPy à partir d'une liste Python
a = np.array([1, 2, 3, 4, 5])
print("Tableau a:", a)

# Création d'un tableau multidimensionnel
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Tableau b:\n\n", b)

# Création d'un tableau de zéros
c = np.zeros((4, 4))
print("Tableau c:\n\n", c)

# Création d'un tableau de un
d = np.ones((4, 4))
print("Tableau d:\n\n", d)

# Création de 0 a 9 a intervale de 2
e = np.arange(0, 10, 2)
print("Tableau e:\n\n", e)

# Création d'un tableau de 0 a 10 avec 5 nombres equidistants
f = np.linspace(0, 11, 5)
print("Tableau f:\n\n", f)

# Création d'une matrice avec des valeurs aleatoirs
g = np.random.random((4, 5))
print("Tableau g:\n\n", g)


"""
    Quelques fonctions utiles
    - np.sum()  : calcule la somme 
    - np.mean() : calcule la moyenne
    - np.std()  : calcule l'ecart type
    - np.sqrt() : calcule la racine carre
    - np.abs()  : calcule la valeur absolue
    - np.dot()  : calcule le produit scalaire de deux tableaux
    .
    .
    .
"""

