num = int(input())
baduk = [[0]*20 for i in range(20)]
    
for i in range(num):
  x,y = input().split()
  baduk[int(x)][int(y)] = 1

for i in range(1,20):
  for j in range(1,20):
    print(baduk[i][j],end=" ")
  print()
