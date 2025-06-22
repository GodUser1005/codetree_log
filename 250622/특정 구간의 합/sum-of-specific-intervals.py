n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def print_sequence_sum(a,b):
    s = 0
    for e in arr[a-1:b]:
        s += e
    print(s)

for query in queries:
    print_sequence_sum(query[0],query[1])
