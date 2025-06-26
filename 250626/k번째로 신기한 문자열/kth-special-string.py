n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.
t_start_str = [element for element in str if element[:len(t)] == t]
t_start_str.sort()
print(t_start_str[k-1])