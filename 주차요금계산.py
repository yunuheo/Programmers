import math
def solution (fees, records):
    answer = []
    inTime = [0]*10000
    isIn = [0]*10000
    sumT = [0]*10000

    for record in recoreds:
        a, b, c = record.split() #공백이 구분자
        h, m = a.split(":")
        if c == 'IN':
            inTime[int(b)] = int(b)*60+int(m)
            isIn[int(b)] = 1
        else:
            sumT[int[b]] += ((int(h))*60+int(m)) - inTime[int(b)]
            isIn[int(b)] = 0
    
    for i in range(10000):
        if isIn[i] == 1:
            sumT[i] += (23*60+59) - inTime[i]

    for i in range(10000):
        if sumT[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumT[i]-fees[0])/fees[2]),0)*fees[3])

    return answer

