def bubble_sort (list_sort):
    for outer_index in range(0, len(list_sort) - 1):
        has_made_changes = False 
        for index in range (0, len(list_sort)-1 - outer_index):
            current_element = list_sort[index]
            next_element = list_sort[index +1]
            if current_element > next_element:
                list_sort[index] = next_element
                list_sort[index +1] = current_element
                has_made_changes = True
        if not has_made_changes:
            return
            

my_test_list = [11,1,2,3,10,4,5,6,9,7,8]
bubble_sort(my_test_list)
print(my_test_list)


