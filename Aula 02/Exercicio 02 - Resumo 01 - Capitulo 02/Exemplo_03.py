import numpy as np
import matplotlib.pyplot as plt

label_set = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica',
)

def read_label(label):
    return label_set.index(label)

data = np.loadtxt('iris.data',
delimiter = ',',
converters = { 4 : read_label })

color_set = ('.00', '.50', '.75')
color_list = [color_set[int(label)] for label in data[:,4]]

plt.scatter(data[:,0], data[:,1], color = color_list)
plt.show()
