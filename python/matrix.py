# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 21:13:51 2024

@author: ARYAN DATLA
"""
import numpy as np

# matrix = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
#     ]

# n = len(matrix)

# #printing a matrix
# for i in matrix:
#     print(i)

# #transpose of a matrix
# for i in range(n):
#     for j in range(n):
#         print(f'[ {matrix[j][i]} ]')
#     print()


#matrix using numPy


#---Method: 1---
a = np.array([ 
    [1,2,4], 
    [2,4,3], 
    [1,0,9] 
    ])
for i in a:
    print(i)
    
print()

#---Method: 2---
b = np.arange(1, 10)
print(b)

print()
    

#---Method: 3---
c = np.array([ 
    [np.arange(1, 4)], 
    [np.arange(1, 4)], 
    [np.arange(1, 4)] 
    ])
for i in c:
    print(i)
print()
    
#---Method: 4---(didn't werk as expected)
d = np.arange(1,10)
d.reshape(3,3)#should convert d in matrix form
for i in d:
    print(i)
    
    

