import math
def solution (fees, records):
    answer = []
    inTime = [0]*10000
    isIn = [0]*10000
    sumT = [0]*10000

    for record in records:
        a, b, c = record.split() #공백이 구분자
        h, m = a.split(":")
        if c == "IN":
            inTime[int(b)] = int(h)*60+int(m)
            isIn[int(b)] = 1
        else:
            sumT[int(b)] += (int(h)*60+int(m)) - inTime[int(b)]
            isIn[int(b)] = 0
    
    for i in range(10000):
        if isIn[i] == 1:
            sumT[i] += (23*60+59) - inTime[i]

    for i in range(10000):
        if sumT[i] > 0:
            answer.append(fees[1] + max(math.ceil((sumT[i]-fees[0])/fees[2]),0)*fees[3])

    return answer

print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))

