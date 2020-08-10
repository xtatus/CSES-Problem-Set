dna = input()

repetition = True
max_l = 1
l = 1

for i in range(0, len(dna) - 1):

    if dna[i] != dna[i+1]:
        l += 1
    else:
        l = 1

    if l == 4:
        if dna[i] == dna[i-3]:
           break
        else:
            l = 3

    if l > max_l:
        max_l = l

print(max_l)
