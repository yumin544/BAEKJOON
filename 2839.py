N = int(input())
i = 0

while True:
    a = i + (N // 3)
    if N < 5 and N % 3 == 0:
        print(a)
        break
    if N < 5 and N % 3 != 0:
        print(-1)
        break
    if N >= 5 and N % 3 == 0 and N < 15:
        print(a)
        break
    elif N >= 5:
        i += 1
        N = N - 5