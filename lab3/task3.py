n, m, k = map(int, input().split())

boys_rooms = (n + k - 1) // k
girls_rooms = (m + k - 1) // k

print(boys_rooms + girls_rooms)