def solution(num_list):
    answer = []
    if num_list[-1] >num_list[-2] : 
        a= num_list[-1] - num_list[-2]
    if num_list[-1] <=num_list[-2] : 
        a= int(num_list[-1])*2
    answer=num_list+[a]
    return answer