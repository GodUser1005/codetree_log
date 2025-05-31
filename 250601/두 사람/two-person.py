ages, genders = [],[]
is_in = 0
for _ in range(2):
    age, gender = input().split()
    age = int(age)
    if age >= 19 and gender == "M":
        is_in = 1
        print(is_in)
        break
if not is_in:
    print(is_in)
 