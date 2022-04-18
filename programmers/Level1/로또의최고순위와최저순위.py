def solution(lottos, win_nums):
    answer = []

    cur_num = 0
    zero_count = 0
    for i in range(6):
        if lottos[i] in win_nums:
            cur_num += 1
        if lottos[i] == 0:
            zero_count += 1
    
    answer.append(cur_num)
    cur_num = cur_num + zero_count
    answer.append(cur_num)

    for i in range(2):
        if answer[i] == 6:
            answer[i] = 1
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 2:
            answer[i] = 5
        else:
            answer[i] = 6

    return answer[::-1]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))