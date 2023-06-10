import java.util.*;

class Solution {

    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push('(');
            }
            else if (s.charAt(i) == ')') {

                // 공백스택이 되면 false
                if (stack.isEmpty()) {
                    return false;
                }
                //괄호의 쌍이 맞으면 pop
                stack.pop();
            }
        }
        //마지막 괄호의 짝까지 다 맞으면 공백 스택이 되어야 함
        return stack.isEmpty();
    }
}