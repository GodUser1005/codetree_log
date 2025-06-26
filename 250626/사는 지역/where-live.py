n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Please write your code here.
class Person:
    def __init__(self,name,street_address,region):
        self.name = name
        self.street_address = street_address
        self.region = region

people = [Person(name[i],street_address[i],region[i]) for i in range(n)]

result = people[0]
for person in people[1:]:
    if result.name < person.name:
        result = person

print(f"name {result.name}\naddr {result.street_address}\ncity {result.region}")