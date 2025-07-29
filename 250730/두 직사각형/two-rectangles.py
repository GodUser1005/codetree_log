a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

# Please write your code here.

def is_intersecting(a,b):
    x1,y1,x2,y2 = a
    x3,y3,x4,y4 = b

    if (x1 > x4) or (x3 > x2) or (y1 > y4) or (y3 > y2):
        return False
    return True

print("overlapping" if is_intersecting(a,b) else "nonoverlapping") 
