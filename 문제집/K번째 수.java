import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];

        int n = 0;

        for (int i =0; i < commands.length; i++){
            //정수열 배열에서 값을 자르기 위해 copyOfRange()함수 사용
            int[] result = Arrays.copyOfRange(array, commands[i][0]-1, commands[i][1]);

            //오름차순 정렬
            Arrays.sort(result);
            answer[n++] = result[commands[i][2]-1];
        }

        return answer;
    }
}