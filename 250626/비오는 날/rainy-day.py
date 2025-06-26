n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Please write your code here.
class Weather_data:
    def __init__(self,date,day,weather):
        self.date = date
        self.day = day
        self.weather = weather

data = [Weather_data(date[i],day[i],weather[i]) for i in range(n)]

first = Weather_data("2100-12-31",0,0)
for weather in data:
    if first.date > weather.date and weather.weather == "Rain":
        first = weather

print(first.date,first.day,first.weather)
