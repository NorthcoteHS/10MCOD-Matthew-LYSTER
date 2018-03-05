player = input("Rock, Paper, or Scissors? (choose wisely): ")
cheater = ["Rock", "Paper", "Scissors"]

from random import choice, sample
cheater = choice(list(set([0, 1, 2])))

if (player) == "Rock":
    if (cheater) == "Rock":
        print("It would appear that we have made the same choice")
    elif (cheater) == "Paper":
        print("AHAHAHAHAHAHAHAHAHAHAHAHAHA YOU SUCK! I JUST BEAT YOU SENSELESS WITH THE POWER OF PAPER!")
    elif (cheater) == "Scissors":
        print("...I don't wanna talk about it....")
elif (player) == "Paper":
    if (cheater) == "Rock":
        print("I guess you win...")
    elif (cheater) == "Paper":
        print("Don't copy me like that. Tie")
    elif (cheater) == "Scissors":
        print("I eat paper like that for breakfast. YOU SUCK!")
elif (player) == "Scissors":
    if (cheater) == "Rock":
        print("Well. That was unexpected. JUST KIDDING OF COURSE YOU LOST! YOU SUCK!")
    elif (cheater) == "Paper":
        print("Well. I guess there is hope for you after all")
    elif (cheater) == "Scissors":
        print("That is what you people call a tie")
else:
    print("Please try again and acutally input 'Rock', 'Paper' or 'Scissors', (Make sure you use a capital letter at the start")
