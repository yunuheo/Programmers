# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/43163

from collections import deque

def solution(begin, target, words):
    
    answer = 0
    q = deque()
    q.append([begin, 0])    #[단어, 깊이]
    V = [0] * (len(words))  # 단어의 검사 여부를 확인

    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]: #방문하지 않은 단어라면
                for j in range(len(word)):
                    if word[j] != words[i][j]: #검사하려고 하는 단어를 words의 모든 단어와 비교
                        temp_cnt += 1

                if temp_cnt == 1: # 만약 다른 글자가 1개라면
                    q.append([words[i], cnt+1]) # 단어를 q에 등록
                    V[i] = 1 # 해당 단어 방문했음을 기록
    return answer

