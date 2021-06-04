def solution(brown, yellow):
    answer = []
    ab = brown + yellow
    for i in range(ab, 0, -1):
        a = i
        b = int(ab / i)
        if a*b == ab and a >= b:
            if (2*a+2*b-4) == brown and (a-2)*(b-2) == yellow:
                answer = [a,b]
    return answer
