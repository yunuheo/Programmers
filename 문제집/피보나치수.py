#리스트 두개를 더하는 것으로 해결
def solution(n):
    answer = [0,1]
    for i in range(n-1):
        answer.append(answer[i] +answer[i+1])
    return answer[-1]%1234567

# 재귀함수를 이용한 첫 번재 풀이에서는 시간초과 발생
# def solution(n):
    
#     answer = 0
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
    
    
#     answer = solution(n-2) + solution(n-1)

#     return (answer % 1234567)

# print(solution(5))
