from sklearn import datasets

iris = datasets.load_iris()

print(type(iris))
print(iris)
print(iris.data)

print(iris.target)
print(iris.target_names)