# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946

from itertools import permutations

def solution(k, dungeons):
    dun_num = len(dungeons) # 던전의 개수
    answer = 0
    
    for permut in permutations(dungeons, dun_num): #던전 개수만큼 순열을 구해줌
        hp = k #현재 피로도
        count = 0
        for pm in permut:
            if hp >= pm[0]: #현재 피로도가 던전의 최소 피로도보다 높은지 확인
                hp -= pm[1] #위에 검사 통과하면 소모피로도 차감
                count += 1  #던전 클리어 횟수 증가
        if count > answer:  #순열의 모든 경우의수를 완전탐색하여 가장 큰 count를 구해줌
            answer = count
    
    return answer