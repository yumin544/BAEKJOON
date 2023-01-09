i = 0
new_num = None

num = int(input())
if num < 10:
    num * 10
a = num

while new_num != num:
    i += 1
    b = a // 10
    c = a % 10
    d = b + c
    e = d % 10
    new_num = c * 10 + e
    a = new_num
print(i)