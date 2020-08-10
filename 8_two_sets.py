def sequence_1(n):
    a = []
    b = []
    for i in range(1, n+1, 4):
        a.append(i)
        a.append(i + 3)
        b.append(i + 1)
        b.append(i + 2)

    return a,b

def sequence_2(n):
    a = [1, 2]
    b = [3]
    for i in range(4 , n+1, 4):
        a.append(i)
        a.append(i+3)
        b.append(i + 1)
        b.append(i+2)

    return a, b

n = int(input())

if n%4 == 0:
    a,b = sequence_1(n)
    print("YES")
    print(n//2)
    print(" ".join(map(str, a)))
    print(n//2)
    print(" ".join(map(str,b)))
elif (n-3)%4 ==0:
    a,b = sequence_2(n)
    print("YES")
    print(n//2)
    print(" ".join(map(str, b)))
    print(n // 2 + 1)
    print(" ".join(map(str, a)))
else:
    print("NO")