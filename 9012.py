i = int(input())
j = 0

while j < i:
    t = 0
    VPS = input()
    for k in range(len(VPS)):
        if VPS[k] == '(':
            t += 1
        else:
            t -= 1
            if t < 0:
                break
    if t == 0:
        print('YES')
    else:
        print('NO')
    j += 1