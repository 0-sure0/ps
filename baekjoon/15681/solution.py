// [문제 링크]: https://www.acmicpc.net/problem/15681

import sys
input = sys.stdin.readline
sys.setrecursionlimit(150000)
n,r,q=map(int,sys.stdin.readline().rstrip().split())
​
graph=[[] for i in range(n+1)]
visited=[0 for i in range(n+1)]
for i in range(n-1):
    a,b=map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
​
def DFS(v):
    visited[v]+=1
    for i in graph[v]:
        if visited[i]==0:
            visited[v]+=DFS(i)
    return visited[v]
​
DFS(r)
​
for i in range(q):
    a=int(input())
    print(visited[a])