player = input("Rock, Paper, or Scissors? (choose wisely): ")

import random
cheater = random.randint(0,2)

if (player) == "Rock":
    if (cheater) == 0:
        print("It would appear that we have made the same choice")
    elif (cheater) == 1:
        print("AHAHAHAHAHAHAHAHAHAHAHAHAHA YOU SUCK! I JUST BEAT YOU SENSELESS WITH THE POWER OF PAPER!")
    elif (cheater) == 2:
        print("...I don't wanna talk about it....")
elif (player) == "Paper":
    if (cheater) == 0:
        print("I guess you win...")
    elif (cheater) == 1:
        print("Don't copy me like that. Tie")
    elif (cheater) == 2:
        print("I eat paper like that for breakfast. YOU SUCK!")
elif (player) == "Scissors":
    if (cheater) == 0:
        print("Well. That was unexpected. JUST KIDDING OF COURSE YOU LOST! YOU SUCK!")
    elif (cheater) == 1:
        print("Well. I guess there is hope for you after all")
    elif (cheater) == 2:
        print("That is what you people call a tie")
else:
    print("Please try again and acutally input 'Rock', 'Paper' or 'Scissors', (Make sure you use a capital letter at the start")
