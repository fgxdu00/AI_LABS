a, b, c = map(int, input().split())

has_even = (a % 2 == 0) or (b % 2 == 0) or (c % 2 == 0)
has_odd = (a % 2 != 0) or (b % 2 != 0) or (c % 2 != 0)

if has_even and has_odd:
    print("YES")
else:
    print("NO")