def solution(nums):
    n = int(len(nums)/2)
    set_nums = set(nums)
    if len(set_nums) >= n:
        return n
    else:
        return len(set_nums)

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))
print(solution([3,3,3,2,2,2]))