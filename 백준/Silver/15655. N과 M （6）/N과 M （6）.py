import sys
sys.setrecursionlimit(10 ** 8)

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
result = []
nums.sort()

def backtracking(s):
    if len(result) == m:
        print(" ".join(map(str, result)))
        return

    for i in range(s, n):
        result.append(nums[i])
        backtracking(i+1)
        result.pop()

backtracking(0)