def solution(n, lost, reserve):
    get = []
    reserve_lost = []
    for i in lost:
        if i in reserve:
            reserve.remove(i)
            reserve_lost.append(i)
    for i in reserve_lost:
        lost.remove(i)
    for i in lost:
        if i-1 in reserve:
            reserve.remove(i-1)
            get.append(i)
        elif i+1 in reserve:
            reserve.remove(i+1)
            get.append(i)
    answer = n - len(lost) + len(get)
    return answer
