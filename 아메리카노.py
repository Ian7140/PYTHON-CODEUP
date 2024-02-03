own, coupon = map(int,input().split())
coffee = int(0)
while own>=coupon:
    coffee += int(own // coupon)
    own = (own//coupon) + (own%coupon)

print(coffee)
