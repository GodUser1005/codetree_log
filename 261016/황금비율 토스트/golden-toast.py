class Bread:
    def __init__(self, char):
        self.data = char
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        dummy = Bread('dummy')
        self.head = dummy
        self.tail = dummy
        self.size = 0

    def begin(self):
        return self.head
    
    def end(self):
        return self.tail
    
    def push(self, bread, char):
        new_bread = Bread(char)
        # 현재 위치가 꼬리일 때
        if bread == self.tail:
            new_bread.prev = bread
            bread.next = new_bread
            self.tail = new_bread
        # 현재 위치가 중간일 때
        else:
            new_bread.next = bread.next
            new_bread.prev = bread
            bread.next.prev = new_bread
            bread.next = new_bread
        
        # 현재 위치가 맨 앞일 때 
        if bread.data == "dummy":
            self.head = new_bread

        self.size += 1

        return new_bread
    
    def pop(self, bread):
        if self.tail == bread:
            return bread
        
        self.size -= 1
        # 다음 빵이 마지막 일 때
        if self.tail == bread.next:
            bread.next = None
            self.tail = bread
            return bread
        # 다음 빵이 머리 일 때
        elif self.head == bread.next:
            bread.next = self.head.next
            self.head.next.prev = bread
            self.head = bread.next
            return bread
        # 다음 빵이 중간 빵 일 때
        else:
            next_bread = bread.next
            bread.next = next_bread.next
            next_bread.next.prev = bread
            return bread
            


n,m = map(int, input().split())

str = list(input())
dll = DLL()
it = dll.begin()
for c in str:
    it = dll.push(it, c)


it = dll.end()
for i in range(m):
    cmd = input().split()
    if cmd[0] == "L":
        if it.prev != None:
            it = it.prev
    elif cmd[0] == "R":
        if it.next != None:
            it = it.next
    elif cmd[0] == "D":
        it = dll.pop(it)
    elif cmd[0] == "P":
        it = dll.push(it, cmd[1])
    


it = dll.begin()
while it != None:
    print(it.data, end="")
    it = it.next
