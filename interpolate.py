import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline

x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 4, 10, 14, 27])

x_smooth = np.linspace(x.min(), x.max(), 300)
spl = make_interp_spline(x, y, k=3)
y_smooth = spl(x_smooth)

plt.scatter(x, y)
plt.plot(x_smooth, y_smooth)
plt.show()
