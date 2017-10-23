from sklearn import tree
"""Weight  Texture      Label
   150g	   Bumpy(0)	    Orange(1)
   170g	   Bumpy(0) 	Orange(1)
   140g	   Smooth(1)	Apple(0)
   130g	   Smooth(1)	Apple(0)"""
features = [[140,1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)
"""0 is an apple, 1 is an orange"""
print classifier.predict([[160, 0]])
