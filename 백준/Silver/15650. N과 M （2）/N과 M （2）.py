import sys

input = sys.stdin.readline

n, m = map(int, input().split())
answer = []

def backtracking():
    if len(answer) == m:
        print(" ".join(map(str, answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            if len(answer) > 0:
                if i < answer[len(answer)-1]:
                    continue
            answer.append(i)
            backtracking()
            answer.pop()

backtracking()