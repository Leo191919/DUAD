#100 numeros los dos ejercicios de 100 numeros los hice en este mismo

numbers = [] #  list to storage numbers
total_summa= 0
for i in range(100): #el bucle se ejecuta 100 veces 
    number=int(input("Please, enter number "+ str (i+1)+ ":"))
    numbers.append(number)
    total_summa+=number
largest_number= int(max(numbers))
print(f"The total and the highest number are : {total_summa}, {largest_number} ")