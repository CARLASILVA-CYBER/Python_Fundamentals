# _*_coding: UTF-8 -*
if __name__ == '__main__':
  X=[20,10,20,15,20,20,17,20,20,20,89,20]
  E=20
  i=0
  while i<len(X):
    if X[i]==E:
        X.remove(X[i])
    else: i+=1
  print(X)
