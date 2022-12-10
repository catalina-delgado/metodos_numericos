# importamos la interpolaci�n beric�ntrica del m�dulo de interpolaci�n de Scipy
# importamos la librer�a Matplotlib con un alias
# importamos la librer�a Numpy con un alias
from scipy.interpolate import barycentric_interpolate
import numpy as np
import matplotlib.pyplot as plt

# Aplicaremos la interpolaci�n baric�ntrica para a la funci�n dada
def runge(x):
    """Funcion de Runge"""
    return 1 / (1 + x ** 2)

# Nodos de interpolaci�n
N = 11 
# linspace devuelve espacios num�ricos uniformemente
xp = np.linspace(-5,5,N)
fp = runge(xp)
x = np.linspace(-5,5,200)
y = barycentric_interpolate(xp, fp, x)

# Graficamos los polinomios obtenidos
plt.figure('1')
plt.plot(x,y, label='interpolaci�n')
plt.plot(xp, fp, 'x')
plt.plot(x, runge(x), label='funci�n real')
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper center')
plt.show()