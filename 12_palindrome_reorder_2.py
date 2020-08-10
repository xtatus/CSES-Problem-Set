def palindrome_checker(string):
    start = []
    mid = ""

    if len(string)%2 == 0:
        for i in range(0, len(string) - 1, 2):
            if string[i] == string[i+1]:
                start.append(string[i])
            else:
                return "NO SOLUTION"
    else:
        i = 0
        while i < len(string) - 1:
            if string[i] == string[i+1]:
                start.append(string[i])
            else:
                if mid == "":
                    mid = string[i]
                    i -= 1
                else:
                    return "NO SOLUTION"
            i += 2

        if mid == "":
            mid = string[len(string) - 1]

    return "".join(start) + mid + "".join(sorted(start, reverse = True))



string = sorted(input())
print(palindrome_checker(string))
