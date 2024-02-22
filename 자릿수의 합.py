n=int(input())

div=1
s=0
while(s==0 or s>=10): #두자리 수일 때만 돌기
    s=0
    while(n>0):
        s+=int(n%10) # 일의 자리의 값 s에 더함
        n = int(n/10) 
    n=s

print(s)
