def number_spiral(x, y):
    max_num = max(x,y)
    if max_num % 2 == 0:
        return max_num * max_num - (y - 1) - (max_num - x)
    else:
        return max_num * max_num - (x - 1) - (max_num - y)

t = int(input())

datas = []
for i in range(t):
    datas.append(list(map(int, input().split())))

for data in datas:
    print(number_spiral(data[0], data[1]))