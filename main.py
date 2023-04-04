# Import des librairies
import matplotlib.pyplot as plt
from numpy import *

# Entrée de la fonction
fonction = str(input('entrez votre fonction: '))

# Création des abscisses
x = linspace(-5, 5, 1001)
g = linspace(-5, 5, 1001) * 0

# Liste contenant les valeurs de f(x)
y = []

# Variable servant à l'incrémentation pour une boucle
j = 0

# Calcul des valeurs de f(x) en fonction de ses particularités (trigonométrique et exponentielle)
for i in x:
    if 'tan' in fonction:
        if round(cos(i), 2) != 0:
            y.append(eval(fonction.replace('x', '(' + str(i) + ')')))
        else:
            y.append(nan)
    elif 'exp' in fonction:
        while j < len(fonction):
            if fonction[j] == 'x' and list(fonction)[j - 1] != 'e':
                fonction = list(fonction)
                fonction[j] = 'X'
                fonction = ''.join(fonction)
            else:
                pass
            j += 1
        try:
            y.append(eval(fonction.replace('X', '(' + str(i) + ')')))
        except:
            y.append(nan)
    else:
        try:
            y.append(eval(fonction.replace('x', '(' + str(i) + ')')))
        except:
            y.append(nan)

# Tracer de y = 0
plt.plot(x, g, color='b')
# Tracer de f(x)
plt.plot(x, y, color='black')
# Calcul des valeurs pour lesquels f(x) = 0 (méthode pour savoir pour quelles valeurs f(x) croise y = 0)
idx = argwhere(diff(sign(g - y))).flatten()
for i in idx:
    if isnan(float(str(y[i]))):
        idx = delete(idx, list(idx).index(i))
    elif 'tan' in fonction:
        if round(y[i], 1) != 0:
            idx = delete(idx, list(idx).index(i))
    elif round(y[i], 0) != 0:
        idx = delete(idx, list(idx).index(i))
# Tracer des racines de f(x)
plt.plot(x[idx],
         g[idx],
         marker=".",
         markersize=10,
         markeredgecolor="black",
         markerfacecolor="red")
# Setup des axes et titres
plt.title('f(' + str(fonction) + ')')
plt.grid(True)
plt.xlim(-5, 5)
plt.ylim(-5, 5)
ax = plt.gca()
ax.set_aspect('equal')
plt.ylabel("Ordonnées")
plt.xlabel("Abscisses")
# Sauvegarde de l'image de la fonction
plt.savefig("function.png")
plt.close()
