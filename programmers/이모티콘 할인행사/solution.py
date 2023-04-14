// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    n = len(users)
    m = len(emoticons)

    sale_percent = product([40, 30, 20, 10], repeat=m)

    for sale in sale_percent:
        cnt = sale_price = 0
        for user in users:
            tmp = 0
            percent, limit = user
            for j in range(m):
                if sale[j] >= percent:
                    tmp += int(emoticons[j] * ((100 - sale[j]) * 0.01))

            if tmp >= limit:
                cnt += 1
            else:
                sale_price += tmp

        if cnt > answer[0] or (cnt == answer[0] and sale_price > answer[1]):
            answer = [cnt, sale_price]

    return answer