n = int(input())
array = list(map(int, input().split()))

array = sorted(array)

for i in range(1,n):
    if array[i - 1] != i:
        break
    elif i == len(array):
        i = n

print(i)