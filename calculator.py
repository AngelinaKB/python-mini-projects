num1 = int(input("Enter the first digit: "))
num2 = int(input("Enter the second digit: "))

operator= input("Enter the operator (+,-,/,*): ")

if (operator == "+"):
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif (operator == "-"):
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif (operator == "/"):
    result = num1 / num2
    print(f"{num1} / {num2} = {result}")
elif (operator == "*"):
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
else:
    print("Operator not recognized! Please try again.")
    
