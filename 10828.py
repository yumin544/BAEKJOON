result = []
i = int(input())
j = 0
while j < i:
    j += 1
    a = input().split()
    b = a[0]
    if len(a) == 2:
        result.append(a[1])
    elif len(result) and (b == 'pop' or b == 'top'):
        print(result[-1])
        if b == 'pop':
            result.pop()
    elif b == 'size':
        print(len(result))
    elif b == 'empty':
        print(0 if len(result) else 1)
    else:
        print(-1)
# 솔직히 패스