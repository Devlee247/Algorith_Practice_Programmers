import collections

def solution(tickets):
    graph = collections.defaultdict(list)

    for start,end in sorted(tickets):
        graph[start].append(end)
    
    print(graph)
    
    route = []
    def dfs(ticket):
        while graph[ticket]:
            dfs(graph[ticket].pop(0))
        route.append(ticket)

    dfs('ICN')
    return route[::-1]
