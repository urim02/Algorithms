import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [i + 1 for i in range(N)]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i-1:j] = baskets[i-1:j][::-1]

print(*baskets)
