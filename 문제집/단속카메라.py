def solution(routes):

    routes.sort(key = lambda x: x[1]) #나가는 지점을 기준으로 오름차순 정렬
    answer = 1 
    camera = routes[0][1] #초기 카메라 설치 지점 => 첫번째 차량이 나가는 지점
    
    for i in range(1, len(routes)):
        if camera < routes[i][0]:  #다음 차량의 진입지점이 카메라의 설치지점보다 뒤에 있으면
            camera = routes[i][1]  #해당 차량의 나가는 지점에 카메라를 위치시키자
            answer += 1  #카메라 개수 증가
                
    return answer

print(solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]))