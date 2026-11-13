#Suma de numeros 


number=0
counter=0
counter2=1

number=int(input("Please, enter the number: "))

while counter2<=number:

    counter+=counter2
    counter2+=1

print(f"The sum of the number is: {counter}")