def sum_list(list_numbers):
    sum = 0 
    for number in list_numbers:
        sum+= number
    return sum

my_list = [1,2,3,4,5,6,7,8,9,10]
result = sum_list(my_list)
print(result)