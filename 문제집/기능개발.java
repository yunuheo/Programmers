import java.util.ArrayList;
import java.util.LinkedList; //import
import java.util.Queue; //import
class Solution {
    public int[] solution(int[] progresses, int[] speeds) {


        //각 작업의 배포날짜
        //int [] release = new int [progresses.length];
        Queue<Integer> release = new LinkedList<>();

        for (int i = 0; i < progresses.length; i++) {
            int cnt = 0;
            int tmp = progresses[i];
            while (true) {
                if (tmp < 100) {
                    tmp += speeds[i];
                    cnt += 1;
                } else {
                    release.add(cnt);
                    break;
                }

            }
        }

        ArrayList<Integer> arr = new ArrayList<>(); // 결과를 담을 배열
        int cnt = 1;
        int now = release.poll(); // 첫번째 항목을 꺼냄
        while(!release.isEmpty()){
            int next = release.poll();    // 현재 작업일과 다음 작업일을 비교하기 위해 값을 꺼냄
            if(now >= next) cnt++;  // 만일 현재 작업일이 더 많을 경우 cnt증가
            else{                   // 현재 작업일이 작은경우
                arr.add(cnt);       // 배열에 계산한 cnt추가
                now = next;         // 현재 작업일을 next로 교체
                cnt = 1;            // cnt초기화
            }
        }
        arr.add(cnt);               // 마지막 cnt는 추가가 안됨으로 따로 추가

        // ArrayList를 배열로 변환
        int[] answer = new int[arr.size()];
        for(int i = 0; i < answer.length; i++){
            answer[i] = arr.get(i);
            //answer[i] = arr[i]; 처럼 사용불가 ==> ArrayList의 개별원소에 접근하려면 get()메서드를 사용해야 함
        }
        return answer;
    }
}