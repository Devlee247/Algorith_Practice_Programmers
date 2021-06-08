def solution(number, k):
    answer = ''
    stack = [number[0]]
    while k:
        for i in range(1, len(number)):
            if int(stack[-1]) >= int(number[i]):
                stack.append(number[i])
            else:
                while len(stack) and k and int(stack[-1]) < int(number[i]):
                    stack.pop(-1)
                    k -= 1
                stack.append(number[i])
        else:
            return ''.join(stack[:len(number)-k])
    return ''.join(stack)
