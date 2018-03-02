player = input("Rock, Paper, or Scissors? (choose wisely): ")
cheateroptions = ["Rock", "Paper", "Scissors"]
cheater = cheateroptions[randint(0, 2)]
if (player) == "Rock":
    if (cheater) == "Rock":
        print("It would appear that we have made the same choice")
    if (cheater) == "Paper":
        print("AHAHAHAHAHAHAHAHAHAHAHAHAHA YOU SUCK! I JUST BEAT YOU SENSELESS WITH THE POWER OF PAPER!")
    if (cheater) == "Scissors":
        print("...I don't wanna talk about it....")
if (player) == "Paper":
    if (cheater) == "Rock":
        print("I guess you win...")
    if (cheater) == "Paper":
        print("Don't copy me like that. Tie")
    if (cheater) == "Scissors":
        print("I eat paper like that for breakfast. YOU SUCK!")
if (player) == "Scissors":
    if (cheater) == "Rock":
        print("Well. That was unexpected. JUST KIDDING OF COURSE YOU LOST! YOU SUCK!")
    if (cheater) == "Paper":
        print("Well. I guess there is hope for you after all")
    if (cheater) == "Scissors":
        print("That is what you people call a tie")
