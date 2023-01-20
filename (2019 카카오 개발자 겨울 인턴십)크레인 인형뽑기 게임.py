'''
문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/64061
'''
def solution(board, moves):
    answer = 0

    basket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] > 0:
                basket.append(board[j][i-1])
                board[j][i-1] = 0

                if len(basket) > 1:
                    if basket[-1] == basket[-2]:  # 첫번째 요소부터 비교하면 불필요한 반복문을 사용해야함.
                        basket.pop(-1) # -1번째 요소를 리턴하고 삭제
                        basket.pop(-1)
                        answer += 2

                break

    return answer


print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [
      4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4]))