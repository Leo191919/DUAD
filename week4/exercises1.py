#Clasificacion por edad

name=input("Input your name: ")
lastname=input("Input your lastname: ")
age=float (input("Input your age: "))

if age<=1:
    print("You are a baby")

elif 2< age <=12:
    print("You are a child")
elif 13< age <=16:
    print("You are a preadolescence")
elif 17< age <=18:
    print("You are a adolescence")
elif 19< age <=26:
    print("You are a young adult")
elif 27< age <=59:
    print("You are a adult")
elif age >60:
    print("You are a older adult")