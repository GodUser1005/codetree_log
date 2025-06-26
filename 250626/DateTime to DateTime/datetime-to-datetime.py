a, b, c = map(int, input().split())

# Please write your code here.
time = ((a-11)*60*24 + b * 60 + c) - (11*60 + 11)
print(time if time >= 0 else -1)