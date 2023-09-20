def solution(absolutes, signs):
    
    
    answer = 0

    for i in range(len(signs)):
        if signs[i] == True:
            signs[i] = 1
        else:
            signs[i] = -1
    
    for j in range(len(absolutes)):
        answer = answer + (absolutes[j] * signs[j])
    print(answer)
    return answer

solution([4,7,12],[True,False,True])