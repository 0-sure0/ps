// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    dp = [set() for _ in range(9)]

    for i in range(1, 9):
        if int(str(N) * i) == number:
            return i
        tmp = set([int(str(N) * i)])
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    if op1 + op2 == number:
                        return i
                    tmp.add(op1 + op2)

                    if op1 - op2 == number:
                        return i
                    tmp.add(op1 - op2)

                    if op1 * op2 == number:
                        return i
                    tmp.add(op1 * op2)

                    if op2 != 0:
                        if op1 // op2 == number:
                            return i
                        tmp.add(op1 // op2)
        dp[i] = tmp
    return -1