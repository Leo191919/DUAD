def turn_over (my_string):

    string = ''
    for i in range (len(my_string)-1,-1,-1):
        string+= my_string[i]
    return string
