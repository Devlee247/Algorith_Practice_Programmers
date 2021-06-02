def solution(citations):
    answer = 0
    sorted_citations = sorted(citations, reverse=True)
    
    for i in range(sorted_citations[0], 0, -1):
        count = 0
        for j in sorted_citations:
            if j >= i:
                count += 1
            else:
                break
        if count >= i:
            answer = i
            break
    return answer
