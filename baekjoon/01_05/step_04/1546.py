import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

max_score = max(scores)

manipulated = [(s / max_score) * 100 for s in scores]

average = sum(manipulated) / N
print(average)