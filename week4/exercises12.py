#El numero mas alto entre los 5


numbers = []  #LISTA para almacenar numeros 

for i in range(5): # El bucle se ejecuta 5 veces 
    number = int(input("Please, enter number"+ str(i+1)+":"))
    numbers.append(number)
largest_number=max(numbers)
print("The largest number is: ", largest_number)