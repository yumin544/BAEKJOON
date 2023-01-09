i = int(input())
list = ['1/1']

for j in range(i-1):
    a = int(list[j].split('/')[0])
    b = int(list[j].split('/')[1])
    if a == b == 1:
        list.append('1/2')
    else:
        c = int(list[j-1].split('/')[0])
        d = int(list[j-1].split('/')[1])
        if (a == c and b > d) or (a - c == 1 and d - b == 1 and b != 1):
            list.append(f'{a+1}/{b-1}')
        elif (a > c and b == d) or (c - a == 1 and b - d == 1 and a != 1):
            list.append(f'{a-1}/{b+1}')
        elif b == 1:
            list.append(f'{a+1}/{1}')
        elif a == 1:
            list.append(f'{1}/{b+1}')
print(list[-1])