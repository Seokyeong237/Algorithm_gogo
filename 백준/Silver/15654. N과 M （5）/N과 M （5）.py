import sys

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
answer = []

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(len(nums)):
        if nums[i] not in answer:
            answer.append(nums[i])
            backtracking()
            answer.pop()

backtracking()
