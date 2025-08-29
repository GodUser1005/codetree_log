from collections import deque

class Queue:
    def __init__(self):
        self.q = deque()
    
    def push(self, a):
        self.q.append(a)
    
    def pop(self):
        return self.q.popleft()
    
    def size(self):
        return len(self.q)
    
    def empty(self):
        return int(self.size() == 0)

    def front(self):
        return self.q[0]

n = int(input())
q = Queue()

for _ in range(n):
    command = tuple(input().split())
    if len(command) == 2:
        q.push(int(command[1]))
    else:
        command = command[0]
        if command == "pop":
            print(q.pop())
        elif command == "size":
            print(q.size())
        elif command == "empty":
            print(q.empty())
        elif command == "front":
            print(q.front())



    
