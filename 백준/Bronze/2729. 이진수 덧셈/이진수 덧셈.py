n = int(input()) 
for i in range(n):
	a,b = input().split() 
	ans = int(a,2) + int(b,2)
	print(bin(ans)[2:])