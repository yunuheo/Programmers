'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/82612
'''
def solution(price, money, count):
    answer = 0
    for i in range(1,count+1):
        money -= (price*i)
    if money >= 0:  
        return answer
    return abs(money) #부족한 금액을 리턴