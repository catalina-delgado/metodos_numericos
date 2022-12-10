# importamos la interpolación bericéntrica del módulo de interpolación de Scipy
# importamos la librería Matplotlib con un alias
# importamos la librería Numpy con un alias
from scipy.interpolate import barycentric_interpolate
import numpy as np
import matplotlib.pyplot as plt

# Aplicaremos la interpolación baricéntrica para a la función dada
def runge(x):
    """Funcion de Runge"""
    return 1 / (1 + x ** 2)

# Nodos de interpolación
N = 11 
# linspace devuelve espacios numéricos uniformemente
xp = np.linspace(-5,5,N)
fp = runge(xp)
x = np.linspace(-5,5,200)
y = barycentric_interpolate(xp, fp, x)

# Graficamos los polinomios obtenidos
plt.figure('1')
plt.plot(x,y, label='interpolación')
plt.plot(xp, fp, 'x')
plt.plot(x, runge(x), label='función real')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper center')
plt.show()