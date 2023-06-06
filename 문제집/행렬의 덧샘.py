def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        temp = [] #임시 리스트
        for j in range(len(arr1[0])):
            temp.append(arr1[i][j]+arr2[i][j])
        answer.append(temp)
    
    return answer

print(solution([[1,2],[2,3]],[[3,4],[5,6]]))

