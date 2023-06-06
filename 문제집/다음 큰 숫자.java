class Solution {
    public int solution(int n) {
        int answer = 0;
        //n을 2진수로 변환하여 문자열 반환
        String nBinary = Integer.toBinaryString(n);


        //1의 개수를 계산
        int one_cnt = nBinary.length() - nBinary.replace("1", "").length();


        for(int i =n+1;i<1000000;i++){
            int tmp_cnt = i;
            //다음 큰 수(tmp_cnt)를 2진수로 바꾸고 문자형 반환
            String BigBinary = Integer.toBinaryString(tmp_cnt);
            //1의 개수를 계산
            int bigOne_cnt = BigBinary.length() - BigBinary.replace("1", "").length();

            //1의 개수가 같으면 answer에 저장하고 반복문 탈출
            if (one_cnt == bigOne_cnt) {
                answer =  Integer.parseInt(BigBinary, 2);
                break;
            }
        }
        return answer;
    }
}

//참고: https://fbtmdwhd33.tistory.com/240