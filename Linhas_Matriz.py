import numpy as np
if __name__=="__main__":
    a=np.array([[1.4, 4., 2], [-2.,1.,1.]])
    for i in range(a.shape[0]):
      lm=max(abs(a[i]))
      a[i]=a[i]/lm
    print (a)
