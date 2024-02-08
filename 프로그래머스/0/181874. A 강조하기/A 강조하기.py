def solution(myString):
    answer = []
    answer=myString.lower()
    if 'a' in answer : 
        answer = answer.replace('a','A')
    return answer