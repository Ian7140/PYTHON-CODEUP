weight = list(map(int,input().split()))
weight.sort()
for i in range(len(weight)):
  print(weight[i],end=" ")
