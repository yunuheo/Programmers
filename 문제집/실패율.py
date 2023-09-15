'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42889
'''
def solution(N, stages):
    k = len(stages)
    s = []
    
    for i in range(1,N+1):  # 스테이지1 ~ 스테이지N
        c = 0
        for j in range(len(stages)):
            if stages[j] == i: # 해당 스테이지에 도달했지만 아직 클리어 하지 못한 경우
                c += 1
        if c == 0:          #스테이지에 도달한 유저가 없는 경우 0
            s.append(0)
        else:
            s.append(c/k)
        k = k - c
    
    a = sorted(s,reverse=True)
    answer = []
    
    for i in range(len(a)):
        answer.append(s.index(a[i])+1)  # s의 인덱스값으로 변환
        s[s.index(a[i])] = 2            # 중복값 제거
            
    return answer