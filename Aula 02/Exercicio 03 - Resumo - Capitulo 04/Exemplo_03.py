import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 1024)

plt.ylim(-1.25, 1.25)

plt.plot(X, np.sinc(X), c = 'green', alpha = 0.5)
plt.show()