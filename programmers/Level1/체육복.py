def solution(n, lost, reserve):
    reserve_set = set(reserve)-set(lost) 
    lost_set = set(lost)-set(reserve) 
    
    for reserve_person in reserve_set: 
        if reserve_person-1 in lost_set: 
            lost_set.remove(reserve_person-1) 
        elif reserve_person+1 in lost_set: 
            lost_set.remove(reserve_person+1) 
    
    return n-len(lost_set)

print(solution(5, [2, 4], [1, 3, 5]))
print(solution(5, [2, 4], [3]))
print(solution(3, [3], [1]))