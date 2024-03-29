from collections import defaultdict
from collections import deque

def solution(n, edge):
    graph = defaultdict(list)
    for node in edge:
        graph[node[0]].append(node[1])
        graph[node[1]].append(node[0])

    q = deque()
    q.append([1, 0])

    dist = [-1 for _ in range(n+1)]
    dist[1] = 0

    answer = 0
    answer_list = []

    while q:
        v, w = q.popleft()
        for u in graph[v]:
            if dist[u] == -1:
                q.append([u, w+1])
            dist[u] = max(dist[u], w+1)
            
            if dist[u] > answer:
                answer = dist[u]
                answer_list = [v]
            elif dist[u] == answer:
                answer_list.append(v)

    answer_list = list(set(answer_list))
    return len(answer_list)
