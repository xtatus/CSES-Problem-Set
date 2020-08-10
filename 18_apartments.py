def main():
    n,m,k = list(map(int,input().split()))

    # n: number of applicants
    # m: number of apartments
    # k: maximum allowed difference

    # a: the desired apartment size of each applicant
    a = sorted(list(map(int, input().split())))

    # b: the size of each apartment
    b = sorted(list(map(int, input().split())))
 
    n_get = 0

    for person in a:
        for apartment in b: 
            if person + k < apartment:
                break

            if (person - k <= apartment):
                b.remove(apartment)
                n_get += 1
                break

            b.remove(apartment)

    print(n_get)

if __name__ == "__main__":
    main()
