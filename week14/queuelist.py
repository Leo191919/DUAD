class QueueList:
    def __init__(self):
        self.item=[]


    def enqueue(self,item):
        self.item.append(item)


    def dequeue(self):
        if not self.is_empty():
            return self.item.pop(0)
        return None
    

    def is_empty(self):
        return len(self.item)==0 
    

    def size(self):
        return len(self.item)
    

    def __str__(self):
        return f"QueueList({self.item})"


from collections import deque

class QueueDeque:
    def __init__(self):
        self.item = deque()

    def enqueue(self,item):
        self.item.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.item.pop()
        return None
    

    def is_empty(self): 
        return len(self.item) == 0 
    

    def size(self):
        return len(self.item)
    

    def __str__(self):
        return f"QueueDeque({list(self.item)})"



    
if __name__== "__main__":
    my_first_queue = QueueList()
    my_first_queue.enqueue(10)
    my_first_queue.enqueue(20)
    my_first_queue.enqueue("Hola Mundo")
    my_first_queue.enqueue(30)

    print(my_first_queue)

    my_queue = QueueDeque()
    my_queue.enqueue(10)
    my_queue.enqueue(20)
    my_queue.enqueue("Hola mundo")
    my_queue.enqueue(30)

    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())
    print(my_queue.dequeue())