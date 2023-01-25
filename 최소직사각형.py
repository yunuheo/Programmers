def solution(sizes):
    answer = 0
    sorted_size = []
    for i in sizes: # index 0번과 1번을 내림차순으로 정렬하고 별도의 리스트에 저장
        i.sort(reverse=True)
        sorted_size.append(i)
    
    sorted_size.sort(key=lambda x: -x[0])  # 0번 index 중 가장 큰 값
    a = sorted_size[0][0]
    sorted_size.sort(key=lambda x:-x[1])   # 1번 index 중 가장 큰 값
    b = sorted_size[0][1]
    answer = a*b

    return answer

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))