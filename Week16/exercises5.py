def counting_letter (string):
    upper = 0
    lower = 0
    for letter in string:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower+=1
    return upper, lower
