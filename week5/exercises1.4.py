my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers=[]
for number in my_list:
    if number %2==0:
        even_numbers.append(number)
print(even_numbers)