def solution(board, moves):
    stack = [0]
    count = 0
    for i in range(len(moves)):
        for j in range(len(board[0])):
            if board[j][moves[i]-1] != 0:
                if stack[len(stack)-1] == board[j][moves[i]-1]:
                    stack.pop(len(stack)-1)
                    count += 2
                else:
                    stack.append(board[j][moves[i]-1])
                
                board[j][moves[i]-1] = 0
                break
    return count


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))