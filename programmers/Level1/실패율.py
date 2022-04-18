def solution(N, stages):
    dict1 = {}

    for i in range(1, N + 1):
        clear_user = 0
        none_clear = 0
        for j in range(len(stages)):
            if stages[j] > i:
                clear_user += 1
            elif stages[j] == i:
                none_clear += 1
        if (clear_user + none_clear) == 0:
            p = 0
        else:
            p = none_clear / (clear_user + none_clear)
        dict1[i] = p
    answer = sorted(dict1.items(), key=lambda x: x[1], reverse=True)
    res = []
    for i in range(len(answer)):
        res.append(answer[i][0])

    return res

print(solution(5, [2,1,2,6,2,4,3,3]))
print(solution(4, 	[4,4,4,4,4]))