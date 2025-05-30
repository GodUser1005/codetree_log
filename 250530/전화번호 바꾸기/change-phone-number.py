phone_num = input().split("-")
phone_num[1], phone_num[2] = phone_num[2],phone_num[1]
print(phone_num[0],phone_num[1],phone_num[2],sep="-")
