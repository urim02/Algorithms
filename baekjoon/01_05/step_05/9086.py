import sys

T = int(input())

for _ in range(T):
    s = sys.stdin.readline().strip()
    # print(s)
    print(s[0] + s[-1])