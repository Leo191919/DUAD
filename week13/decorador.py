def say_hello_before(original_function):

    def modified_function():
        print("Hello! I'm about to run a function.")
        original_function()
    return modified_function

@say_hello_before
def my_first_function():
    print("I'm the first function!.")

@say_hello_before
def my_second_function():
    print("I'm the second function! I'm doing something different.")


print("--- calling my_first_function ---")
my_first_function()

print("\n--- Calling my_second_function---")
my_second_function()