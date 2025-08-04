class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList():
    def __init__(self):
        self.head = Node('nil')
        self.tail = None
        self.size = 0
    
    def push_back(self,data):
        new_node = Node(data)
        if self.size == 0:
            self.head.next = new_node
            new_node.prev = self.head
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

n,m = map(int,input().split())
bread = input()
dll = DoublyLinkedList()
for c in bread:
    dll.push_back(c)

iterator = dll.end()

commands = []
for _ in range(m):
    commands.append(list(input().split()))

for command in commands:
    if len(command) == 1:
        c, = command
        if c == 'L':
            if iterator == dll.begin().prev:
                continue
            iterator = iterator.prev
        elif c == 'R':
            if iterator == dll.end():
                continue
            iterator = iterator.next
        elif c == 'D':
            if iterator == dll.end():
                continue
            del_node = iterator.next
            if del_node == dll.end():
                dll.tail = iterator
                iterator.next = None
            else:
                iterator.next = del_node.next
                del_node.next.prev = iterator
                if del_node == dll.begin():
                    dll.head = iterator.next
            dll.size -= 1
    else:
        c,d = command
        new_node = Node(d)
        new_node.prev = iterator
        new_node.next = iterator.next
        iterator.next = new_node
        if new_node.next != None:
            new_node.next.prev = new_node
        iterator = new_node
        if iterator.prev == dll.end():
            dll.tail = new_node
        elif iterator.next == dll.begin():
            dll.head = new_node
        dll.size += 1

iterator = dll.begin()
for _ in range(dll.size):
    print(iterator.data,end="")
    iterator = iterator.next


        
        




