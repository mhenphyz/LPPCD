import numpy as np
import matplotlib.pyplot as plt

def pdf(X, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (X - mu) ** 2)

X = np.linspace(-6, 6, 1024)

for i in range(64):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    
    plt.plot(X, pdf(X, mu, sigma), color = '.75', linewidth = .5)

plt.plot(X, pdf(X, 0., 1.), color = 'b', linewidth = 3.)

plt.show()