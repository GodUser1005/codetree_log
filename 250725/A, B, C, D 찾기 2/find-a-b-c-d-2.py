MAX_N = 40
arr = list(map(int,input().split()))
arr.sort()

def find_a_b_c_d(arr):
    for a in range(1,MAX_N+1):
        for b in range(a,MAX_N+1):
            for c in range(b,MAX_N+1):
                for d in range(c,MAX_N+1):
                    tmp = [a,b,c,d]
                    avail = []
                    for i in range(len(tmp)):
                        avail.append(tmp[i])
                    
                    for i in range(len(tmp)):
                        for j in range(i+1,len(tmp)):
                            avail.append(tmp[i]+tmp[j])
                    
                    for i in range(len(tmp)):
                        sum_ = 0
                        for j in range(len(tmp)):
                            if i != j:
                                sum_ += tmp[j]
                        avail.append(sum_)
                    
                    avail.append(sum(tmp))
                    avail.sort()
                    is_equal = True
                    for i in range(len(avail)):
                        if avail[i] != arr[i]:
                            is_equal = False
                            break
                    if is_equal:
                        return tmp
    return 0

ans = find_a_b_c_d(arr)
if ans == 0:
    print(-1)
else:
    a,b,c,d = ans
    print(a,b,c,d)



                