import itertools

def main():
    string = input()
    a = list(itertools.permutations(string))
    b = sorted(list(set(a)))
    print(len(b))
    for word in b:
        print("".join(word))

if __name__ == "__main__":
    main()
