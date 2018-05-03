favourites = []
rating = []
userInput = input("What's one of your favourite movies? ")
while userInput != "quit":
    ratingQ = input("What would you rate it out of 10? ")
    rating.append(ratingQ)
    userInput = input("What's one of your favourite movies? ")
    favourites.append(userInput)
print("Thanks for telling me all the movies I need to avoid, you have named ", str(len(favourites))" movies")
