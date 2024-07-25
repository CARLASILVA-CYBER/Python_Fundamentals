import numpy as np
if __name__=="__main__":
  vetor=np.array([2,5.2,7.8,9])
  MultPortEscalar=7.8*vetor
  print(MultPortEscalar)
  print(vetor.shape)
  matriz=np.array([
  [2,0,4,8],
  [4,5,7,9],
  [2,3,5,0]])
  print(matriz.shape)
  print(matriz)
  a=matriz
  b=np.array([[1,0,5,7], [2,4,0,1], [3,0,0,4]])
  print(a*b)
  print(a+b)
  print(a-b)
  c=np.array([[1,0], [2,4], [3,0], [0,1]])
  print (np.dot(a,c))
  d=np.array([[1,2], [3,4]])
  print (round(np.linalg.det(d),2))
