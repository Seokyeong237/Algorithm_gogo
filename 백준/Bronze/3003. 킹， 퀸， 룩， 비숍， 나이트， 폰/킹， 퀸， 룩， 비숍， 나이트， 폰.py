import sys

chess = [1, 1, 2, 2, 2, 8]
number = list(map(int, sys.stdin.readline().split()))

for i in range(0, 6):
    print(chess[i] - number[i], end=' ')