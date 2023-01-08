'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/42862
'''


def solution(n, lost, reserve):
    answer = 0
    #여벌이 있으나 도난당한 학생을 빼주고, 중복된 요소를 없애기 위해 set 자료구조 사용
    reserve_set = set(reserve) - set(lost)
    lost_set = set(lost) - set(reserve)

    for i in reserve_set:
        if i-1 in lost_set:
            lost_set.remove(i-1) #체육복을 빌리면 lost_set에서 삭제
        elif i+1 in lost_set:
            lost_set.remove(i+1) #체육복을 빌리면 lost_set에서 삭제
    answer = n - len(lost_set)   #전체 학생수에서 여전히 lost_set에 남아 있는 학생수를 빼주자
    return answer


print(solution(5, [2, 4], [3]))
