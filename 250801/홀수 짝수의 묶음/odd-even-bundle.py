n = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
odd_count = len([num for num in numbers if num % 2 == 1])
even_count = n - odd_count

basket_count = min(odd_count,even_count) * 2
if odd_count > even_count:
    odd_count -= even_count
    if odd_count % 3 == 0:
        basket_count += (odd_count // 3) * 2
    elif odd_count % 3 == 1:
        basket_count += (odd_count // 3) * 2 - 1
    elif odd_count % 3 == 2:
        basket_count += ((odd_count // 3) * 2 + 1)
else:
    basket_count += 1
print(basket_count)
