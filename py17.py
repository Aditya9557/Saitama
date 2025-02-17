import numpy as np


matrix = np.arange(1, 17).reshape(4, 4)

np.fill_diagonal(matrix, 0)

matrix[matrix > 10] = 100

print(matrix)



Data ={
  'Name' : ['jhon','Alice','Bob','Female'],
  'Age' :[25,23,24,22],
  'Gender':['Male','Female','Male','Female'],
  'Marks':[85,90,75,95]
  
    }
