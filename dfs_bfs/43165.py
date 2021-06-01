def solution(numbers, target):
    answer = 0
    def DFS(index, sum_numbers):
        if index == len(numbers):
            if sum_numbers == target:
                return 1
            else:
                return 0
        
        ret = 0
        ret += DFS(index+1, sum_numbers + numbers[index])
        ret += DFS(index+1, sum_numbers - numbers[index])
        
        return ret
    
    answer = DFS(0, 0)
    
    return answer
