import java.util.*;

class Solution {
    public boolean solution(String[] phone_book) {
        //hasSet에서는 각 요소가 중복을 허용하지 않는 고유한 객체(내부적으로 hashMap사용)
        Set<String> set = new HashSet<>();

        //전화번호를 set에 입력
        for (String phone : phone_book) {
            set.add(phone);
        }

        for (String phone : phone_book) {
            for (int i = 1; i < phone.length(); i++) {
                //배열 자료구조에서는 contains()를 사용할 때 O(n)만큼의 시간복잡도를 가지지만
                //set자료구조에서는 O(n)만큼의 속도로 훨신 빠르게 탐색 가능
                if (set.contains(phone.substring(0, i))) {
                    return false;
                }
            }
        }

        return true;
    }
}