'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/77484
'''

def solution(lottos, win_nums):
    
    answer = []
    
    cnt = 0
    for i in lottos:
        for j in win_nums:
            if i == j:
                cnt += 1
    a = cnt
    
    cnt += lottos.count(0)
    
    b = cnt
    
    if b == 6:
        answer.append(1)
    elif b == 5:
        answer.append(2)        
    elif b == 4:
        answer.append(3)
    elif b == 3:
        answer.append(4)
    elif b == 2:
         answer.append(5)
    else:
        answer.append(6)        

    if a == 6:
        answer.append(1)
    elif a == 5:
        answer.append(2)
    elif a == 4:
        answer.append(3)
    elif a == 3:
        answer.append(4)
    elif a == 2:
        answer.append(5)
    else:
        answer.append(6)
    
    return answer

    '''
    다른 사람 풀이(출처: https://school.programmers.co.kr/learn/courses/30/lessons/77484/solution_groups?language=python3)
    
    solution(lottos, win_nums):
    rank = {
        0: 6,
        1: 6,
        2: 5,
        3: 4,
        4: 3,
        5: 2,
        6: 1
    }
    return [rank[len(set(lottos) & set(win_nums)) + lottos.count(0)], rank[len(set(lottos) & set(win_nums))]]

    '''