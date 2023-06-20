// [문제 링크]: https://www.acmicpc.net/problem/18222

from sys import stdin
from math import log
​
​
def thue_morse(idx: int) -> int:
    if idx == 0:
        return 0
​
    x = int(log(idx, 2))
​
    val = 0
    while x > 0:
        if idx >= 2 ** x:
            val ^= 1
            idx %= 2 ** x
        x -= 1
​
    return [val, val ^ 1][idx == 1]
​
​
def main():
    k = int(stdin.readline())
    print(thue_morse(k - 1))
​
​
if __name__ == "__main__":
    main()