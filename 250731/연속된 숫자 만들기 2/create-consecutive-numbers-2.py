pos = list(map(int, input().split()))

# Please write your code here.
pos.sort()

if pos[2] - pos[0] == 2:
    print(0)
# elif pos[1]-pos[0] == 1:
#     next_0 = pos[2] - 2
#     next_1 = pos[2] - 1
#     print(next_0 - pos[0] + next_1 - pos[1])
# elif pos[2]-pos[1] == 1:
#     next_2 = pos[0] + 2
#     next_1 = pos[0] + 1
#     print(pos[1] - next_1 + pos[2] - next_2)
# else:
#     next_0 = pos[2] - 2
#     next_1 = pos[2] - 1
#     ans_1 = next_0 - pos[0] + next_1 - pos[1]

#     next_2 = pos[0] + 2
#     next_1 = pos[0] + 1
#     ans_2 = pos[1] - next_1 + pos[2] - next_2
#     print(min(ans_1,ans_2))
else:
    print(2)