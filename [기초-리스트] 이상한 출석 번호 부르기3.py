num = int(input())
a = list(map(int,input().split()))
min = int(10001)
for i in range(0,num):
  if a[i] < min:
    min = a[i]
print(min)
