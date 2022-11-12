import collections
def solution(id_list, report, k):
    answer = []
    
    report = list(set(report))
    reportHash = collections.defaultdict(set)
    stopped = collections.defaultdict(int) #기본적으로 0으로 초기화됨

    for x in report:
        a, b = x.split(' ')
        reportHash[a].add(b)
        stopped[b] += 1
    
    
    
    return answer