"""
    ------------------------------------------------------------------------------------------------------------
    100DML - Day 5: Manipulation de la Bibliotheque MATPLOTLIB
    ------------------------------------------------------------------------------------------------------------
    
    Matplotlib est une bibliothèque Python très populaire pour la création de graphiques et de visualisations de données. Elle offre 
    des outils puissants pour créer des graphiques 2D et 3D, des histogrammes, des diagrammes en barres, etc.
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000) # Génère 1000 points entre 0 et 10
y = np.exp(x) # Calcule l'exponentielle de chaque point de x

plt.plot(x, y) # Trace la courbe de y en fonction de x
plt.show() # Affiche le graphique