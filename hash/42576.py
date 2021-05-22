def solution(participant, completion):
    answer = ''
    count = dict()
    
    for i in participant:
        try:
            count[i] += 1
        except:
            count[i] = 1
    for i in completion:
        count[i] -= 1
    for i in count:
        if count[i] is 1:
            answer = i
    return answer
