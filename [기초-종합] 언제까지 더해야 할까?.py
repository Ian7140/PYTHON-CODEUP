num = int(input())
count = int(0)
for i in range(1,num+1):
  count += i
  if count >= num:
    print(i)
    break
