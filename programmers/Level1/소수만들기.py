def solution(nums):
    num_list = []
    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                num_list.append(nums[i]+nums[j]+nums[k])
    count = 0

    for i in range(len(num_list)):
        is_s = 0
        for j in range(2, int(num_list[i])):
            if num_list[i] % j == 0:
                is_s = 1
                break
        if is_s == 0:
            count += 1
    return count

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))