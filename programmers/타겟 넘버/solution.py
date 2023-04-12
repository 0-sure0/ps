// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/43165

def solution(numbers, target):
    answer = 0

    def dfs(i, path):
        nonlocal answer

        if i >= len(numbers):
            if target == sum(path):
                answer += 1
            return
        dfs(i + 1, path + [numbers[i]])
        dfs(i + 1, path + [-numbers[i]])
        return
    
    dfs(1, [numbers[0]])
    dfs(1, [-numbers[0]])

    return answer