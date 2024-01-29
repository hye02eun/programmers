def solution(todo_list, finished):
    N=len(todo_list)
    answer=[]
    for i in range (0, N) :
        if finished[i] == False : 
            answer.append(todo_list[i])            
    return answer
        