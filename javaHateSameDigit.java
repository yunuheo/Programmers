import java.util.ArrayList;
public class HateSameDigit {
    public static void main(String[] args) {
        class Solution {
            public static ArrayList<Integer> solution(int[] arr) {
                ArrayList<Integer> answer = new ArrayList<Integer>();

                for (int i = 0; i < (arr.length-1); i++) {

                    if (i == (arr.length-2)) {
                        if (arr[i] != arr[i+1]) {
                            answer.add(arr[i]);
                            answer.add(arr[i+1]);
                            return answer;
                        }
                        else {
                            answer.add(arr[i]);
                            return answer;
                        }
                    }
                    else if (arr[i] == arr[i+1]) {
                        continue;
                    }
                    else {
                        answer.add(arr[i]);
                    }
                }
                System.out.println(answer);
                return answer;
            }
        }

    }
}
