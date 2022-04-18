
def solution(numbers, hand):
    phone_dict = {
        1 : [0, 0],
        2 : [0, 1],
        3 : [0, 2],
        4 : [1, 0],
        5 : [1, 1],
        6 : [1, 2],
        7 : [2, 0],
        8 : [2, 1],
        9 : [2, 2],
        '*' : [3, 0],
        0 : [3, 1],
        '#' : [3, 2],
    }

    left_hand = [3, 0]
    right_hand = [3,2]
    answer = ""

    for i in range(len(numbers)):
        if numbers[i] == 1 or numbers[i] == 4 or numbers[i] == 7:
            left_hand = phone_dict[numbers[i]]
            answer = answer + 'L'
        elif numbers[i] == 3 or numbers[i] == 6 or numbers[i] == 9:
            right_hand = phone_dict[numbers[i]]
            answer = answer + 'R'
        else:
            l_a = abs(phone_dict[numbers[i]][0] - left_hand[0])
            l_b = abs(phone_dict[numbers[i]][1] - left_hand[1])
            l_len = l_a + l_b

            r_a = abs(phone_dict[numbers[i]][0] - right_hand[0])
            r_b = abs(phone_dict[numbers[i]][1] - right_hand[1])
            r_len = r_a + r_b

            if l_len < r_len:
                left_hand = phone_dict[numbers[i]]
                answer = answer + 'L'
            elif l_len > r_len:
                right_hand = phone_dict[numbers[i]]
                answer = answer + 'R'
            else:
                if hand == "right":
                    right_hand = phone_dict[numbers[i]]
                    answer = answer + 'R'
                elif hand == "left":
                    left_hand = phone_dict[numbers[i]]
                    answer = answer + 'L'
                else:
                    pass

            

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))