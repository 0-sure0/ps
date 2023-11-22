
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
