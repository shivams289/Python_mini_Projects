# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import heapq
    

def solution(A, B):
    # write your code in Python 3.6
    dif = sum(A) - sum(B)

    if dif == 0:
        return 0
    elif dif < 0:
        min_hp, max_hp = A,B
    else:
        min_hp, max_hp = B,A
    
    dif = abs(dif)
    min_hp.sort()
    min_hp.sort()
    heapq.heapify(min_hp) 
    max_hp = [-i for i in max_hp]
    heapq.heapify(max_hp)
    count = 0
    val = 0

    while val<dif:
        val_min_heap = min_hp[0]
        val_max_heap = abs(max_hp[0])

        if val_min_heap == 6 and val_max_heap == 1:    
            return -1

        diff_if_min = 6 - val_min_heap 
        diff_if_max = val_max_heap - 1 
        count += 1
        val += max(diff_if_min, diff_if_max)

        if diff_if_min > diff_if_max:
            heapq.heappop(min_hp)
            heapq.heappush(min_hp,6)
        else:
            heapq.heappop(max_hp)
            heapq.heappush(max_hp,-1)
    
    return count
