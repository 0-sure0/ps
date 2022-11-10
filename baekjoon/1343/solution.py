// [문제 링크]: https://www.acmicpc.net/problem/1343

import sys
#sys.stdin = open("test.txt", "r")
input = sys.stdin.readline
​
​
def solution():
    global board
    ans = ""
    tmp = ""
    for i in range(len(board)):
        if board[i] == 'X':
            tmp += board[i]
        else:
            if tmp == "":
                ans += board[i]
                continue
            if len(tmp) % 2 != 0:
                print(-1)
                return
            else:
                length = len(tmp)
                if length % 4 == 0:
                    ans += 'AAAA' * (length // 4)
​
                else:
                    cnt = 0
                    while length:
                        length -= 2
                        cnt += 1
                        if length % 4 == 0:
                            ans += 'AAAA' * (length // 4) + 'BB' * cnt
                            break
            tmp = ""
            ans += board[i]
​
    if tmp != "":
        length = len(tmp)
        if length % 4 == 0:
            ans += 'AAAA' * (length // 4)
​
        else:
            cnt = 0
            while length:
                length -= 2
                cnt += 1
                if length % 4 == 0:
                    ans += 'AAAA' * (length // 4) + 'BB' * cnt
                    break
​
    print(ans)
​
    return
​
board = input()
solution()
​