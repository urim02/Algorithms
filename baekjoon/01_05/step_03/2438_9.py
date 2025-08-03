N = int(input())

# # 2438
# for i in range(1, N+1):
#     print('*' * i)

# 2439
for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * i)