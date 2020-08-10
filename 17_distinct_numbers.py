def main():
    n = int(input())
    array = sorted(list(map(int, input().split())))
    distinct = 1
    
    if n == 0:
        print(0)
        return 0
    if n == 1:
        print(1)
        return 0

    for i in range(n-1):
        if array[i] == array[i+1]:
            pass
        else:
            distinct +=1

    print(distinct)

if __name__ == "__main__":
    main()
