def alphabetical_sequence(string):
    string_list = string.split('_')
    string_list.sort()
    return '_'.join(string_list)

