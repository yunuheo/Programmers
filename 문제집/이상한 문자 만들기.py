'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/12930
'''

def solution(s):
    answer = ''
    
    words = list(s.split(' '))  #공백을 기준으로 단어별로 리스트에 담기
    for word in words:
        for i in range(len(word)):
            if i%2 == 0:  #짝수번째면 대문자
                answer += word[i].upper()
            else:         #홀수번째면 소문자
                answer += word[i].lower()
        answer += ' '
    return answer[0:-1]   # 처음에는 rstrip()를 사용해줘서 불필요한 공백을 없애려 했으나 테스트 오류로 인해  [0:-1]로 공백을 제거함

print(solution('try hello world'))