import java.util.PriorityQueue;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        //최소힙(MinHeap) 사용
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        //모든 음식을 최소힙으로 표현
        for (int i = 0; i < scoville.length; i++) {
            pq.add(scoville[i]);
        }

        while (true) {
            //가장 맵지 않은 음식
            int now = pq.poll();

            //스코빌 지수보다 낮을경우
            if (now < K) {

                //스코빌 지수를 K 이상으로 만들 수 없는 경우
                if (pq.peek() == null) {
                    answer = -1;
                    break;
                }
                //두 번째로 맵지 않은 음식
                int next = pq.poll();
                //섞은 음식의 스코빌 지수
                pq.add(now + (next * 2));
                answer++;
            } else {
                break;
            }
        }

        return answer;
    }
}