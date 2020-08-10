n = int(input())

trailing = 0
five = 5

while five <= n:
    trailing = n//five + trailing
    five = five * 5




print(int(trailing))