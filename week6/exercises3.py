def sum_lista(lista_numeros):
    sum = 0 
    for numero in lista_numeros:
        sum+= numero
    return sum

my_list = [1,2,3,4,5,6,7,8,9,10]
result = sum_lista(my_list)
print(result)