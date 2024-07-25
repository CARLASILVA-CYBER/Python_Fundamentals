import numpy as np

if __name__ == '__main__':
  a=np.array([[4,5,6], [3,8,7], ]2,0,9], [9,0,0], [3,2,1], [6,1,1]])
  for l in range(a.shape[0]):
          print("1", a[l] # 1)
  print ("2", a[3:5]) #2)
  print ("3", a[::2]) #3)
  print ("4", a[1::3]) #4)  
  print ("5", a[3::]) #5)
  print ("6", a[1][1::]) #6)
  ls=6
  b=a>ls
  print("7", b) #7)
  a[a>ls]=-1
  print("8",a) #8)
  
