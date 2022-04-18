def solution(numbers):
    sum = 45
    for i in range(len(numbers)):
        sum -= numbers[i]
    return sum

print(solution([1,2,3,4,6,7,8,0]))
print(solution([5,8,4,0,6,7,9]))