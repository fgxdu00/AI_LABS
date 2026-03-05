n = int(input())

if n == 0:
    print(1)
else:
    if n < 0:
        n = -n
    count = 0
    while n > 0:
        count += 1
        n //= 10
    print(count)