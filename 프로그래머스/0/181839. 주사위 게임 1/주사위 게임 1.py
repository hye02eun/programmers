def solution(a, b):
    score = 0
    if (a*b) %2 != 0 : 
        score = a**2 + b**2
    elif a %2 != 0 or b %2 != 0 : 
        score = 2*(a+b)
    elif a%2 == 0 and b%2 == 0 : 
        score = abs(a-b)
    return score
        