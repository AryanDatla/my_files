# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 19:42:46 2024

@author: ARYAN DATLA
"""

weight = int(input("weight: "))
unit = input("Lbs or Kgs: ")

if unit == "Lbs" :     
    print(float(weight*0.45))
elif unit == "Kgs":
    print(weight)
else:
    print("invalid input")