def solution(a, b, n):
    answer = 0
    temp = 0
    
    
    if a % b == 0:
        a = a//b
        b = b//b
        
    
    if a == n:
        return b
    
    while True:
        answer += (n//a)*b
        n = n//a
        temp += n % a
        if n<a:
           if (n+temp)%a == 0:
               answer += ((n+temp)//a)*b
           else:
               break
    return answer

print(solution(2,1,20))
               