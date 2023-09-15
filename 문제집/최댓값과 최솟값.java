import java.util.Arrays;
class Solution {
    public String solution(String s) {
        String answer = "";

        //공백 기준으로 스플릿
        String[] stChange1 = s.split("\\s");

        int[] intArr = new int[stChange1.length];
        // int 배열로 재가공
        for (int i = 0; i < stChange1.length; i++) {
            intArr[i] = Integer.parseInt(stChange1[i]);
        }

        //오름차순 정렬
        Arrays.sort(intArr);

        //최소값 최대값을 담아둘 변수 2개 선언
        String str1 = Integer.toString(intArr[0]);
        answer += str1 + " ";
        String str2 = Integer.toString(intArr[intArr.length-1]);
        answer += str2;

        return answer;
    }
}