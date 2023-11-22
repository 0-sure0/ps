// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150368

from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    sales = [10, 20, 30, 40]
    for sale in product(sales, repeat=len(emoticons)):
        join = 0
        total_price = 0

        for percent, price in users:
            t = 0
            for sale_rate, emoticon in zip(sale, emoticons):
                if sale_rate >= percent:
                    t += emoticon * (1 - (sale_rate / 100))

            if t >= price:
                join += 1
            else:
                total_price += t

        answer = max(answer, [join, total_price])
    return answer
