class Node:
    def __init__(self,data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def push_front(self,a):
        new_node = Node(a)
        if self.size != 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1
    
    def push_back(self,a):
        new_node = Node(a)
        if self.size != 0:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1
    
    def pop_front(self):
        data = self.head.data
        if self.size > 1:
            self.head.next.prev = None
            self.head = self.head.next
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return data
    
    def pop_back(self):
        data = self.tail.data
        if self.size > 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
        else:
            self.head = None
            self.tail = None
        self.size -= 1
        return data
    
    def print_size(self):
        return self.size
    
    def empty(self):
        return int(self.size == 0)

    def front(self):
        return self.head.data

    def back(self):
        return self.tail.data
    

n = int(input())

dll = DoublyLinkedList()
commands = []
for _ in range(n):
    command = list(input().split())
    commands.append(command)

for command in commands:
    if len(command) == 2:
        c,a = command
        a = int(a)
        if c == 'push_front':
            dll.push_front(a)
        else:
            dll.push_back(a)
    else:
        c, = command
        if c == 'pop_front':
            print(dll.pop_front())
        elif c == 'pop_back':
            print(dll.pop_back())
        elif c == 'size':
            print(dll.print_size())
        elif c == 'empty':
            print(dll.empty())
        elif c == 'front':
            print(dll.front())
        elif c == 'back':
            print(dll.back())







