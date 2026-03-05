def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


m, n = map(int, input().split())

min_sum = 100
count = 0

for i in range(m, n + 1):
    s = digit_sum(i)
    if s < min_sum:
        min_sum = s
        count = 1
    elif s == min_sum:
        count += 1

print(count)