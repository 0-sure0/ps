// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43162

def solution(n, computers):
    answer = 0

    def dfs(node):
        checked[node] = 1

        for j in range(n):
            if node != j and computers[node][j] and not checked[j]:
                dfs(j)
                
        return

    checked = [0] * n
    for i in range(n):
        if not checked[i]:
            answer += 1
            dfs(i)

    return answer