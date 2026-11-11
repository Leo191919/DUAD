user_numbers = []

for i in range (10):
    user_number= int(input(f'ingrese el dato número{i+1}:' ))
    user_numbers.append(user_number)

top_number = max(user_numbers)
print(f'{user_numbers}, the highest was {top_number}')