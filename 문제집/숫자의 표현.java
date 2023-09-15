class Solution {
    public int solution(int n) {
        int answer = 0;

        for (int i = 1; i <= n; i++) {
            int sum = 0;
            for (int j = i; j <= n; j++) {
                sum += j; //n이 곧바로 들어왔을 경우에도 검사해줘야 하므로 sum을 맨 위에 배치
                if (sum == n) {
                    answer += 1;
                    break;
                }

                //해당 if문 삭제시 효율성 테스트 통과 못함
                if (sum > n) {
                    break;
                }

            }
        }
        return answer;
    }
}