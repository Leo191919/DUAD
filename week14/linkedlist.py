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
        print("-->".join(elements))


if __name__== "__main__":
    my_list = LinkedList()
    my_list.append("hola mundo")
    my_list.append(20)
    my_list.append(30)
    my_list.append(40)

    my_list.display()