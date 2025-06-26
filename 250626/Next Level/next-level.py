user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self,user_id,level):
        self.user_id = user_id
        self.level = level

user_1 = User("codetree",10)
user_2 = User(user2_id,user2_level)

print(f"user {user_1.user_id} lv {user_1.level}")
print(f"user {user_2.user_id} lv {user_2.level}")
    