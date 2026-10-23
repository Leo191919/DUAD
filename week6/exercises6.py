def alphabetical_sequence(string):
    string_list = string.split('_')
    string_list.sort()
    return '_'.join(string_list)

Vehicles = 'truck_trailer_car_bicycle_bicycle_bike_bus'
result=alphabetical_sequence(Vehicles)
print (result)

