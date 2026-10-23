def counting_letter (string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower+=1
    return upper, lower


counting_string = 'Hola Mundo!. Hoy Es Un Buen Dia Para Aprendeder' 
counting_string2 = 'Hola Mundo!.' 

upper_count1,lower_count1 = counting_letter (counting_string)
upper_count2,lower_count2  = counting_letter(counting_string2)

print(f"“There’s {upper_count1} upper cases and {lower_count1} lower cases")
print(f"There’s {upper_count2} upper cases and {lower_count2} lower cases")