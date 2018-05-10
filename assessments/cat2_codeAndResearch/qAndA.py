#imports the time module
import time

#create a list of all the questions
question = ["How many episodes of No Game No Life are there currently? ", "What do Sora and Shiro call themselves? ", "What is the opening theme to No Game No Life called? ", "In the beginning scene of episode 1, how many was the highest amount of mmorpg characters Sora was playing at once? ", "Were there any references to Jojo's Bizarre Adventure in NGNL? ", "Were there any references to Ace Attorney in NGNL? ", "Were there any references to Spirited Away in NGNL? ", "What was the name of the main Flugel in NGNL? ", "What was the result of the coin toss in episode 12 with the leader of the Werebeasts?(win/loss/draw)? "]

#and another list with all the answers, in corresponding positions with their questions
answer = ["12", "blank", "this game", "4", "yes", "yes", "no", "jibril", "draw"]

#welcome message
print("Hey ya shmuck! If you've come here to do something useful with your time you've come to the wrong place. This a 'No Game No Life' trivia thingy (easy tho). Make sure not to use any capital letters in your answers ^^")

#thisThing will be for changing question and a score variable set up at 0
thisThing = 0
score = 0

#then the questions and responses to the answers the user inputs
if thisThing == 0:
    question1 = input(question[0])
    if question1 == (answer[0]):
        print("Yup that's right. If you know NGNL you'll know that we will probably never get a season 2 (no matter how much a season 2 is needed)")
        score = score + 1
    if question1 != (answer[0]):
        print("Oof not quite.")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 1:
    question2 = input(question[1])
    if question2 == (answer[1]):
        print("Yup your right! It's 「　」!")
        score = score + 1
    if question2 != (answer[1]):
        print("Nah mate not quite.")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 2:
    question3 = input(question[2])
    if question3 == (answer[2]):
        print("Yup that's it! This Game is one of the greatest anime openings ever.")
        score = score + 1
    if question3 != (answer[2]):
        print("Nup you got This question wrong.")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 3:
    question4 = input(question[3])
    if question4 == (answer[3]):
        print("Yup. 1 for each hand, and 1 for each foot. Nuts.")
        score = score + 1
    if question4 != (answer[3]):
        print("Nope. Sorry :/")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 4:
    question5 = input(question[4])
    if question5 == (answer[4]):
        print("Well done! Yes there were a couple of Jojokes in there :P")
        score = score + 1
    if question5 != (answer[4]):
        print("Nah of course there were ;)")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 5:
    question6 = input(question[5])
    if question6 == (answer[5]):
        print("HOLD IT! Yes there were a couple of those. Ace Attorney is great :P")
        score = score + 1
    if question6 != (answer[5]):
        print("OBJECTION! There were some :P")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 6:
    question7 = input(question[6])
    if question7 == (answer[6]):
        print("Your right! There weren't (but there should have been)")
        score = score + 1
    if question7 != (answer[6]):
        print("Nah, sadly there weren't :/")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 7:
    question8 = input(question[7])
    if question8 == (answer[7]):
        print("Yup! Jibril was a great character. All of this is bringin' back memories :P")
        score = score + 1
    if question8 != (answer[7]):
        print("Well either you spelled it incorrectly or you're just wrong :/")
    thisThing = thisThing + 1
time.sleep(2)
if thisThing == 8:
    question9 = input(question[8])
    if question9 == (answer[8]):
        print("Yup. The most bull$#!+ coin toss in history :/")
        score = score + 1
    if question9 != (answer[8]):
        print("Nope. If only it were that simple...")
    thisThing = thisThing + 1
time.sleep(2)

#displays a concluding message, telling people what score they got with different responses based on how many questions they got right
if thisThing == 9:
    if score < 5:
        print("Done! You got " + str(score) + " answer(1) correct! I reckon you could do a bit better though :)")
    if 4 < score < 9:
        print("Well that's it! Well done, you got " + str(score) + "questions right! That's a pretty decent score!")
    if score == 9:
        print("That's all mate! Fastastic $#!+ you got 9 out of 9 correct!")
