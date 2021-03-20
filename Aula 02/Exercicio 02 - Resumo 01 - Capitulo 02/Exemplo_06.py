import numpy as np
import matplotlib.pyplot as plt

women_pop = np.array([5., 30., 45., 22.])
men_pop = np.array([5., 25., 50., 20.])

X = np.arange(4)

plt.barh(X, women_pop, color = '#8be9fd', alpha=0.5, linestyle='dotted')
plt.barh(X, -men_pop, color = '#ffb86c', alpha=0.5)
plt.show()