
## LinkedList class
class OutBoundError(Exception):
    pass

class EmptyError(Exception):
    pass


class Node:
    def __init__(self, value = None, next = None):
        self._value = value
        self._next = next
        
    
    
class LinkedList:
    def __init__(self):
        self._head = Node()
        self._tail = None
        self._length = 0
        
    
    def peek(self):
        if not self._head._next:
            raise EmptyError
        return self._head._next._value
    

    # get funtions
    def get_first(self):
        if not self._head._next:
            raise EmptyError
        return self._head._next._value

    
    
    def get_last(self):
        if not self._head._next:
            raise EmptyError
        node = self._head
        while node._next != None:
            node = node._next
        return node._value


    
    def get(self, index):
        if (index < 0 or index > self._length):
            raise OutBoundError
        if not self._head._next:
            raise EmptyError
        node = self._head._next
        for i in range(index):
            node = node._next
        return node._value        


    # add funtions
    def add_first(self, value):
        node = Node(value, None)
        node._next = self._head._next
        self._head._next = node
        self._length += 1
        
        
    def add_last(self, value):
        new_node = Node(value)
        node = self._head
        while node._next != None:
            node = node._next
        node._next = new_node
        self._length += 1
        
        
    def add(self, index, value):
        if (index < 0 or index > self._length):
            raise OutBoundError
        if not self._head._next:
            raise EmptyError
        new_node = Node(value)
        node = self._head
        for i in range(index):
            node = node._next
        new_node._next = node._next
        node._next = new_node
        self._length += 1
        

    # remove funcitons    
    def remove_first(self):
        if not self._head._next:
            raise EmptyError
        node = self._head._next
        self._head._next = self._head._next._next
        self._length -= 1

         
        
    def remove_last(self):
        if not self._head._next:
            raise EmptyError
        node = self._head._next
        pre_node = self._head
        while node._next != None:
            pre_node = node
            node = node._next
        pre_node._next = None
        self._length -= 1

    
    
    def remove(self, index):
        if (index < 0 or index >= self._length):
            raise OutBoundError
        if not self._head._next:
            raise EmptyError
        node = self._head
        for i in range(index):
            node = node._next
        
        node._next = node._next._next
        self._length -= 1


    # show funtion
    def print_list(self):
        node = self._head._next
        while node:
            print(node._value, end = " ")
            node = node._next
        print(" ")

    
