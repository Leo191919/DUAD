def square_root(number):
    for i in range(number // 2 + 1):
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

list_of_number =[97,25,2,15,13,87,31,60]




roots = roots_of_list(list_of_number)


prime = numbers_prime(list_of_number)
print("Numbers prime: ",prime)
