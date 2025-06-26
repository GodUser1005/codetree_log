unlock_code, wire_color, seconds = input().split()
seconds = int(seconds)

# Please write your code here.
class Bomb:
    def __init__(self,unlock_code,wire_color,seconds):
        self.unlock_code = unlock_code
        self.wire_color = wire_color
        self.seconds = seconds

bomb = Bomb(unlock_code,wire_color,seconds)
print(f"code : {bomb.unlock_code}\ncolor : {bomb.wire_color}\nsecond : {bomb.seconds}")