def solution(n, computers):
    answer = 0

    visited = []
    queue = []
    
    for i in range(0, n, 1):
        if i in visited:
            continue
        queue.append(i)
        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.append(node)
                temp = []
                for j, k in enumerate(computers[node]):
                    if j != node and k == 1:
                        temp.append(j)
                queue.extend(temp)
        answer += 1
    return answer
