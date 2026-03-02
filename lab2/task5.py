def digit_sum(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


n = int(input())
numbers = list(map(int, input().split()))

min_sum = digit_sum(numbers[0])
result = numbers[0]

for i in range(1, n):
    s = digit_sum(numbers[i])
    if s <= min_sum:
        min_sum = s
        result = numbers[i]

print(result)
