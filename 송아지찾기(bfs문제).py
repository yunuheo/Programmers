from collections import deque
def solution(s, e):   #s가 현수의 위치 , e가 송아지의 위치
    answer = 0
    ch = [0]*100001

    #deque는 앞과 뒤에서 데이터를 처리할 수 있는 양방향 자료형이다.
    #스택처럼 써도 되고 큐처럼 써도 된다.
    dQ = deque()
    
    dQ.append(s)
    ch[s] = 1  #특정 노드 s를 방문했다고 체크해둠.
    L = 0 #트리에서 노드의 레벨(특정 레벨에서 송아지를 발견하면 그 레벨이 정답)
    while(dQ): #dq에 노드가 있으면 반복
        lenth = len(dQ)
        for _ in range(lenth):
            x = dQ.popleft()
            if x == e:
                return L
            for nx in [x-1, x+1, x+5]: #자식노드 생성
                if nx > 0 and nx <= 10000 and ch[nx] == 0:
                    ch[nx] = 1
                    dQ.append(nx)
        L += 1
    return answer


