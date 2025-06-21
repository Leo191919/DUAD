class TreeNode:
    def __init__ (self,data):
        self.data = data 
        self.left = None
        self.right = None 


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        new_node = TreeNode(data)
        if self.root is None :
            self.root = new_node
            return
        
        class _QueueNode: 
            def __init__(self, tree_node_ref):
                self.tree_node = tree_node_ref
                self.next = None

        _queue_head = None 
        _queue_tail = None 

        def _enqueue(node_ref):
            nonlocal _queue_head, _queue_tail
            q_node = _QueueNode(node_ref)
            if _queue_head is None :
                _queue_head = q_node
                _queue_tail = q_node
            else:
                _queue_tail.next = q_node
                _queue_tail = q_node


        def _dequeue():
            nonlocal _queue_head, _queue_tail
            if _queue_head is None:
                return None
            q_node_to_return = _queue_head
            _queue_head = _queue_head.next
            if _queue_head is None:
                _queue_tail = None
            return q_node_to_return.tree_node
            
        _enqueue(self.root)

        while True: 
            current_tree_node = _dequeue()
            if current_tree_node is None :
                break

            if current_tree_node.left is None:
                current_tree_node.left = new_node
                break
            else:
                _enqueue(current_tree_node.left)

            if current_tree_node.right is None:
                current_tree_node.right = new_node
                break 
            else:
                _enqueue(current_tree_node.right )


    def  print_structure (self):

        if self.root is None:
            print("Binary Tree: Empty")
            return
            

        class _QueueNode:
            def __init__(self, tree_node_ref):
                self.tree_node = tree_node_ref
                self.next = None

        _queue_head = None
        _queue_tail = None

        def _enqueue(node_ref):
            nonlocal _queue_head, _queue_tail
            q_node = _QueueNode(node_ref)
            if _queue_tail is None:
                _queue_head = q_node
                _queue_tail = q_node

            else :
                _queue_tail.next = q_node
                _queue_tail = q_node

            
        def _dequeue():
            nonlocal _queue_head, _queue_tail
            if _queue_head is None :
                return None 
            q_node_to_return = _queue_head
            _queue_head = _queue_head.next
            if _queue_head is None:
                _queue_tail = None
            return q_node_to_return.tree_node
        
        _enqueue(self.root)

        print("Binary Tree(Level Order Traversal):")
        while _queue_head:
            current_level_count = 0 
            temp_current_for_count = _queue_head

            while temp_current_for_count:
                current_level_count +=1 
                temp_current_for_count = temp_current_for_count.next 

            nodes_at_this_level_data = []

            for _ in range (current_level_count):
                node = _dequeue()
                if node:
                    nodes_at_this_level_data.append(str(node.data))
                    if node.left: 
                        _enqueue(node.left)
                    if node.right:
                        _enqueue(node.right)
                else:
                    nodes_at_this_level_data.append("None")

            if nodes_at_this_level_data:
                print (f" [{' '.join(nodes_at_this_level_data)}]")
                

if __name__ == "__main__":
    my_tree = BinaryTree() 

    print("--- Inserting elements ---")
    my_tree.insert(50)
    my_tree.print_structure()

    my_tree.insert(25)
    my_tree.insert(75)
    my_tree.print_structure()

    my_tree.insert(10)
    my_tree.insert(35)
    my_tree.insert(60)
    my_tree.insert(90)
    my_tree.print_structure()

    my_tree.insert(5)
    my_tree.insert(15)
    my_tree.print_structure()

    print("\n ---Empty Tree ---")
    empty_tree = BinaryTree()
    empty_tree.print_structure()

    