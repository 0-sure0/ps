// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import defaultdict, deque

def solution(n, edge):
    graph = defaultdict(list)
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    def bfs():
        q = deque([1])
        checked[1] = 1
        cnt = 0
        while q:
            cnt = len(q)
            for _ in range(len(q)):
                node = q.popleft()
                for next_node in graph[node]:
                    if not checked[next_node]:
                        checked[next_node] = 1
                        q.append(next_node)
        return cnt

    checked = [0] * (n + 1)
    answer = bfs()
    return answer