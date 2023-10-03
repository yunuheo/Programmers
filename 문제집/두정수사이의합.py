# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/12912

def solution(a, b):
    answer = 0
    
    array = [a,b]
    
    array.sort()  # 오름차순 정렬
    
    if array[0] == array[-1]:  # a와 b가 같으면 둘 중 아무거나 출력
        answer = array[0]
    else:
        for i in range(array[0],array[-1]+1): #range()를 통해 a와 b사이의 정수를 합함
            answer += i
    return answer