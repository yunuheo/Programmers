'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86051
'''

def solution(numbers):
    answer = 0
    
    for i in range(10):  
        if i in numbers:  
            continue
        answer += i  # 0~9의 숫자가 numbers에 없으면 더해줌
        
    return answer