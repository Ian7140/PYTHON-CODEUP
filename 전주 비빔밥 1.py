vegi = input().split()
a = int(vegi[0])
b = int(vegi[1])
c = int(vegi[2])
result = a // 40
if result > b // 50 : result = b//50
if result > c // 30 : result = c//30
print(result)
