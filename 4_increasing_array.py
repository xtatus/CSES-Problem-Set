n = int(input())
array = list(map(int, input().split()))


increase = 0
for i in range(len(array)-1):

    if array[i] > array[i+1]:

        increase = - array[i+1] + array[i] + increase
        array[i+1] = array[i]

print(increase)