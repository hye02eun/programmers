def solution(hp):
    answer = 0
    n=int(int(hp)//5)
    if int(hp)%5>= 3 : 
        s=int((hp%5)//3)
        t=int((hp%5)%3)
    else :
        s=0
        t=int(hp%5)
    return n+s+t