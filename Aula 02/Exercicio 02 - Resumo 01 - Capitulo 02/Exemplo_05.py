import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    
    return a * np.exp(b * (X - mu) ** 2)

X = np.linspace(-6, 6, 1024)

plt.plot(X, pdf(X, 0., 1.), color='red', linestyle='solid')
plt.plot(X, pdf(X, 0., .5), color='green', linestyle='dashed')
plt.plot(X, pdf(X, 0., .25), color='blue', linestyle='dashdot')

plt.show()
