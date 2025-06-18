string = input()
cnt_arr = [0,0]
for i in range(0,len(string)-1):
    if string[i] == 'e':
        if string[i+1] == 'e':
            cnt_arr[0] += 1
        elif string[i+1] == 'b':
            cnt_arr[1] += 1

for cnt in cnt_arr:
    print(cnt,end=" ")
