#Porcentaje  de Hombres y mujeres 


men = 0
women = 0
sex= 0
total_people = 0
counter = 1
average_women = 0
average_men = 0


total_people = int(input("Please, enter the number of people: "))


while counter <= total_people:
    sex = int(input("Please, enter your sex(1=women)(2=men): "))
    counter += 1
    if sex <= 1:
        women += 1
    else: 
        men += 1

average_women=100/total_people*women
average_men=100/total_people*men
print(f"The number of women is: {women}, {average_women} %")
print(f"The number of women is: {men}, {average_men} %")