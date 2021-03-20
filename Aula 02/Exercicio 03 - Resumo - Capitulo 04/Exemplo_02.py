import numpy as np
import matplotlib.pyplot as plt

T = np.linspace(0, 2 * np.pi, 1024)

plt.plot(2. * np.cos(T), np.sin(T), c = 'k', lw = 3.)
plt.axes().set_aspect('equal')

plt.show()