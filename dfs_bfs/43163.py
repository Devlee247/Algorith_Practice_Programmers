import sys
MAX_INT = 52372726
def compare(s1,s2):
    cnt = 0
    for i in range(len(s1)):
        if s1[i]!=s2[i]:
            cnt+=1
            if cnt==2 : return False
    return True

def solution(begin, target, words):
    visited = [0] * len(words)
    if target not in words : return 0

    def dfs(depth,word):
        if word == target: return depth

        ret = MAX_INT
        for i,w in enumerate(words):
            if compare(word,w) and visited[i]==0:
                visited[i]=1 
                ret = min(ret, dfs(depth+1, w))
                visited[i]=0 
        return ret

    ret = dfs(0,begin)

    if ret == MAX_INT:
        return 0
    else:
        return ret
