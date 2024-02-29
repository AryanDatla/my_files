# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 12:46:20 2024

@author: ARYAN DATLA
"""
import time

# PROGRAM - 1
print("Hello, World!")

time.sleep(1.5)

# print(Hello) - gives error

print(5)
time.sleep(1.5)

n = int(input("enter an integer: "))
list = []
for i in range(1,n+1):
    print(i, end='')
time.sleep(1.5)

print("My name is Khan. \nI'm a superstar!")

time.sleep(1.5)

# PROGRAM - 2
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
time.sleep(1.5)

print(f"Sum of {a} & {b} is {a+b}")
time.sleep(1)

print(f"Subtraction of {a} & {b} is {a-b}")
time.sleep(1)

print(f"Multiplication of {a} & {b} is {a*b}")
time.sleep(1)

print(f"Division of {a} & {b} is {a/b}")
time.sleep(1.5)


# PROGRAM - 3: AREA OF TRIANGLE
import math

A = float(input("enter length of first side: "))
B = float(input("enter length of second side: "))
C = float(input("enter length of first side: "))

S = (A+B+C) / 2

area_of_triangle = math.sqrt(S*(S-A)*(S-B)*(S-C))

time.sleep(1)
print(f"Area of tringle with sides {A} units, {B} units & {C} units  is {area_of_triangle} sq. units")

# PROGRAM-4: area of circle
radius = float(input("Enter radius of circle: "))

area_of_circle = math.pi*(radius**2)

time.sleep(1)
print(f"Area of circle of radius {radius} units is {area_of_circle} sq. units")
time.sleep(1.5)


# PROGRAM-5: simple & compound interest
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time period: "))

simple_interest = (P*R*T)/100
n = 1

compound_interest = P * (1 + (R/n))**(n*T)

time.sleep(1)

print(f"Calculated simple interest for given parameters is {simple_interest}")

time.sleep(1)

print(f"Calculated compound interest for n = 1 and given parameters is {compound_interest}")
time.sleep(1.5)


# PROGRAM-6: calendar
import calendar

year = int(input("ENTER YEAR: "))
Month = int(input("ENTER MONTH: "))

time.sleep(1)

print(calendar.month(year,Month))

time.sleep(1.5)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    