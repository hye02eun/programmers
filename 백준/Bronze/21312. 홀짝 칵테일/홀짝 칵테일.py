box=list(map(int,input().split()))

#짝수 1개 라도 있는 경우 무조건 출력값은 짝수가 됨
#홀수 3개일 때만 출력

odd=[]
for i in range(3) : 
    if (box[i] %2) != 0 : 
        odd.append(box[i])

#홀수가 없는 경우 짝수의 곱 중 가장 큰 곱
    answer=1
    if not odd : 
        for i in range(3) : 
            answer *= box[i]
    else : 
        for i in range(len(odd)) : 
            answer *= odd[i]
print(answer)