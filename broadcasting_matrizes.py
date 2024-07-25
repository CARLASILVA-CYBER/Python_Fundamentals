import numpy as np

if __name__ == '__main__':
  
    a=np.arange(1,25, 2).reshape(4,3)
    b=np.arange(1,11, 3).reshape(4,1)
    print("a+b\n", a+b)
