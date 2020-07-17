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

    def find_node(self, node):
        # return the node that matches input node 
        curr = self.head
        while curr != node:
            curr = curr.get_next()
        return curr


    def reverse_list(self, node, prev):
        # reverse singly linked list, given the node to start
        # Time: O(n), Space: O(n)
        # boundary cases, return None
        # base case: one item, return self
        # node will be where reverse ocurr 
        # boundary case: null
        if node is None:
            return None
        # base case, 1 item, not null
        if node.get_next() is None: 
            # fix the head
            self.head = node           
            return node
        # reverse (node.next), and returned as rest
        rest = self.reverse_list(node.get_next(), None)
        # reverse pointer between node and node.next
        node.get_next().set_next(node)
        # fix the tail
        node.next = None
        return rest
        
            
        
    # Below is a functional solution using loop, just for my own reference. Time: O(n), Space: O(1)
    """
    def reverse_list(self, node, prev): 
        # iterative method
        # initialize three pointers
        # this three pointers will be sliding down the chain until prev sits on the tail (the new head)

        prev = None
        curr = self.head 
        next = None
        while curr != None:
            next = curr.get_next()
            curr.set_next(prev)
            prev = curr
            curr = next
            
        self.head = prev        
        
    """
