"""
Prog:   debugTheCodeYesOrNoMachineDone.py
Name:   Matthew Lyster
Date:   2018/03/12
Desc:   Answers yes or no to any question.
"""

#import the random module
import random


# Ask the user for a question.
question = input('Ask me anything! ')

# Check for special input.
if question == 'Quit':
    print('Goodbye.')
elif question == 'Hi':
    print("What's up?")
elif question == 'Hello':
    print("What's up?")

# Answer yes or no randomly.
else:
    num = random.randint(1, 2)
    if num == 1:
        print("Yes!")
    elif num == 2:
        print("No")

