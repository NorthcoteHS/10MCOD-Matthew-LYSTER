number1 = int(input("first number: "))
operation = input("Which operation?(+, -, *, or /): ")
number2 = int(input("second number: "))
if operation == "+":
    print (number1 + number2)
elif operation == "-":
    print (number1 - number2)
elif operation == "*":
    print (number1 * number2)
elif operation == "/":
    print (number1 / number2)
else:
    print("you haven't entered an operation you klutz")
