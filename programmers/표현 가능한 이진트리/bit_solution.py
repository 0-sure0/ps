from math import ceil, log2

#인덱스 시작을 1로 가정
#자손 노드 접근 방법 -> 현재 인덱스를 x라 하자. a = x & (-x)
#왼쪽 자손: x - a // 2   
#오른쪽 자손: x + a // 2

def solution(numbers):
    def dfs(v: int, pow: int) -> int:
        if pow == 1:
            return True
        push_count = 2 ** (pow - 1) - 1
        left, mid, right = v >> (push_count + 1), (v >> push_count) & 1, v & (2 ** push_count - 1)
        if not mid and (left or right):
            return False
        return min(not left or dfs(left, pow - 1), not right or dfs(right, pow - 1))
    return [int(dfs(v, ceil(log2(ceil(log2(v + 1)) + 1)))) for v in numbers]
