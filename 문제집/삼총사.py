def solution(number):
    lenth = len(number)

    answer = 0

    
    
    for i in range(0, lenth-2):
        
        for j in range(i+1, lenth-1):
          
          for k in range(j+1, lenth):
                
                if number[i] + number[j] + number[k] == 0:
                    answer += 1

    return answer


print(solution([-3, -2, -1, 0, 1, 2, 3]))
