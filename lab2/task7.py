x, n, m = map(int, input().split())

result = 1
x = x % m

for i in range(n):
    result = result * x % m

print(result)
