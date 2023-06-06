import java.util.*;

public class 문자열내맘데로정렬 {
    public String[] solution(String[] strings, int n) {
        String[] answer = {};
        ArrayList<String> list = new ArrayList<>();

        // n번째 인덱스 글자를 srings배열에 앞에 연결함
        for (int i = 0; i < strings.length; i++) {
            list.add(strings[i].charAt(n) + strings[i]);
        }

        //n번 글자를 기준으로 정렬함과 동시에 사전순으로 정렬 됨
        Collections.sort(list);

        answer = new String[list.size()];
        // 앞에 연결한 문자 자르고 answer 배열에 담기
        for (int i = 0; i < list.size(); i++) {
            answer[i] = list.get(i).substring(1, list.get(i).length());
        }
        return answer;
    }
}
