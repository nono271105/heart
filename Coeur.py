import numpy as np
import matplotlib.pyplot as plt

# Paramètres pour l'équation du cœur
t = np.linspace(0, 2 * np.pi, 1000)

# Équations paramétriques pour un cœur
x = 16 * np.sin(t) ** 3
y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

# Tracé du graphique
plt.plot(x, y, color="red", lw=2)
plt.fill(x, y, color="red", alpha=0.5)  # Remplir le cœur avec une couleur rouge semi-transparente

# Personnalisation du graphique
plt.title("Cœur")
plt.xlabel("X")
plt.ylabel("Y")
plt.gca().set_aspect('equal', adjustable='box')  # Garder les proportions égales

# Afficher le graphique
plt.show()
