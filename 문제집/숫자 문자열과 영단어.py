'''
문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/81301
참고 블로그: https://pearlluck.tistory.com/590
'''

def solution(s):
    answer = s

    dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4,
            "five": 5, "six": 6, "seven": 7, "eight": 8, 'nine': 9}

    for item in dict.items():
        answer = answer.replace(item[0],str(item[1]))
    print(int(answer))

solution("one4seveneight")