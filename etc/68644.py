def solution(numbers):
    answer = []
    for i,j in enumerate(numbers):
        for j in range(i+1, len(numbers)):
            sum_numbers = numbers[i] + numbers[j]
            if sum_numbers not in answer:
                answer.append(sum_numbers)
    
    answer.sort()
    
    return answer
