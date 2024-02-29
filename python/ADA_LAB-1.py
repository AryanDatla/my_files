# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 08:37:21 2024

@author: ARYAN DATLA
"""


#push zeroes at end--------------------------------------------------------
def push_zero(arr, n):
    
    count = 0
    
    for i in range(n):
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
            
    while(count < n):
        arr[count] = 0
        count += 1
        
#MAIN---------------------------------------
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 

n = len(arr)

push_zero(arr, n)

print(f"new array: {arr}")




#bubble sort---------------------------------------------------------------
def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        
        if not swapped:
            break

# MAIN--------------------------------------
arr = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
print(f"\nList before sorting: {arr}")

bubble_sort(arr)

print(f"\nList after sorting: {arr}")

#fibonacci series----------------------------------------------------------------------
def recursive_fibonacci(n):
  if n <= 1:
      return n
  else:
      return(recursive_fibonacci(n-1) + recursive_fibonacci(n-2))

#MAIN--------------------------------------------
n = 10
 
# check if the number of terms is valid
if n <= 0:
  print("Invalid input!")
  
else:
  print("Fibonacci series:")
  
for i in range(n):
    print(recursive_fibonacci(i))



