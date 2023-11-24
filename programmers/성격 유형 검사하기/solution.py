// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/118666

def solution(survey, choices):
    dic = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    score = [0, 3, 2, 1, 0, 1, 2, 3]

    for i in range(len(survey)):
        s = survey[i]
        if choices[i] > 4:
            dic[s[1]] += score[choices[i]]
        elif choices[i] < 4:
            dic[s[0]] += score[choices[i]]

    answer = ""
    answer += "R" if dic["R"] >= dic["T"] else "T"
    answer += "C" if dic["C"] >= dic["F"] else "F"
    answer += "J" if dic["J"] >= dic["M"] else "M"
    answer += "A" if dic["A"] >= dic["N"] else "N"

    return answer