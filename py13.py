import numpy as np

arr = np.array([[10,20,30,],[40,50,60],[70,80,90]])
# access the element in the secound row and third coloum.
print(arr)
print(arr[1,2])
print(0)
print(arr[:,-1])
arr[:,1]=0
print(arr)
