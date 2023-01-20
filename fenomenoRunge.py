# importamos la interpolacion bericentrica del modulo de interpolacion de Scipy
# importamos la libreria Matplotlib con un alias
# importamos la libreria Numpy con un alias
from scipy.interpolate import barycentric_interpolate
import numpy as np
import matplotlib.pyplot as plt

# Aplicaremos la interpolacion baricentrica para a la funcion dada
def runge(x):
    """Funcion de Runge"""
    return 1 / (1 + x ** 2)

# Nodos de interpolacion
N = 11 
# linspace devuelve espacios numericos uniformemente
xp = np.linspace(-5,5,N)
fp = runge(xp)
x = np.linspace(-5,5,200)
y = barycentric_interpolate(xp, fp, x)

# Graficamos los polinomios obtenidos
plt.figure('1')
plt.plot(x,y, label='interpolacion')
plt.plot(xp, fp, 'x')
plt.plot(x, runge(x), label='funcion real')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper center')
plt.show()