n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
min_price = price[0]
max_value = 0
for p in price[1:]:
    if p - min_price > max_value:
        max_value = p - min_price
    if min_price > p:
        min_price = p
print(max_value)