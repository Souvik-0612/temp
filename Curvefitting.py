import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 10, 14, 27])

def fit(x, a, b):
    return a * x**2 + b

popt, pcov = curve_fit(fit, x, y, [1, 0])

plt.plot(x, y, 'ro')
plt.plot(x, fit(x, *popt), 'b-')
plt.show()
print(np.diag(pcov))
