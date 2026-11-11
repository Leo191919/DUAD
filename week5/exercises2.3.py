list_to_delete_keys = ['access level','age']
employee = {'name':'john','email':'john@ecorp.com', 'access level':5 , 'age':28}

for key in list_to_delete_keys:
    if key in employee:
        del employee[key]

print(employee)