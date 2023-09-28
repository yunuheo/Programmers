# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    player_dict = {player: idx for idx, player in enumerate(players)} #딕셔너리의 key, value 선수이름, index로 매핑(enumerate())
    
    for call in callings:
        idx = player_dict[call]
        
        players[idx], players[idx-1] = players[idx-1], players[idx] # 추월한 선수, 추월 당한 선수 위치 바꿈
        
        #선수 딕셔너리 위치 조정
        player_dict[players[idx]] = idx 
        player_dict[players[idx-1]] = idx-1
    
    return players