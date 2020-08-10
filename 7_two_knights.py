import math

n = int(input())

for i in range(1, n+1):
    if i == 1:
        valid_turn = 0
    elif i == 2:
        valid_turn = 6
    else:
        k = 2 * ( i - 2) * (i - 1) * 4
        all_turn = i**4 - i**2
        valid_turn = (all_turn - k)//2

    print(valid_turn)