sentence = input()
a, b = map(int, input().split())

for i in range(a, a + b):
    print(sentence[i], end="")
    
print()
