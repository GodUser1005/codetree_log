n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
max_value = 0

for i in range(n):
    for sell_price in price[i+1:]:
        max_value = sell_price - price[i] if max_value < sell_price - price[i] else max_value

print(max_value)