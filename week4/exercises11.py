#Si tiene algun 30 esta correcto sino incorrecto


number1 = 0
number2 = 0 
number3 = 0 

number1 = int(input("Please, enter number 1: "))
number2 = int(input("Please, enter number 2: "))
number3 = int(input("Please, enter number 3: "))

if number1 + number2 + number3 == 30 :
    print("Correct")
elif number1 == 30:
    print("Correct")
elif number2 == 30:
    print("Correct")
elif number3 == 30:
    print("Correct")
else:
    print("Incorrect")
