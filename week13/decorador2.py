def validate_numeric_params(func):
    def wrapper(*args, **kwargs):
        for arg in args :
            if not isinstance(arg,(int,float)):
                raise TypeError(f"Error iin function '{func.__name__}':"
                                f"Parameter '{arg}'is npt a number . Expected"
                )
        for key, value in kwargs.items():
            if not isinstance(value, (int, float)):
                raise TypeError(
                    f"Error in function '{func.__name__ }':" 
                    f"Parameter '{key}' (with value '{value}') if not a number. Expected an int or float."                        
                )  

            return func(*arg, **kwargs)
        return wrapper


@validate_numeric_params 
def add_numbers (a,b):
    return a + b


@validate_numeric_params
def calculate_average (num1,num2, num3, factor=1.0):
    return (num1+num2+num3) / 3 * factor 

print("---Successful test (all parameter are number)---")
try:
    result1 = add_numbers (10,5)
    print(f"Sum of 10 and 5:{result1}")

    result2 = calculate_average(1000,200,300)
    print(f"Average of 100, 200, 300: {result2}")

    result3 = calculate_average(10,20,30, factor = 2.5)
    print(f"Average of 10,20,330 with factor 2.5: {result3}")

except TypeError as e :
    print(f"An unexpected error occurred!: {e}")

print("\n--- Test with errors (non-numeric parameter)---")

try:
    print("Attempting add_numbers (7, 'eight')...")
    add_numbers(7, "eight")
except TypeError as e:
    print(f"Caught expected exception: '{e}' ")

print("-" *30)

try: 
    print("Attempting add_numbers([1],2)...")
    add_numbers([1],2)
except TypeError as e :
    print(f"Caught expected exception: {e}")

print("-" * 30 )


try: 
    print("Attempting add_numbers (5, None)... ")
    add_numbers(5,None)
except TypeError as e:
    print(f"Caught expected exception: {e}")
    