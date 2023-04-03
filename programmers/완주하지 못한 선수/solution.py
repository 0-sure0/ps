// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42576

from collections import Counter


def solution(participant, completion):
    participant = Counter(participant)
    for c in completion:
        participant[c] -= 1

    for p, v in participant.items():
        if v == 1:
            return p