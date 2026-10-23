#Numero menor

a=0
b=0
number1=0
number2=0

number1=input("Please, enter the first numbers: ") 
number2=input("Please, enter the second numbers: ")

if number1>number2:
    a=number2
    b=number1
else:
    number2>number1
    a=number1
    b=number2
print(f"""The sum of the number is: 
{a}
{b}""")
