money = int(input())
range = [50000,10000,5000,1000,500,100,50,10]
i = count = int(0)
while money != 0:
    if money >= range[i]:
        count += money // range[i]
        money %= range[i]
    else:
        i += 1

print(count)
