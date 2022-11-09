def solution(x, y):

    answer = ''
    answer_list = []
    for i in (set(x) & set(y)):    #set()끼리 비교는 &(비교연산자) 사용
        for j in range(min(x.count(i),y.count(i))):  #짝꿍의 수가 일치하도록 min()함수 사용
            answer_list.append(i)
    answer_list.sort(reverse=True)
    if len(answer_list) == 0:
        return '-1'
    if answer_list[0] == "0":
        return '0'
        #배열 요소들을 조합하여 최대값 구하는 로직
    
    answer = "".join(answer_list)    
    return answer

