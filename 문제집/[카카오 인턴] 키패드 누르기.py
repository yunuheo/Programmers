'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/67256
'''

def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
           4: [1, 0], 5: [1, 1], 6: [1, 2],
           7: [2, 0], 8: [2, 1], 9: [2, 2],
           '*':[3, 0], 0: [3, 1], '#': [3, 2]}

    
    left_s = dic['*']
    right_s = dic['#']

    for number in numbers:
        if number == 1 or number == 4 or number == 7: # if i in [1,4,7] 로 바꿔서 쓸 수 있다.
            answer += 'L'
            left_s = dic[number]
        elif number == 3 or number == 6 or number == 9:
            answer += 'R'
            right_s = dic[number]
        else:
            current = dic[number]
            #좌표 사이의 거리를 계산함
            #zip() 함수를 이용한 더 짧은 코드(출처: https://bladejun.tistory.com/115)
            '''
            for a, b, c in zip(left_s, right_s, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            '''
            #내가 구현한 코드
            if abs(current[0]-left_s[0])+abs(current[1]-left_s[1]) < abs(current[0]-right_s[0]) + abs(current[1]-right_s[1]):
                answer += 'L'
                left_s = dic[number]
            elif abs(current[0]-left_s[0])+abs(current[1]-left_s[1]) > abs(current[0]-right_s[0]) + abs(current[1]-right_s[1]):
                answer += 'R'
                right_s = dic[number]
            else:
                if hand == 'left':
                    answer += 'L'
                    left_s = dic[number]
                else:
                    answer +='R'
                    right_s = dic[number]
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0],"right"))