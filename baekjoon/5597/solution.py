// [문제 링크]: https://www.acmicpc.net/problem/5597

from collections import defaultdict
​
ans = []
student = defaultdict(int)
for _ in range(28):
    student[int(input())] = 1
​
for i in range(1, 31):
    if student[i] == 0:
        ans.append(i)
        
for a in ans:
    print(a)