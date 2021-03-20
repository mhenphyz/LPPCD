import numpy as np
import matplotlib.pyplot as plt

N = 8
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)

plt.rcParams["patch.force_edgecolor"] = True

plt.bar(X, A, color = 'w', hatch = '*')
plt.bar(X, A + B, bottom = A, color = 'w', hatch = '+')

plt.show()