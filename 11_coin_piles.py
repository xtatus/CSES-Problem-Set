def coin_piles(a, b):
    if a == 0 and b == 0:
        return "YES"

    if (2*b - a) % 3 != 0:
        return "NO"

    if (2*a - b) % 3 != 0:
        return "NO"
 
    if 2 >= a/b and a/b >= 0.5:
        return "YES"
    else:
        return "NO"


t = int(input())
array = []
n = []

for i in range(t):
    a, b = (map(int, input().split()))
    print(coin_piles(a, b))
