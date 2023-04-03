// [문제 링크]: https://school.programmers.co.kr/learn/courses/30/lessons/1845?language=python3

from itertools import combinations


def solution(nums):
    return min(len(set(nums)), len(nums) // 2)