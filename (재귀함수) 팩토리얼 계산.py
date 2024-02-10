multiple = 1

def func(a):
    global multiple
    
    if a == 0:
        return 1

    multiple *= a
    func(a - 1)
    
    return multiple

a = int(input())
result = func(a)
print(result)
