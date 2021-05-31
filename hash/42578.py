def solution(clothes):
    answer = 0
    closet = {}
    
    for i, j in clothes:
        if j not in closet:
            closet[j] = 1
        else:
            closet[j] += 1
    count = 1
    for i in closet:
        count *= closet[i] + 1
    answer = count - 1
    return answer
