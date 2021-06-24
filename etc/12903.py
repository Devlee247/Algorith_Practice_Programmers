def solution(s):
    answer = ''
    
    if len(s) % 2 == 0:
        index = int(len(s)/2)
        answer += s[index-1] + s[index]
    else:
        index = int(len(s)/2)
        answer += s[index]
    return answer
