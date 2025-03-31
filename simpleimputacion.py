def simpleinputacion(X,tipo):
  if(tipo==1):
    n=0
    suma=0
    for i in X:
      for j in i:
        if not(np.isnan(j)):
          n=n+1
          suma=suma+j
    media=suma//n
    for i in range(np.shape(X)[0]):
      for j in range(np.shape(X)[1]):
        if (np.isnan(X[i,j])):
          X[i,j]=media
  else:
    diferentes=[]
    lista=[]
    for i in X:
      for j in i:
        if not(np.isnan(j)):
          lista.append(j)
          if j not in diferentes:
            diferentes.append(j)
    max=0
    moda=0
    max2=0
    for i in diferentes:
      max2=lista.count(i)
      if(max2>max):
        max=max2
        moda=i
    for i in range(np.shape(X)[0]):
      for j in range(np.shape(X)[1]):
        if (np.isnan(X[i,j])):
          X[i,j]=moda
  return X
X = np.array([[1, 2, 5], [8, np.nan, 3], [7, 6, np.nan]])
Y = np.array([[1,3, 2], [3, np.nan, 1], [2, 2, np.nan]])
print(simpleinputacion(X,1))
print(simpleinputacion(Y,2))
