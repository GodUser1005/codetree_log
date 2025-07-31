n = int(input())
seats = list(input())

# Please write your code here.
positions = [i for i,seat in enumerate(seats) if seat == '1']
if len(positions) == 1:
    print(max(positions[0],n-1 - positions[0]))
else:
    diff = [positions[i+1]-positions[i] for i in range(len(positions)-1)]
    if 1 in diff:
        print(1)
    else:
        diff.sort()
        nearest_diff = diff[-1]//2
        if len(diff) >= 2:
            nearest_diff = min(nearest_diff,diff[0])
        if seats[-1] == '1':
            print(nearest_diff)
        else:
            min_diff = min(diff[0],n-1 - positions[-1])
            if seats[0] == '0':
                min_diff_2 = min(diff[0],positions[0])
                print(max(nearest_diff,min_diff,min_diff_2))
            else:
                print(max(nearest_diff,min_diff))
    