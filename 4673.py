new_list = []

def selfnum(a):
    b = len(str(a))
    c = int(a)
    j = 1
    for l in range(b):
        c += (a // j) % 10
        j *= 10
    return c

for i in range(10000):
    new_list.append(selfnum(i))
    if i not in new_list:
        print(i)