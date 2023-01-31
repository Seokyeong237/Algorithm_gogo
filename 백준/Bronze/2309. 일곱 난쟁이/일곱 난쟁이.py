a = []

for i in range(0, 9):
    a.append(int(input()))

a.sort()

for k in range(0, len(a)):
    false1 = a[k]
    for j in range(1, len(a)):
        false2 = a[j]

        if (sum(a) - (false1+false2) == 100):
            for l in range(0, len(a)):
                if (l == k or l == j):
                    pass
                else:
                    print(a[l])
            exit(0)