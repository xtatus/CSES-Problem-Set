n = int(input())

if n == 1:
    print("1")
elif n == 3 or n == 2:
    print("NO SOLUTION")
else:
    for i in range(2, n + 1, 2):
        print(i)
    for i in range(1, n+1, 2):
        print(i)
