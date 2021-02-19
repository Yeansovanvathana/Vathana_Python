v, t, s, d = map(int, input().split())
time = d / v
print("Yes") if time < t or time > s else print("No")

