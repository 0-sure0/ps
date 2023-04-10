// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):

    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            tmp = 0
            if j - 1 >= 0:
                tmp = max(tmp, triangle[i - 1][j - 1])
            if j < len(triangle[i - 1]):
                tmp = max(tmp, triangle[i - 1][j])
            triangle[i][j] += tmp
    return max(triangle[-1])