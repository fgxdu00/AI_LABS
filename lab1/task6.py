n = int(input())

if n == 1:
    print(0)
else:
    a = 0
    b = 1
    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c
    print(b)
