def solution(numbers):
    answer = ''
    numbers_str = list(map(str, numbers))
    same_length = [[i, i * int(12 / len(i))] for i in numbers_str]
    same_length.sort(key = lambda x: x[1], reverse=True)
    for i in same_length:
        answer += i[0]
    answer = str(int(answer))
    return answer
