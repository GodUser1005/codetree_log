x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
# x1[0], y1[0], x2[0], y2[0] =-8, 7, 5, 9
# x1[1], y1[1], x2[1], y2[1] = -3, -2, -2 ,-1

# Please write your code here.
offset = 1000
mat = [[0]*(2*offset+1) for _ in range(2*offset+1)]

for i in range(y1[0]+offset,y2[0]+offset):
    for j in range(x1[0]+offset,x2[0]+offset):
        mat[i][j] = 1

for i in range(y1[1]+offset,y2[1]+offset):
    for j in range(x1[1]+offset,x2[1]+offset):
        mat[i][j] = 0

def find_bottom_left():
    for i in range(y1[0]+offset,y2[0]+offset):
        for j in range(x1[0]+offset,x2[0]+offset):
            if mat[i][j] == 0:
                return j,i
    return x2[0]+offset, y2[0]+offset

def find_up_right():
    for i in range(y2[0]+offset-1,y1[0]+offset-1,-1):
        for j in range(x2[0]+offset-1,x1[0]+offset-1,-1):
            if mat[i][j] == 0:
                return j+1,i+1
    return x1[0] + offset, y1[0]+offset

bottom_left = find_bottom_left()
up_right = find_up_right()

rec_length = x2[0] - x1[0]
rec_height = y2[0] - y1[0]

length = up_right[0] - bottom_left[0]
height = up_right[1] - bottom_left[1]

if rec_length != length and rec_height != height:
    print(rec_length * rec_height)
elif rec_height == height and rec_length == length:
    print(0)
elif rec_length == length:
    if bottom_left[1] != (y1[0] + offset) and up_right[1] != y2[0] + offset:
        print(rec_length * rec_height)
    else:
        print(rec_length * (rec_height-height))
elif rec_height == height:
    if bottom_left[1] != (x1[0] + offset) and up_right[1] != x2[0] + offset:
        print(rec_length * rec_height)
    else:
        print((rec_length-length) * rec_height)

# for i in range(y1[0]+offset,y2[0]+offset):
#     for j in range(x1[0]+offset,x2[0]+offset):
#         print(mat[i][j],end=" ")
#     print()


            


        

