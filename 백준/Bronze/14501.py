import sys

input = sys.stdin.readline

n = int(input())
dp = [0]

# t: 상담을 완료하는데 걸리는 기간
# p: 상담을 했을 때 받을 수 있는 금액
# d[i]: i번째날부터 퇴사날까지 벌 수 있는 최대 수입
# d[i] = d[i+1]: 오늘 시작되는 상담을 했을 때 퇴사일까지 끝나지 않는 경우
# d[i] = Max(d[i+1], d[i+T[i]] + p[i]): 오늘 시작되는 상담을 헸을 때 퇴사일 안에 끝나는 경우
for i in range(n):
    t, p = map(int, input().split()) 

