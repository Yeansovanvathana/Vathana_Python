a, b = map(int, input().split())
n = list(map(int, input().split()))
s = list(map(int, input().split()))
total = 0
for i in range(b):
    problem_index = s[i] - 1
    total += n[problem_index]
print(total)