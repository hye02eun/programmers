def solution(my_string):
    answer =0 
    my_string=list(filter (lambda x : x in'123456789', my_string))
    my_string = list(map(int, my_string))
    answer = sum(my_string)
    return answer
            