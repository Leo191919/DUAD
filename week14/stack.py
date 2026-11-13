class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack: 

    def __init__(self):
        self.top = None
        self.size_count = 0 


    def is_empty(self): 
        return self.top is None


    def size(self):
        return self.size_count 
    

    def push (self, data):
        new_node = Node(data)
        if self.top is not None:
            new_node.next = self.top
        self.top = new_node
        self.size_count += 1


    def pop(self):
        if self.is_empty():
            return None
        
        popped_node_data = self.top.data
        self.top = self.top.next
        self.size_count -=1
        return popped_node_data
    

    def peek(self):

        if self.is_empty():
            return None
        return self.top.data
    

    def print_structure(self):
        if self.is_empty():
            print("Stack: Empty")
            return
        

        current = self.top
        temp_elements = []

        while current:
            temp_elements.append(str(current.data))
            current = current.next

        
        print ("Stack (Top to Bottom):")

        for i in range (len(temp_elements)-1,-1,-1):
            print(f" | {temp_elements[i]} | ")
        print(" ----- ")

if __name__ == "__main__":
    my_stack = Stack()

    print("--- Push Operations ---")
    my_stack.push ("A")
    my_stack.print_structure()

    my_stack.push ("B")
    my_stack.print_structure()
    
    my_stack.push ("C")
    my_stack.print_structure()
    

    print(f"\nStack Size: {my_stack.size()} ")
    print(f"Element at top (peek): {my_stack.peek()}")

    print("\n --- Pop Operations ---")
    popped_item = my_stack.pop()
    print(f'Popped: {popped_item}')
    my_stack.print_structure()


    popped_item = my_stack.pop()
    print(f"Popped: {popped_item}")
    my_stack.print_structure()

    print(f"Stack Size: {my_stack.size()}")
    print(f"Element at top (peek): {my_stack.peek()}")

    popped_item = my_stack.pop()
    print(f"Popped: {popped_item}")
    my_stack.print_structure()


    print(f"\nIs stack empty? {my_stack.is_empty()}")
    print(f"Attempting pop from empty stack: {my_stack.pop()}")