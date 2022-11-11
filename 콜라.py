def solution(a, b, n):
    answer = 0
    temp = 0
        
    if a == n:
        return b
    
    while True:
        answer += (n//a)*b
        n = n%a
        temp += n % a
        if n<a:
           if (n+temp) >= a:
               answer += ((n+temp)//a)*b
               break
           
           break
    return answer

print(solution(6,2,20))
               