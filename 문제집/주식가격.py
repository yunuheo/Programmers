#문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42584

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        
        check = queue.popleft()

        sec = 0   
        for q in queue:  #마지막 pop 연산 후 빈큐 이므로 수행되지 않음
            sec += 1
            if check > q:
                break
        answer.append(sec)
        
    return answer