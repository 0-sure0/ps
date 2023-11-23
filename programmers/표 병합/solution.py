// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/150366

merged = [[(r, c) for c in range(51)] for r in range(51)]
content = [["EMPTY"] * 51 for _ in range(51)]


def update(command):
    r, c, value = command
    r = int(r)
    c = int(c)

    tr, tc = merged[r][c]
    content[tr][tc] = value
    return


def update_by_value(command):
    value1, value2 = command

    for r in range(1, 51):
        for c in range(1, 51):
            if content[r][c] == value1:
                content[r][c] = value2
    return


def merge(command):
    r1, c1, r2, c2 = map(int, command)
    r1, c1 = merged[r1][c1]
    r2, c2 = merged[r2][c2]

    if (r1, c1) == (r2, c2):
        return

    if content[r1][c1] == "EMPTY":
        content[r1][c1] = content[r2][c2]

    for r in range(1, 51):
        for c in range(1, 51):
            if merged[r][c] == (r2, c2):
                merged[r][c] = (r1, c1)
    return


def unmerge(command):
    r, c = map(int, command)
    tr, tc = merged[r][c]
    value = content[tr][tc]

    for i in range(1, 51):
        for j in range(1, 51):
            if merged[i][j] == (tr, tc):
                merged[i][j] = (i, j)
                content[i][j] = "EMPTY"

    content[r][c] = value
    return


def p(command):
    r, c = map(int, command)
    r, c = merged[r][c]
    return content[r][c]


def solution(commands):
    answer = []
    for command in commands:
        command = command.split()
        order = command[0]
        if order == "UPDATE":
            if len(command) == 4:
                update(command[1:])
            else:
                update_by_value(command[1:])

        elif order == "MERGE":
            merge(command[1:])

        elif order == "UNMERGE":
            unmerge(command[1:])

        elif order == "PRINT":
            answer.append(p(command[1:]))
    return answer