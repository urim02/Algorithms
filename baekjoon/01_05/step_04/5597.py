import sys

summit_nums = [int(sys.stdin.readline()) for _ in range(28)]
# print(summit_nums)

for i in range(1, 31):
    if i not in summit_nums:
        print(i)



