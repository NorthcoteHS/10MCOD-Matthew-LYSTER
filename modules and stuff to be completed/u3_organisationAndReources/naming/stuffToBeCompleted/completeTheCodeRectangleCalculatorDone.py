"""
Prog:   completeTheCodeRectangleCalculatorDone.py
Name:   Matthew Lyster
Date:   2018/03/12
Desc:   Calculates the area and perimeter of a rectangle.
"""

# Display welcome message.
print('Welcome to the Rectangle Calculator!')

# Use input to get the rectangle's length and width (2 lines).
# - Remember to provide a prompt message for each input.
length = input("what is the length of the rectagle? ")
width = input("what is the width? ")


# Convert length and width to integers.
length = int(length)
width = int(width)

# Calculate the area (1 line: length times width).
area = length * width

# Display the area.
print('The area is', area)

# Calculate and display the perimeter (2 lines: P = 2*length + 2*width).
perimeter = length + length + width + width
print("The perimeter is ", perimeter)

