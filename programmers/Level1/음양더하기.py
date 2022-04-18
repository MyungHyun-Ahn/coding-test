def solution(absolutes, signs):
    sum = 0
    for i in range(len(absolutes)):
        if signs[i] == True:
            sum = sum + absolutes[i]
        elif signs[i] == False:
            sum = sum - absolutes[i]
    return sum

print(solution([4,7,12], [True, False, True]))
print(solution([1,2,3], [False, False, True]))
