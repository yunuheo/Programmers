#replace => 첫번째 인자로 전달받은 요소를 두번째 인자로 대체
#strip => strip()은 공백을 제거해줌

def solution(babbling):
    answer = 0
    for i in babbling:
        for b in ["aya","ye","woo","ma"]:
            if b*2 not in i:
                i = i.replace(b,' ')
        
        if len(i.strip()) == 0:
            answer += 1

    

    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))