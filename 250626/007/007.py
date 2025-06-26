secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.
class schedule:
    def __init__(self, secret_code, meeting_point, time):
        self.secret_code = secret_code
        self.meeting_point = meeting_point
        self.time = time

schedule_ = schedule(secret_code,meeting_point,time)
print(f"secret code : {schedule_.secret_code}")
print(f"meeting point : {schedule_.meeting_point}")
print(f"time : {schedule_.time}")