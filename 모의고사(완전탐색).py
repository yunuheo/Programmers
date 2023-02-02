'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42840
'''
def solution(answers):
    answer = []
    
    num1 = [1,2,3,4,5]
    num2 = [2,1,2,3,2,4,2,5]
    num3 = [3,3,1,1,2,2,4,4,5,5]
    
    def check(who):
        cnt = 0
        j = 0
        for i in range(len(answers)):
            if j >= len(who):
                    j = 0
            if answers[i] == who[j]:
                        cnt += 1
            j += 1
        return cnt
    
    if max(check(num1),check(num2),check(num3)) == check(num1):
        answer.append(1)
    if max(check(num1),check(num2),check(num3)) == check(num2):
        answer.append(2)
    if max(check(num1),check(num2),check(num3)) == check(num3):
        answer.append(3)
    
    if len(answer) > 1:
        return answer
    else:
        return answer

print(solution([1, 3, 2, 4, 2]))