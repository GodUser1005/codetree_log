n = int(input())
seat = list(map(int,input()))

# Please write your code here.
max_near_dist = 0
for i in range(n):
    if seat[i] == 0:
        for j in range(i+1,n):
            if seat[j] == 0:
                tmp_seat = seat.copy()
                tmp_seat[i],tmp_seat[j] = 1,1
                seat_pos = [i for i in range(len(tmp_seat)) if tmp_seat[i] == 1]
                min_dist = n
                for i in range(len(seat_pos)-1):
                    dist = seat_pos[i+1]-seat_pos[i]
                    min_dist = min(dist,min_dist)
                max_near_dist = max(max_near_dist,min_dist)

print(max_near_dist)
                


