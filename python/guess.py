# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 20:38:40 2024

@author: ARYAN DATLA
"""

#guess

secret_number = 11
i = 0#counter
while True:
    
    guess = int(input("Guess: "))
    
    i += 1
    
    if guess == secret_number:
        print("you won!!")
        break
    else:
        print("wronng answer!")
    
    if i == 3:
        print("Out of guesses")
        break