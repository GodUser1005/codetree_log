n = int(input())
points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

points = [(points[i][0], Point(points[i][1][0],points[i][1][1])) for i in range(n)]
points.sort(key=lambda p: (abs(p[1].x) + abs(p[1].y),p[0]))

for p in points:
    print(p[0])