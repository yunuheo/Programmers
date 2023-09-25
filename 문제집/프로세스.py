# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3

from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque(priorities)
    while q:
        m = max(q)
        l = q.popleft()
        location -= 1
        if l != m:
            q.append(l)
            if location < 0:
                location = len(q) -1
        else:
            answer += 1
            if location < 0:
                break
    return answer