classroom = ['Sofía García',
'Alejandro Ramírez',
'María López',
'David Fernández',
'Laura Martínez,']
first = classroom[0]
last = classroom[-1]
classroom = [last] + classroom[1:-1] + [first]
print(classroom)
