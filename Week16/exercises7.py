def square_root(number):

    if number ==0:
        return 0 
    
    for i in range(1, number + 2):
        if i * i > number:
            return i - 1
    return number 


def es_primo(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def roots_of_list (list_of_number):
    results=[]
    for number in list_of_number:
        result=square_root(number)
        results.append(result)
    return results


def numbers_prime(list_of_numbers):
    results=[]
    for number in list_of_numbers:
        if es_primo(number):
            results.append(number)
    return results


