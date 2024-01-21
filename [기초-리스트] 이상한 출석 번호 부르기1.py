num = int(input())
a = input().split()
result = [0 for i in range(24)]
for i in range(num):
  result[int(a[i])] += 1
for i in range(1,24):
  print(result[i],end=" ")
