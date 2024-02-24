# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 21:16:36 2024

@author: ARYAN DATLA
"""
import time

command = "" #move the car
turn = ""    #change direction of car
car_on = False
car_off = True

print("type help to get commands")
time.sleep(1)

while command.lower() != "quit":
    command = input("> ")
    
    match command.lower():
        
        #turn the car on
        case 'start':
            if car_on == True:
                time.sleep(1)
                print("car already started...")
            else:    
                time.sleep(1)
                print("car started....")
                car_on = True
                car_off = False
            
        #turn the car off
        case 'stop':
            if car_off == True:
                time.sleep(1)
                print("car already stopped...")
            else:    
                time.sleep(1)
                print("car stopped...")
                car_on = False
                car_off = True 
        
        #move the car forward
        case 'move':
            time.sleep(1)
            if car_off == True:
                print("turn on the car")            
            else:
                time.sleep(1)
                print("car moving forward...")
        
        case 'reverse':
            time.sleep(1)
            if car_off == True:
                print("turn on the car")
            else:
                time.sleep(1)
                print("car going in reverse...")
        
        #turn the car left or right
        case 'turn':
            time.sleep(1)
            if car_off == True:
                print("turn on the car")
            else:
                time.sleep(1)
                direction = input("turn where: ")
                
                if direction == 'left':
                    time.sleep(1)
                    print("car turning left...")
                elif direction == 'right':
                    time.sleep(1)
                    print("car turning right...")
                else:
                    print("wrong input entered")
                    
        #quit the program   
        case 'quit':
            time.sleep(1)
            print("bye-bye!!")   
        
        #commands for car
        case 'help':
            time.sleep(1)
            print('''  start - start the car\n  stop  - stop the car\n  quit  - quit game\n  move  - move the car forward\n  turn  - turn the car left or right\n  reverse - move car in reverse
                  ''')
        #defualt case        
        case default:
            print("check input...")
    
              
