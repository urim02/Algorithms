import sys

remain_set = set()

for _ in range(10):
    num_list = int(sys.stdin.readline())
    remain_set.add(num_list % 42)

print(len(remain_set))
