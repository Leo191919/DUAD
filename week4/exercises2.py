#Numero secreto 


number_secret=7
attempts=0

while True:
    guess = int(input("Guess the number secret(entre 1 y 10): "))
    attempts += 1
    if guess<number_secret:
        print("Failed, try again.")
    elif guess>number_secret:
        print("Failed, try again.")
    else :
        print(f"You guess the number secret in {attempts} guess.")
        break
