def solution(seoul):
    answer = ''
    for i,j in enumerate(seoul):
        if j == 'Kim':
            answer = "김서방은 " + str(i) + "에 있다"
    return answer
