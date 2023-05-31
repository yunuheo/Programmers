public class Solution {

    public String solution(String s, int n) {
        String answer = "";
        for(int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if(ch==' ') { //공백이면 그대로 붙이고 continue
                answer += ch;
                continue;
            }
            if(ch>='a' && ch<='z') { //소문자일 경우
                if(ch+n > 'z') { //알파벳 범위z를 벗어날 경우 a로 돌아가서(아스키코드값 - 26) n만큼 이동
                    answer += (char)(ch-26+n);
                }else {
                    answer += (char)(ch+n);
                }
            }else if(ch>='A' && ch<='Z') { //대문자일 경우
                if(ch+n > 'Z') {
                    answer += (char)(ch-26+n);
                }else {
                    answer += (char)(ch+n);
                }
            }
        }
        return answer;
    }
}