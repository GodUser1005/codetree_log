n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Please write your code here.
students = [(name[i],height[i],weight[i]) for i in range(n)]
students.sort(key=lambda x: x[1])
for student in students:
    name, height, weight = student
    print(name,height,weight)