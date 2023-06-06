
def solution(input_string):
    answer = ''
    dict ={}
    answer_list =[]
    for index, alphabet in enumerate(input_string):
        if alphabet not in dict:
            dict[alphabet] = [index]   #딕셔너리에 키값(alphabet)이 없으면 키값을 부여하고 index를 value값으로 대입
        else:
            dict[alphabet].append(index)  #동일한 키값이 있으면, 인덱스를 연달아 append
    
    #알파벳이 인접하지 않을 경우를 구해주는 for문
    for key, value in dict.items():
        if len(value) >= 2:
            for i in range(len(value)-1):
                if abs(value[i]-value[i+1])>1:
                    answer_list.append(key)
                    break   #인덱스의 차이가 1보다 큰게 하나라도 있으면 종료
    
    if len(answer_list) == 0:
        answer = "N"
    else:
        answer_list.sort()   
        answer =''.join(answer_list)  #리스트를 문자열형식으로 만들기 위해 join()함수 사용
    
    return answer

print(solution(""))
