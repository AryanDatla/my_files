# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 19:43:06 2024

@author: ARYAN DATLA
"""

questions = [
    
    {"prompt": "What is the capital of France?",
     "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
     "answer": "A"
     },
    
    {"prompt": "Which language is Spoken in Brazil?",
     "options": ["A. Spanish", "B. Portugese", "C. English", "D. French"],
     "answer": "B"
     },
    
    {"prompt": "What is the smallest prime number?",
     "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
     "answer": "B"
     },
    
    {"prompt": "Who wrote 'To kill a Mockingbird'?",
     "options": ["A. Harper Collins", "B. Harper Lee", "C. J K Rowling", "D. Alice Oseman"],
     "answer": "B"
     },
    
    ]



def run_quiz(questions):
    
    score = 0
    
    for question in questions:
        print(question["prompt"] + "\n")
        
        
        for option in question["options"]:
            print(option + "\n")
            
        answer = input("Choose an option: ")
        print()
        
        if answer.upper() == question["answer"]:
            score += 5
    
    print(f"Your score is: {score}")
    
     
#MAIN-------------------------------------------------------------------------------------------------------------------------------------------
run_quiz(questions)            
        
        
        
        