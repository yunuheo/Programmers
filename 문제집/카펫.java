class Solution {
    public int[] solution(int brown, int yellow) {
        //int[] answer = new int[2];
        int[] answer = {0,0};
        int sum = brown + yellow; //전체 격자의 개수
        for (int i = 1; i <= sum; i++){
            int row = i;
            int col = sum / row;
            if (row > col) {
                continue;
            }
            if ((row-2)*(col-2) == yellow) {
                answer[0] = col;
                answer[1] = row;
                return answer;
            }
        }
        return answer;
    }
}