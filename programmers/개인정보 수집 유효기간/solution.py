// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150370


def calc_time(t):
    t = list(map(int, t.split('.')))
    return t[0] * 12 * 28 + t[1] * 28 + t[2]


def solution(today, term, privacies):
    answer = []
    limit = {}
    today = calc_time(today)

    for t in term:
        d, t = t.split()
        limit[d] = int(t) * 28

    for i, v in enumerate(privacies, start=1):
        p, d = v.split()
        if today - calc_time(p) >= limit[d]:
            answer.append(i)

    return answer
