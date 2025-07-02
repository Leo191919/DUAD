def bubble_sort (list_sort):
    n=len(list_sort)

    for outer_index in range(n-1):
        has_made_changes = False 
        
        for index in range (n-1, outer_index, -1):

            current_element = list_sort[index]
            previous_element = list_sort[index -1]
            
            print(f" -- Iteration {outer_index}, {index}. Current Element(right):{current_element}, Previous Element(left):{previous_element}")

            if current_element < previous_element:
                list_sort[index] = previous_element
                list_sort[index -1] = current_element
                has_made_changes = True

        if not has_made_changes:
            
            return
            

my_test_list = [11,1,2,3,10,4,5,6,9,7,8]
bubble_sort(my_test_list)
print(my_test_list)

