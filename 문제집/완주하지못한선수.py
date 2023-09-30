# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    
    answer = ''
    
    dic = {}

    #이름 언급되면 +1
    for i in participant:
        
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    #완주하면 -1 해줌
    for i in completion:
        if i in dic:
            dic[i] -= 1
    #완주하지 못하면 0이 아닐테니 해당 value에 해당하는 key를 정답에 붙여줌
    for key, value in dic.items():
        if value != 0:
            answer += key
            
    return answer