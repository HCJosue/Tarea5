from sklearn.preprocessing import LabelBinarizer
lb = LabelBinarizer()
X=[1, 2, 6, 4, 2]
lb.fit(X)
print("Los elemento para clasificar")
print(X)
print("Las clases")
print(lb.classes_)
print("Clasifica")
print(lb.transform([1, 6]))
