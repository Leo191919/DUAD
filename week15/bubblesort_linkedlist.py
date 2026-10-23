class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node


    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print("-->".join(elements)if elements else "List is empty")


def bubble_sort_linked_list_swap_data(linked_list):
    head = linked_list.head
    if head is None or head.next is None:
        return
    
    last_sorted_node = None

    while True:
        has_made_changes = False
        current = head        

        while current and current.next != last_sorted_node:
            node1 = current
            node2 = current.next

            if node1.data > node2.data:
                
                node1.data, node2.data = node2.data, node1.data
                has_made_changes = True            
            current = current.next 

        if not has_made_changes:
            break


        last_sorted_node = current
        

if __name__== "__main__":
    my_linked_list = LinkedList()
    elements = [11, 1, 2, 3, 10, 4, 5, 6, 9, 7, 8]
    for element in elements:
        my_linked_list.append(element)

    print("Before sorting (swapping data):")
    my_linked_list.display()

    print("Sorting the linked list using bubble sort (swapping data)...")
    bubble_sort_linked_list_swap_data(my_linked_list)

    print("After sorting:")
    my_linked_list.display()

    print("\n--- Testing with an already sorted list ---")
    sorted_list = LinkedList()
    for e in [1,2,3,4,5]:
        sorted_list.append(e)

    print("Original List (already sorted):")
    sorted_list.display()
    bubble_sort_linked_list_swap_data(sorted_list)
    print("Sorted List:")
    sorted_list.display()


    print("\n--- Testing with a reversed list---")
    reversed_list = LinkedList()
    for e in [5,4,3,2,1]:
        reversed_list.append(e)

    print("Original List (reversed):")
    reversed_list.display()
    bubble_sort_linked_list_swap_data(reversed_list)
    print("Sorted List:")
    reversed_list.display()

    print("\n--- Testing with an empty list (swapping data) ---")
    empty_list = LinkedList()
    print("Original List (empty):")
    empty_list.display()
    bubble_sort_linked_list_swap_data(empty_list)
    print("Sorted List:")
    empty_list.display()
