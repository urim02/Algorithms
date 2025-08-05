d = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
S = input()
time = 0

for i in range(len(S)):
    for j in d:
        if S[i] in j:
            time = time + d.index(j) + 3

print(time)