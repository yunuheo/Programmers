def solution(a, b, n):
    answer = 0
    temp = 0 #남아있는 병의 개수
      
    while True:
        if n<a:
           break  
        temp = n%a
        n = (n//a)*b

        answer += n
        
        n += temp
        
        
        
    return answer

print(solution(2,1,2))
print(solution(3,1,20))
print(solution(3,2,50))


