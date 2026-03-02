def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return a // gcd(a, b) * b


n = int(input())

result = 1
for i in range(2, n + 1):
    result = lcm(result, i)

print(result)
