def palindrome_checker(string):
    palindrome = [None] * len(string)
    if len(string)%2 == 0:
        for i in range(0, len(string) - 1, 2):
            if string[i] == string[i+1]:
                palindrome[i] = string[i]
                palindrome[-1-i] = string[i+1]
            else:
                return "NO SOLUTION"
        return "".join(palindrome)

    else:
        i = 0
        while i < len(string) - 1:
            if string[i] == string[i+1]:
                palindrome[i] = string[i]
                palindrome[-1-i] =  string[i+1]
                i += 2
            else:
                if palindrome[len(string)//2] == None:
                    palindrome[len(string)//2] == string[i]
                    i += 1
                else:
                    return "NO SOLUTION"
        if palindrome[len(string)//2] == None:
            palindrome[len(string)//2] = string[len(string)-1]
        return "".join(palindrome)


string = sorted(input())
print(palindrome_checker(string))
