def solution(n):
    key=[]
    for i in range(0,n+1) : 
        if i%2 != 0 :
            key += [i]
    return key 