def solution(my_string, is_suffix):
    key=my_string[1 :]
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else : 
        return 0 
