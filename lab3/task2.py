h, w, l, k = map(int, input().split())

volume = h * w * l
batteries = (volume + k - 1) // k

print(batteries)