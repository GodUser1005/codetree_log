class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_back(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.size += 1

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail
    
dll = DoublyLinkedList()
dll.push_back(Node('c'))
dll.push_back(Node('c'))
dll.push_back(Node('c'))





