class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)  
        # set the node as head    
        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        current = self.head
        while current:
            if current.get_value() == value:
                return True
            current = current.get_next()
        return False

    def reverse_list(self, node, prev):
        # reverse singly linked list, given the node to start
        # extreme case, None or one item, or input node not in list
        if self.head is None:
            return None
        if self.head.get_next() is None:
            return None
        if not self.contains(node.value):
            return None
        ## find node in list
        # current = self.head
        # while current != node:
        #     currrent = current.get_next()
        # simple case, only two items
        if self.head.get_next() is None:
            pivot= self.head.get_next()
            pivot.set_next(self.head)
            self.head.set_next(None)
            self.head = pivot
        # more than two items: recursion 
        else:
            current = LinkedList()
            current.add_to_head(self.head.get_next())
            current.reverse_list(None, None)
        


