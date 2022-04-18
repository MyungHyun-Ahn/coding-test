def solution(new_id):
    answer = ""

    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] >= 'a' and new_id[i] <= 'z':
            answer = answer + new_id[i]
        elif new_id[i] >= '0' and new_id[i] <='9':
            answer = answer + new_id[i]
        elif new_id[i] == '-' or new_id[i] == '_' or new_id[i] == '.':
            answer = answer + new_id[i]
        else: pass
    answer2 = ""
    for i in range(len(answer)-1):
        if answer[i] == '.' and answer[i+1] == '.':
            pass
        else:
            answer2 = answer2 + answer[i]
    
    answer2 = answer2 + answer[len(answer)-1]

    answer2 = answer2.strip('.')

    if answer2 == "":
        answer2 = 'a'
    
    if len(answer2) > 15:
        answer2 = answer2[:15]
        answer2 = answer2.strip('.')
    
    if len(answer2) < 3:
        while len(answer2) < 3:
            answer2 = answer2 + answer2[len(answer2)-1]

    return answer2

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))