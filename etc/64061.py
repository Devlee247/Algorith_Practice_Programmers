def solution(board, moves):
    answer = 0
    temp = []
    for i in moves:
        for j in range(0, len(board)):
            if board[j][i-1] != 0:
                if len(temp) and temp[-1] == board[j][i-1]:
                    temp.pop()
                    answer += 2
                else:
                    temp.append(board[j][i-1])
                board[j][i-1] = 0
                break
            
    return answer
