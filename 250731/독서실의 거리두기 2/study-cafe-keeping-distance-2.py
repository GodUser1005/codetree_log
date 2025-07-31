n = int(input())
seats = list(input())

# Please write your code here.
positions = [i for i,seat in enumerate(seats) if seat == '1']
diff = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
if 1 in diff:
    print(1)
else:
    diff.sort()
    min_diff = diff[-1] // 2
    max_near_diff = min_diff
    if len(diff) >= 2:
        min_diff = min(min_diff,diff[0])
        max_near_diff = min_diff
    if seats[n-1] == '0':
        min_diff = min(diff[-1],n-1 - positions[-1])
    print(max(max_near_diff,min_diff))