class Node:
    def __init__(self, data ):
        self.data = data
        self.prev = None 
        self.next = None

class Deque:
    def __init__(self):
        self.head =None
        self.tail = None 
        self.size_count = 0 


    def is_empty(self):
        return self.size_count==0 
    
    def size (self):
        return self.size_count 
    
    def push_left(self, data ):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else :
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size_count += 1 

    def push_right(self,data):
        
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node 

        else :
            new_node.prev = self.tail 
            self.tail.next = new_node
            self.tail = new_node
        self.size_count += 1  

    def pop_left(self):

        if self.is_empty():
            return None
        
        remove_node = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

            if self.head :
                self.head.prev = None 
        self.size_count -= 1


        remove_node.next = None
        remove_node.prev = None
        return remove_node.data
    
    
    def pop_right(self):
        if self.is_empty():
            return None
        
        removed_node = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None

        else :
            self.tail = self.tail.prev

            if self.tail :
                self.tail.next = None

        self.size_count -= 1
        removed_node.next = None
        removed_node.prev = None
        return removed_node.data 
    
    def print_structure(self):

        if self.is_empty():
            print("Deque: Empty")
            return

        current = self.head
        elements = ""
        while current:
            elements += str(current.data)
            if current.next:
                elements += "<->" 

            current = current.next
        print (f'Deque : {elements}')


if __name__ == "__main__":
    my_deque = Deque()

    print("---Push Operations (add)---")
    my_deque.push_right("A")
    my_deque.print_structure()

    my_deque.push_left("B")
    my_deque.print_structure()

    my_deque.push_right("C")
    my_deque.print_structure()

    my_deque.push_left("D")
    my_deque.print_structure()

    print(f"\nCurrent Deque Size: {my_deque.size()}")

    print("\n ---Pop Operations (remove)---")
    
    print(f"Pop Left:{my_deque.pop_left()}")
    my_deque.print_structure()

    print(f"Pop Right:{my_deque.pop_right()}")
    my_deque.print_structure()

    print(f"Pop Left:{my_deque.pop_left()}")
    my_deque.print_structure()

    print(f"Pop Right:{my_deque.pop_right()}")
    my_deque.print_structure()

    print(f"\nCurrent Deque Size: {my_deque.size()}")
    print(f"Is Deque Empty? {my_deque.is_empty()}")

    print("\n --- Attempting Pop from Empty Deque ---")
    print(f"Pop Left (empty): {my_deque.pop_left()}")
    print(f"Pop Right (empty): {my_deque.pop_right()}")
    