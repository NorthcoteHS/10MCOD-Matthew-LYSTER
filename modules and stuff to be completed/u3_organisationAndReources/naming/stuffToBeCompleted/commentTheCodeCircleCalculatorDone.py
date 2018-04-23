"""
prog: commentTheCodeCircleCalculatorDone
name: Matthew Lyster
date: 2018/03/12
desc: calculates the area and perimeter of a circle according to the radius given
"""

print('Welcome to the Circle Calculator!')

#inputs radius and changes to an integer
r = input('Enter a radius: ')
r = int(r)

#calculates area and tells the user
area = 3.14 * r * r
print('The area is', area)

#calculates perimeter and tells the user
perimeter = 3.14 * r * 2
print('The perimeter is', perimeter)
