import numpy as np

arr = np.array([5, 10, 15, 20, 25])  # Original array

arr *= 2  # Multiply by 2
print(arr)
arr[arr > 10] = 99  # Replace values greater than 10 with 99
print(arr)
arr += 50  # Add 50 to every element

print(arr)


