import numpy as np

arr = np.array([10,20,30,40,50])
indices = [0,2,4]

print(arr[indices])

arr[[1,3]] = 99

print(arr)
