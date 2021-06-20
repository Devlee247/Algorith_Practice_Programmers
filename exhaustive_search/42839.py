from itertools import permutations
import math
def solution(numbers):
    answer = 0
    number = []
    s = set()
    for i in numbers:
        number.append(int(i))
    for i in range(1, len(number)+1):
        print(i)
        temp = list(permutations(number, i))
        for j in temp:
            new_str = ''
            for k in j:
                new_str += str(k)
            s.add(int(new_str))
    for i in s:
        count = 0
        if i < 2:
            continue
        for j in range (2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                count += 1
        if count == 0:
            answer += 1
    return answer
