import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

m = int(input())
target_list = list(map(int, input().split()))

for i in range(m):
    find = False
    target = target_list[i]

    start = 0
    end = len(A)-1
    while start <= end:
        mid = int((start+end)/2)
        if A[mid] > target:
            end = mid - 1
        elif A[mid] < target:
            start = mid + 1
        else:
            find = True
            break

    if find:
        print(1)
    else:
        print(0)
