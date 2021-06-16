import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville:
        heapq.heappush(heap, i)
    while heap[0] < K:
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        new_scoville = a + (b * 2)
        heapq.heappush(heap, new_scoville)
        answer += 1
        if len(heap) == 1 and heap[0] < K:
            answer = -1
            break

    return answer
