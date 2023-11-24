// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118667

from collections import deque


def solution(queue1, queue2):
    s1, s2 = sum(queue1), sum(queue2)
    q1 = deque(queue1)
    q2 = deque(queue2)
    answer = 0
    
    while q1 and q2 and s1 != s2 and answer < 600001:
        if s1 > s2:
            t = q1.popleft()
            s1 -= t
            s2 += t
            q2.append(t)
        else:
            t = q2.popleft()
            s2 -= t
            s1 += t
            q1.append(t)

        answer += 1

    return answer if s1 == s2 else -1