def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(input())
numbers = list(map(int, input().split()))

result = numbers[0]
for i in range(1, n):
    result = gcd(result, numbers[i])

print(result)