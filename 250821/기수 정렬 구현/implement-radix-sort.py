def ith_digit_string(num,i):
    i = 5-i
    return int(f"{num:0>6d}"[i])

def ith_digit_math(num,i):
    return (num // (10**i)) % 10

def radix_sort(arr):
    for i in range(6):
        list_arr = [[] for _ in range(10)]
        for num in arr:
            list_arr[ith_digit_string(num,i)].append(num)

        new_arr = []
        for j in range(10):
            row_list = list_arr[j]
            for k in range(len(row_list)):
                new_arr.append(row_list[k])
        arr = new_arr
    return arr

n = int(input())
arr = list(map(int, input().split()))
answer = " ".join(list(map(str,radix_sort(arr))))

# Please write your code here.
print(answer)
