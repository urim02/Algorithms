import sys

T = int(sys.stdin.readline())

for _ in range(T):
    R, S = map(str, sys.stdin.readline().split())
    R = int(R)
    S = list(S)
    for i in range(len(S)):
        print(S[i] * R, end='')
    print('')                       # 줄 바꿈
    