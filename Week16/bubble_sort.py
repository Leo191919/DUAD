def bubble_sort(list_to_sort):
    if not isinstance(list_to_sort, list):
        raise TypeError("Input must be a list")

    n=len(list_to_sort)
    if n<=1:
        return
    
    for outer_index in range (n-1):
        has_made_changes = False        

        for index in range(n-1 - outer_index):
            current_element = list_to_sort[index]
            next_element = list_to_sort[index + 1]

            #print (f' -- Iteracion {outer_index}, {index}. Elemento actual: {current_element}, Siguiente elemento:{next_element}')
        
            if current_element > next_element:
                
                list_to_sort[index], list_to_sort[index + 1] = next_element, current_element
                has_made_changes = True


        if not has_made_changes:
            return
