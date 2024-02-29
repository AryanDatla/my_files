# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 00:00:28 2024

@author: ARYAN DATLA

A list is a data structure in python used to store homogeneous elements. It is mutable, i.e.,
we can add, remove and manipulate the elements as per our requirement
It can be cloned by various methods, like copy() or throught iteration or list comprehensions.
Each element is individually accesible using their correct index starting from 0.
It also supports negetive idexing, i.e., the last elements can be accesed from from both front and last,
eg: print(nums[::-1]) prints the list in reverse order, 
simillarly we can access each element using either it's positive or negetive index
"""


from operator import length_hint


nums = [1, 2, 3, 5, 7, 3]

nums.append(9)#appending at end

nums.insert(3, 4)#inserting elemnt at specific index (index, element)
print (nums)

nums.remove(7)#deleting a particular element
print(nums)

# nums.clear()#emptying the list
# print(nums)

nums.pop()#remove last element
print(nums)

print("index of 5 is: ", nums.index(5))

#in operator generates a boolean value when used for checking
print(50 in nums) 

print(f"3 occurs {nums.count(3)} times in nums")#counting the occurene of an element

#sorting the list
nums.sort()
print(f"sorted list:{nums}")

nums.reverse()#reversing the list
print(nums)

numbers = nums.copy()#creating a copy of original list
print(f"this is a copy of nums: {numbers}")

#slicing 
# <name of list>[Intial : End : Step]
print(nums[1:6:1])


#QUESTIONS--------------------------------------------------------------------------------------------------

# removing duplicates from a list

nums = [1, 2, 3, 5, 7, 3]

unique_nums = []
for i in nums:
    if(i not in unique_nums):
        unique_nums.append(i)
        
print(f"edited list: {unique_nums}")      


#swapping first and last elements
temp = nums[0]
nums[0] = nums[-1]
nums[-1] = temp

print(nums)  


#swapping any two elements
a = int(input("enter the first number:"))
b = int(input("enter the second number"))

index_a = nums.index(a)
index_b = nums.index(b)

nums[index_a], nums[index_b] = nums[index_b], nums[index_a]
print(f"nums after swapping: {nums}")

#ways to find length of a list

#1: len(<name of object>) method
print(len(nums))

#2: iteration
count = 0

for i in nums:
    count += 1
    
print(count)

#3: length_hint(<name of object>) method present in operator class
length = length_hint(nums)

print(length)

#4: sum() and list comprehension method
length = sum(1 for i in nums)

print(length)

#5: enumerate() method
count = 0
for i, a in enumerate(nums):
    count += 1
print(count)



# pushing zeroes at the end of a list

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


#check if element exists in a list

#1: using 'in':
n = int(input("eneter number to be searched"))
print(n in nums)

#2: iteration:
for i in nums:
    if n == i:
        print(f"element found at index {nums.index(n)}")
        
#3: using enumerate():   
n = int(input("eneter number to be searched"))
for index, value in enumerate(nums):
    if n == value:
        print(f"element found at {index}")

#reversing a list

#1: using reverse() method
nums.reverse()
print(nums)

#2: slicing
print(nums[::-1])

#3: two-pointer technique and swapping
beg = 0
end = len(nums)-1

while(beg < end):
    #swap
    nums[beg], nums[end] = nums[end], nums[beg]
    beg += 1
    end -= 1 
print(arr)    

