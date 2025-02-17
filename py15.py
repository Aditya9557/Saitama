import numpy as np

arr = np.array([1,2,3,4,5,6,7,8,9])

print(arr)

even_numbers= arr[arr % 2 == 0]
print(even_numbers)

arr[ arr % 2 ! = 0]=-1

print(arr)
 
 
