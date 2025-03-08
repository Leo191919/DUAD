def add (Current_number, new_number):
    return Current_number + new_number
    

def subtract (current_number, new_number):
    return current_number - new_number


def multiply (Current_number, new_number):
    return Current_number * new_number


def divide(current_number, new_number):
    if new_number == 0: 
        return "Error: Cannot divide by zero "
    return current_number/new_number

current_number = 0

while True: 

    print(f"\nBasic Calculator")
    print('1. add')
    print('2. Subtract')
    print('3. multiply')
    print('4. divide')
    print('5. Delete result' )
    print('6. Close')

    try:
        option = int(input('Choose a option (1 - 6): ' ))

        if option == 6:
            print('Close basic calculator')
            break

        if option == 5 :
            current_number = 0
            print("Delete result")
            continue
        if option in (1,2,3,4):
            try :
                new_number = float(input("Enter the Number 2: "))
                
                if option == 1 :
                    current_number= add(current_number, new_number)
                    print(f'The result is: {current_number}')
                elif option == 2 : 
                    current_number=subtract(current_number, new_number)
                    print(f'The result is: {current_number}')
                elif option == 3 : 
                    current_number=multiply(current_number, new_number)
                    print(f'The result is: {current_number}')

                elif option == 4 : 
                    result = divide(current_number, new_number)
                    if isinstance (result, str):
                        print(result)
                    else:
                        current_number= result
                        print(f'The result is: {current_number}')
            except ValueError:
                print('Error: Invalid entry. Please enter a valid number.')
        else:
            print('Error: Invalid option. Select an option from 1 to 6.')
    except ValueError:
        print('Error: Invalid entry. Enter an integer number for the option.')