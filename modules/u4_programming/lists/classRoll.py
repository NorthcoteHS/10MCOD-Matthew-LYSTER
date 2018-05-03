import random
roll = ["Jessica", "Emily", "Jordan", "Kayley", "Bruce", "Michael", "Everett", "Lisa", "Sam", "Noah"]
print(roll[2])
enrolment = len(roll)
roll.append("James")
del roll[2]
roll[4] = "Mike"
roll.sort()
roll.reverse()

roll1 = roll[0:6]
roll2 = roll[6:0]
#i dont know if roll2 will actually include 6-10 but if i write [6:10] itll go from 6-9 :/
