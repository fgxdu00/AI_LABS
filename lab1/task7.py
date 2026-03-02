def C(n, k):
    if k == 0 or k == n:
        return 1
    return C(n - 1, k - 1) + C(n - 1, k)


n, k = map(int, input().split())
print(C(n, k))
