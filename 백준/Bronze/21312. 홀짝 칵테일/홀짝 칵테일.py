num = list(map(int, input().split()))

tmp = 1
odd = [] # 홀수 저장

# 홀수 판별
for i in num:
    if i % 2 != 0:
        odd.append(i)
    
if odd:
    for k in odd:
        tmp *= k
else:
    for j in num:
        tmp *= j

print(tmp)