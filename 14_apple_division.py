from itertools import chain, combinations

def main():
    n = int(input())
    array = sorted(list(map(int, input().split())))

    target = sum(array)/2
    sum_curr = 0
    minimum = target

    for i in range(n+1):
        sum_prev = sum_curr
        words = combinations(array,i)
        for word in words:

            if sum(word) >= target:
                minimum = min(minimum, abs(sum_prev - target), abs(sum(word) - target))
            sum_prev = sum(word)

    print(int(minimum*2))

if __name__ == "__main__":
    main()
