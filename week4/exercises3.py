#Numero mayor

number1 = int(input("Input the first number: "))
number2 = int(input("Input the second number: "))
number3 = int(input("Input the third number: "))
number = 0


if number1 >= number2 and number1 >= number3:
    print(f"The major number is {number1}")

elif number2 >= number1 and number2 >= number3:
    print(f"The major number is {number2}") 

elif number3 >= number2 and number3 >= number1:
    print(f"The major number is {number3}")
