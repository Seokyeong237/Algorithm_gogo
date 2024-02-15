import sys

input = sys.stdin.readline

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum < n:
        end_index += 1
        sum += end_index
    else:
        sum -= start_index
        start_index += 1

print(count)