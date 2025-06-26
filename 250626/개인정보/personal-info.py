n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Please write your code here.

class Student:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = height
        self.weight = weight

students = [Student(name[i],height[i],weight[i]) for i in range(5)]
students.sort(key=lambda student: student.name)
print("name")
for student in students:
    print(student.name,student.height,student.weight)
print()
print("height")
students.sort(key=lambda student: -student.height)
for student in students:
    print(student.name,student.height,student.weight)

