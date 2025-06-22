n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

def max_element(n):
    if n == 1:
        return arr[0]
    
    return max(max_element(n-1),arr[n-1])

print(max_element(n))
    

