amount = int(input())
count = amount // 5
money = count * 150000
if amount % 5 != 0 : count+=1
print(count, money)
