num = int(input())
want = list(map(int,input().split()))
cake = [i for i in range(1,num+1)]
once = twice = int(0)
for i in range(0,num):
    if want[i] == 1:
        if cake[want[i]] != 0:
            cake[want[i]-1]=0
            once += 1
    elif want[i] == num:
        if cake[want[i]-2] != 0:
            cake[want[i]-1]=0
            once+=1
    else:
        if cake[want[i]] != 0 and cake[want[i]-2] != 0:
            twice+=1
            cake[want[i]-1] = 0
        elif cake[want[i]] == 0 and cake[want[i]-2] == 0:
            cake[want[i]-1]=0
        elif cake[want[i]] == 0 or cake[want[i]-2] == 0:
            cake[want[i]-1]=0
            once+=1

print(once, twice)
