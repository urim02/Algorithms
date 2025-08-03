import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [i + 1 for i in range(N)]
# print(baskets)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    baskets[i - 1], baskets[j - 1] = baskets[j - 1], baskets[i - 1]
    # print(baskets)

print(*baskets)
