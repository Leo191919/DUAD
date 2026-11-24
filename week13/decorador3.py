from datetime import date 

class User: 
    def __init__(self, name:str , date_of_birth:date):
        if not isinstance( date_of_birth, date):
            raise TypeError("date_of_birth must be a datetime.date object.")
        self.name = name 
        self.date_of_birth = date_of_birth

    @property
    def age (self) -> int:
        today =date.today()
        age = today.year - self.date_of_birth.year
        if today.month < self.date_of_birth.month or \
            (today.month == self.date_of_birth.month and today.day < self.date_of_birth.day ):
            age -= 1
        return age
    
    def __str__(self):
        return f'User(Name: {self.name}, DOB: {self.date_of_birth}, Age:{self.age})'

MAJORITY_AGE = 18 

def check_adult_user(func):
    def wrapper (*args, **kwargs):
        user_param = None

        if args and isinstance (args[0], User):
            user_param = args[0]
            

        if not user_param and 'user' in kwargs and isinstance(kwargs ['user'], User):
            user_param = kwargs['user']

        if not user_param:
            raise TypeError(
                f"Error in function '{func.__name__}': "
                f"The 'check_adult_user' decorator requires one of the parameters to be a 'User' object. "
            )

        if user_param.age<MAJORITY_AGE:
            raise ValueError(
                f"Access denied for function '{func.__name__}': "
                f"User  '{user_param.name}' is not of legal age (is {user_param.age} years old)."
            )
        return func(*args,**kwargs)
    return wrapper 


@check_adult_user
def enter_nightclub (user: User, club_name:str):
    print (f"'{user.name}' has entered '{club_name}'!") 

@check_adult_user
def make_legal_transaction(amount: float, user:User):
    print (f"'{user.name}' has mode a legal transaction of ${amount:.2f}!")

@check_adult_user
def access_restricted_content(user:User, content_id:str):
    print(f"'{user.name}' has accessed restricted content:'{content_id}'!")



adult_user = User("Alice", date(2000,5,15))
print(f"Adult User:{adult_user}")

minor_user = User("Bob", date(2010,8,20))
print(f"Minor User: {minor_user}")


almost_adult_user = User("Charlie", date(2007,6,1))
print(f"User 'Almost Adult' : {almost_adult_user} ")

print("\n" + "=" * 40 + "\n")

print("--- Attempting functions with Adult user ---")
try:
    enter_nightclub(adult_user, "The Python Club ")
    make_legal_transaction(100.50, user=adult_user)
    access_restricted_content(user=almost_adult_user, content_id= "X1Y2Z3")
except (TypeError, ValueError) as e:
    print(f"Unexpected error with adult user: {e}")

print("\n" + "=" * 40 + "\n")

print("--- Attempting functions with MINOR user---")

try: 
    enter_nightclub(minor_user,"The Python Club")
except ValueError as e:
    print(f"Expected error trying to enter club! {e}")
except TypeError as e:
    print(f"Unexpected type error!{e}")

print("-" * 30)

try:
    make_legal_transaction(250.00, user = minor_user)
except ValueError as e: 
    print(f"Expected error trying to make transaction!{e}")
except TypeError as e:
    print(f"Unexpected type error !{e}")

print("-" * 30 )

try:
    access_restricted_content(minor_user,"TOP SECRET_DOCS")
except ValueError as e:
    print(f"Expected error trying to access restricted content!{e}")
except TypeError as e:
    print(f"Unexpected type error {e}")

print("\n"+"=" * 40 + "\n")

print("--- Test with function that doesn't receive. User or has wrong type ---")

@check_adult_user
def no_user_param(param1:int, param2:str):
    print(f"Function without User parameter: {param1},{param2}")


@check_adult_user
def wrong_user_param (user_data:dict):
    print(f"Function with non-User parameter: {user_data}")

try: 
    no_user_param(10, "hello")
except TypeError as e:
    print(f"Expected error for not finding User!{e}")
    print("-"*30)

try: 
    wrong_user_param({"name":"FakeUser","age":20})
except TypeError as e: 
    print(f"Expected error for User of incorrect type! {e}")