import sys

N = int(sys.stdin.readline())
s = input()

sum = 0

for i in range(N):
    sum += int(s[i])

print(sum)