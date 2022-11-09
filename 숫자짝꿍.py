def solution(x, y):

    answer = ''
    answer_list = []
    
    for i in x:
        for j in y:
            if i == j:
                answer_list.append(i)
                y.replace(j,'',1)
                break
    answer_list.sort(reverse=True)
    if len(answer_list) == 0:
        return '-1'
    if answer_list[0] == "0":
        return '0'
        #배열 요소들을 조합하여 최대값 구하는 로직
    
    answer = "".join(answer_list)    
    return answer

print(solution("5525","1255"))

