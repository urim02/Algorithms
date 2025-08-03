import sys

N, M = map(int, sys.stdin.readline().split())
baskets = [0] * N

for _ in range(1, M+1):
    i, j, k = map(int, sys.stdin.readline().split())
    for x in range(i-1, j):     # basket 인덱스는 0부터
        print(x)
        baskets[x] = k
        print(baskets)

print(*baskets)