// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118669

from collections import defaultdict
import heapq

def solution(n, paths, gates, summits):
    graph = defaultdict(list)
    summits = {s: 0 for s in sorted(summits)}

    for a, b, w in paths:
        graph[a].append((w, b))
        graph[b].append((w, a))

    def dijkstra():
        nonlocal answer

        intensity = [1e9] * (n + 1)
        q = []
        for gate in gates:
            intensity[gate] = 0
            heapq.heappush(q, (0, gate))

        while q:
            w, node = heapq.heappop(q)
            if w > intensity[node] or node in summits:
                continue

            for nw, next_node in graph[node]:
                t = max(w, nw)
                if intensity[next_node] > t:
                    intensity[next_node] = t
                    heapq.heappush(q, (t, next_node))

        for summit in sorted(summits):
            if intensity[summit] < answer[1]:
                answer = [summit, intensity[summit]]
        return

    answer = [1e9, 1e9]
    dijkstra()
    return answer