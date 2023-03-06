N = int(input())
a = list(map(int, input().split()))
v = 0

find = int(input())

for i in range(len(a)):
    if (a[i] == find):
        v += 1

print(v)

