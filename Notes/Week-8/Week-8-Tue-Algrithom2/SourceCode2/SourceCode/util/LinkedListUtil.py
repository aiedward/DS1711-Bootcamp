from lecture1.linkedlist.LinkedList import Node
from lecture1.linkedlist.LinkedList import LinkedList

class LinkedListUtil:
    
    def generate_sequence_list(self, n):
        list = LinkedList()
        for i in range(1, n+1):
            list.add_last(i)
        return list

           
    def generate_full_cycle_list(self, n):     
        assert n>=1
        list = LinkedList()
        current = list.head
        first = Node(1)
        current.next = first
        current = first
        
        for i in range(2, n+1):
            node = Node(i)
            current.next = node
            current = node
            
        current.next = first
        return list
    
    def generate_cycle_list(self, n, pos):
        assert n>=1
        assert pos>=1 and pos<=n
        list = LinkedList()
        start = list.head
        
        for i in range (1, pos+1):
            node = Node(i)
            start.next = node
            start = node
            
        current = start
        for i in range (pos+1, n+1):
            node = Node(i)
            current.next = node
            current = node        
    
        current.next = start
        return list

if __name__ == "__main__":
    util = LinkedListUtil()
    list = util.generate_sequence_list(10)
    list.printlist()
    
    list = util.generate_full_cycle_list(6)
    list.printlist()
    
    list = util.generate_cycle_list(6, 3)
    list.printlist()