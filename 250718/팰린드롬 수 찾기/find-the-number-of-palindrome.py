X, Y = map(int, input().split())

# Please write your code here.
def is_pallendrom(x):
    x_list = list(str(x))
    x_list_reverse = x_list[::-1]
    for i in range(len(x_list)):
        if x_list[i] != x_list_reverse[i]:
            return False
    return True

cnt = 0
for i in range(X,Y+1):
    if is_pallendrom(i):
        cnt += 1
print(cnt)