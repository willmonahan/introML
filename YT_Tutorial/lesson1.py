#hello world!
from sklearn import tree

features = [[140, 1], [130, 1], [150, 0], [170, 0]] #1 is smooth, 0 is bumpy
labels = [0, 0, 1, 1] #0 is apple, 1 is orange

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

newFeatures = [[160,0],[135,1]]
newFruit = clf.predict(newFeatures)

print(newFruit)
