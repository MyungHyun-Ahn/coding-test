def solution(answers):
    user1_count = 0
    user2_count = 0
    user3_count = 0
    for i in range(len(answers)):
        user1 = i%5+1
        if user1 == answers[i]:
            user1_count += 1
        
        if i % 2 == 0:
            user2 = 2
        else:
            if i%8 == 1:
                user2 = 1
            elif i%8 == 3:
                user2 = 3
            elif i%8 == 5:
                user2 = 4
            elif i%8 == 7:
                user2 = 5
        if user2 == answers[i]:
            user2_count += 1
        if i%10 == 0 or i%10 == 1:
            user3 = 3
        elif i%10 == 2 or i%10 == 3:
            user3 = 1
        elif i%10 == 4 or i%10 == 5:
            user3 = 2
        elif i%10 == 6 or i%10 == 7:
            user3 = 4
        elif i%10 == 8 or i%10 == 9:
            user3 = 5
        if user3 == answers[i]:
            user3_count += 1
    answer_user = []
    max_count = max(user1_count, user2_count, user3_count)
    if max_count == user1_count:
        answer_user.append(1)
    if max_count == user2_count:
        answer_user.append(2)
    if max_count == user3_count:
        answer_user.append(3)    
    return answer_user

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))