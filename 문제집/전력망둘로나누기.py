'''
전력망(wires)을 트리 형태로 보고 간선 하나를 제거 할 때 
둘로 나눠진 전력망의 송전탑(n)의 개수의 차가 
가장 적은 것을 구하는 문제.
'''
cnt = 0
def DFS(v, ch, graph):
    global cnt #cnt는 전역변수라고 알려줘야함
    ch[v] = 1
    cnt += 1
    for i in graph[v]:
        if ch[i] == 0:
            DFS(i, ch, graph)

def solution(n, wires):
    global cnt #cnt는 전역변수라고 알려줘야함
    answer = n
    graph = [[] for _ in range(n+1)] #graph는 인접리스트
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v1, v2 in wires:
        ch = [0]*(n+1)
        ch[v2] = 1 #배열ch에 1을 넣으면 송전탑v2에 인접한 송전탑들은 DFS로 탐색하지 않음(=전력망이 2개로 나뉨)
        cnt = 0
        DFS(v1, ch, graph)
        answer = min(answer, abs(cnt - (n-cnt)))