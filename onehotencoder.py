from sklearn.preprocessing import OneHotEncoder
enc = OneHotEncoder(handle_unknown='ignore')
X = [['Male', 1], ['Female', 3], ['Female', 2]]
print("Elementos que crearemos por cada elemento diferente creara una nueva columna")
enc.fit(X)
print(enc.categories_)
print("Transformaremos cada elemento de entrada en un unico registro si no hay registro de un elemento entonces se coloca 0")
print(enc.transform([['Female', 1], ['Male', 4]]).toarray())
