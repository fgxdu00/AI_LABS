t = int(input())

for _ in range(t):
    id_, n = map(int, input().split())
    max_val = n
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        if n > max_val:
            max_val = n
    print(id_, max_val)