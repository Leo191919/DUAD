def alphabetical_sequence(string):
    string_list = string.split('-')
    string_list.sort()
    return '-'.join(string_list)

Vehicles = 'truck-trailer-car-bicycle-bicycle-bike-bus'
result=alphabetical_sequence(Vehicles)
print (result)

