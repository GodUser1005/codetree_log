class Node:
    def __init__(self, data):
        self.prev = None
        self.next = None
        self.data = data

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get_size(self):
        return self.size
    
    def empty(self):
        return self.size == 0
    
    def push_front(self, a):
        new_node = Node(a)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1
    
    def push_back(self, a):
        new_node = Node(a)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1
        
    def pop_front(self):
        if self.size == 0:
            return -1
        elif self.size == 1:
            result = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return result
        else:
            self.size -= 1
            del_node = self.head
            self.head = del_node.next
            self.head.prev = None
            return del_node.data
        
    def pop_back(self):
        if self.size == 0:
            return -1
        elif self.size == 1:
            result = self.head.data
            self.head = None
            self.tail = None
            self.size = 0
            return result
        else:
            self.size -= 1
            del_node = self.tail
            self.tail = del_node.prev
            self.tail.next = None
            return del_node.data
        
    def front(self):
        if self.empty():
            return -1
        else:
            return self.head.data
    
    def back(self):
        if self.empty():
            return -1
        else:
            return self.tail.data
    

dll = DLL()

n = int(input())

for i in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        cmd[1] = int(cmd[1])
        if cmd[0] == "push_back":
            dll.push_back(cmd[1])
        elif cmd[0] == "push_front":
            dll.push_front(cmd[1])
    else:
        cmd = cmd[0]
        if cmd == "pop_back":
            print(dll.pop_back())
        elif cmd == "pop_front":
            print(dll.pop_front())
        elif cmd == "size":
            print(dll.get_size())
        elif cmd == "empty":
            print(1 if dll.empty() else 0)
        elif cmd == "front":
            print(dll.front())
        elif cmd == "back":
            print(dll.back())





            


            
    











